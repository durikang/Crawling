import os
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from constants import YEARS, BASE_URL, COLUMNS, XPATHS
from data_collection import collect_team_data, collect_pitcher_data, collect_batter_data
from data_processing import adjust_columns, save_to_excel

# Selenium WebDriver 설정
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

# 데이터 수집
team_data = []
pitcher_table_1_data, pitcher_table_2_data = [], []
batter_table_1_data, batter_table_2_data = [], []

for year in YEARS:
    driver.get(f"{BASE_URL}{year}")

    # 팀 순위 데이터 수집
    team_data.extend(collect_team_data(driver, year))

    # 투수 데이터 수집
    pitcher_data_1, pitcher_data_2 = collect_pitcher_data(driver, year)
    pitcher_table_1_data.extend(pitcher_data_1)
    pitcher_table_2_data.extend(pitcher_data_2)

    # 타자 데이터 수집
    batter_data_1, batter_data_2 = collect_batter_data(driver, year)
    batter_table_1_data.extend(batter_data_1)
    batter_table_2_data.extend(batter_data_2)

driver.quit()

# 데이터 처리
team_data = adjust_columns(team_data, len(COLUMNS["team"]))
pitcher_table_1_data = adjust_columns(pitcher_table_1_data, len(COLUMNS["pitcher_table_1"]))
pitcher_table_2_data = adjust_columns(pitcher_table_2_data, len(COLUMNS["pitcher_table_2"]))
batter_table_1_data = adjust_columns(batter_table_1_data, len(COLUMNS["batter_table_1"]))
batter_table_2_data = adjust_columns(batter_table_2_data, len(COLUMNS["batter_table_2"]))

# 데이터프레임 생성
team_df = pd.DataFrame(team_data, columns=COLUMNS["team"])
pitcher_table_1_df = pd.DataFrame(pitcher_table_1_data, columns=COLUMNS["pitcher_table_1"])
pitcher_table_2_df = pd.DataFrame(pitcher_table_2_data, columns=COLUMNS["pitcher_table_2"])
batter_table_1_df = pd.DataFrame(batter_table_1_data, columns=COLUMNS["batter_table_1"])
batter_table_2_df = pd.DataFrame(batter_table_2_data, columns=COLUMNS["batter_table_2"])

# 엑셀 저장
output_file = "kbo_stats.xlsx"

save_to_excel(output_file,
              [team_df, pitcher_table_1_df, pitcher_table_2_df, batter_table_1_df, batter_table_2_df],
              ["팀 순위", "투수 테이블 1", "투수 테이블 2", "타자 테이블 1", "타자 테이블 2"])

print("데이터 수집 및 저장 완료!")
os.startfile(output_file)
