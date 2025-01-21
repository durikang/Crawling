from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time

# ChromeDriver 경로 설정 (본인 환경에 맞게 수정)
chrome_driver_path = "C:/path/to/chromedriver.exe"  # 적절한 경로로 수정하세요

# Selenium WebDriver 설정
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # 브라우저 창을 띄우지 않음
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")

# Service 객체로 ChromeDriver 경로 설정
service = Service(chrome_driver_path)

# WebDriver 초기화
driver = webdriver.Chrome(service=service, options=options)

# 연도별 URL 리스트
years = [2024, 2023, 2022, 2021, 2020]
base_url = "https://sports.news.naver.com/kbaseball/record/index?category=kbo&year="

# 데이터를 저장할 리스트
team_data, pitcher_data, batter_data = [], [], []

# XPaths
team_xpath = '//*[@id="content"]/div[2]/div/div[2]/table'
pitcher_xpath = '//*[@id="_pitcherRecord"]/table[1]'
batter_xpath = '//*[@id="_batterRecord"]/table[1]'

# 연도별 데이터 수집
for year in years:
    url = f"{base_url}{year}"
    driver.get(url)

    try:
        # 팀 순위 데이터 수집
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, team_xpath)))
        team_table = driver.find_element(By.XPATH, team_xpath)
        for row in team_table.find_elements(By.TAG_NAME, "tr")[1:]:  # 헤더 제외
            cols = [col.text.strip() for col in row.find_elements(By.TAG_NAME, "td")]
            if cols:
                team_data.append([year] + cols)

        # 투수 순위 데이터 수집
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, pitcher_xpath)))
        pitcher_table = driver.find_element(By.XPATH, pitcher_xpath)
        for row in pitcher_table.find_elements(By.TAG_NAME, "tr")[1:]:
            cols = [col.text.strip() for col in row.find_elements(By.TAG_NAME, "td")]
            if cols:
                pitcher_data.append([year] + cols)

        # 타자 순위 데이터 수집
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, batter_xpath)))
        batter_table = driver.find_element(By.XPATH, batter_xpath)
        for row in batter_table.find_elements(By.TAG_NAME, "tr")[1:]:
            cols = [col.text.strip() for col in row.find_elements(By.TAG_NAME, "td")]
            if cols:
                batter_data.append([year] + cols)

    except Exception as e:
        print(f"Error collecting data for year {year}: {e}")

# WebDriver 종료
driver.quit()

# 데이터프레임 생성 및 저장
team_columns = ["Year", "Rank", "Team", "Games", "Wins", "Losses", "Draws", "WinRate", "GamesBehind", "Runs", "Allowed", "RunDiff"]
pitcher_columns = ["Year", "Rank", "Player", "Team", "ERA", "Games", "Innings", "Wins", "Losses", "Saves", "Holds", "Strikeouts",
                   "HitsAllowed", "HomeRunsAllowed", "RunsAllowed", "Walks", "HitByPitch", "WinRate", "WHIP", "K/9", "BB/9", "K/BB", "K%", "BB%", "WPA", "WAR"]
batter_columns = ["Year", "Rank", "Player", "Team", "AVG", "Games", "AtBats", "Hits", "Doubles", "Triples", "HomeRuns", "RBIs",
                  "Runs", "StolenBases", "Walks", "Strikeouts", "OBP", "SLG", "OPS", "IsoP", "BABIP", "wOBA", "wRC+", "WPA", "WAR"]

team_df = pd.DataFrame(team_data, columns=team_columns)
pitcher_df = pd.DataFrame(pitcher_data, columns=pitcher_columns)
batter_df = pd.DataFrame(batter_data, columns=batter_columns)

with pd.ExcelWriter("kbo_stats.xlsx") as writer:
    team_df.to_excel(writer, sheet_name="팀순위", index=False)
    pitcher_df.to_excel(writer, sheet_name="투수순위", index=False)
    batter_df.to_excel(writer, sheet_name="타자순위", index=False)

print("데이터 수집 및 저장 완료!")
