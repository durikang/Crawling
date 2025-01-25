# data_collection.py

import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from helpers import highlight_element, clear_highlight, get_rank_data
from constants import XPATHS


def collect_team_data(driver, year):
    """팀 순위 데이터 수집"""
    # 테이블이 로드될 때까지 대기
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, XPATHS["team_table"])))

    # 순위 데이터 가져오기
    ranks = get_rank_data(driver, XPATHS["team_rank"])

    # 팀 테이블 로드 및 강조 표시
    team_table = driver.find_element(By.XPATH, XPATHS["team_table"])
    highlight_element(driver, team_table)

    # 각 행에서 데이터 추출
    rows = team_table.find_elements(By.XPATH, ".//tr")[1:]  # 헤더 제외
    team_data = []

    for i, row in enumerate(rows):
        # 각 열 데이터를 리스트로 변환
        cols = [col.text.strip() for col in row.find_elements(By.TAG_NAME, "td")]
        # 순위 데이터와 함께 각 행의 데이터를 저장
        if cols and i < len(ranks):
            team_data.append([year, ranks[i]] + cols)

    # 강조 표시 제거
    clear_highlight(driver)

    return team_data


def collect_pitcher_data(driver, year):
    """투수 데이터 수집"""
    pitcher_data_1 = []
    pitcher_data_2 = []

    # 투수 탭 선택
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, XPATHS["pitcher_tab"]))).click()

    # 투수 테이블 1 데이터 수집
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, XPATHS["pitcher_table_1"])))
    time.sleep(1)  # 안정성 확보를 위해 대기
    ranks_1 = get_rank_data(driver, XPATHS["pitcher_rank_1"])
    table_1_rows = driver.find_elements(By.XPATH, XPATHS["pitcher_table_1"] + "//tr")[1:]
    # 테이블 요소를 직접 가져와 강조
    pitcher_table_1 = driver.find_element(By.XPATH, XPATHS["pitcher_table_1"])
    highlight_element(driver,pitcher_table_1)

    for i, row in enumerate(table_1_rows):
        cols = [col.text.strip() for col in row.find_elements(By.TAG_NAME, "td")]
        if cols and i < len(ranks_1):
            name, team = cols[0].split("(",1) if "(" in cols[0] else (cols[0], "")
            team = team.rstrip(")") # 닫는 괄호 제거
            cols[0] = name.strip() # 이름만 남기기
            cols.append(team) # 비고 열에 팀 이름 추가
            pitcher_data_1.append([year, ranks_1[i]] + cols)


    # 강조 표시 제거
    clear_highlight(driver)

    # 테이블2 버튼 요소를 직접 가져와 강조
    pitcher_more_button = driver.find_element(By.XPATH, XPATHS["pitcher_more_button"])
    highlight_element(driver,pitcher_more_button)

    # 투수 테이블 2 데이터 수집
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, XPATHS["pitcher_more_button"]))).click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, XPATHS["pitcher_table_2"])))
    time.sleep(1)  # 안정성 확보를 위해 대기
    ranks_2 = get_rank_data(driver, XPATHS["pitcher_rank_2"])
    table_2_rows = driver.find_elements(By.XPATH, XPATHS["pitcher_table_2"] + "//tr")[1:]

    # 테이블 요소를 직접 가져와 강조
    pitcher_table_2 = driver.find_element(By.XPATH, XPATHS["pitcher_table_2"])
    highlight_element(driver,pitcher_table_2)

    for i, row in enumerate(table_2_rows):
        cols = [col.text.strip() for col in row.find_elements(By.TAG_NAME, "td")]
        if cols and i < len(ranks_2):
            name, team = cols[0].split("(",1) if "(" in cols[0] else (cols[0], "")
            team = team.rstrip(")") # 닫는 괄호 제거
            cols[0] = name.strip() # 이름만 남기기
            cols.append(team) # 비고 열에 팀 이름 추가
            pitcher_data_2.append([year, ranks_2[i]] + cols)

    # 강조 표시 제거
    clear_highlight(driver)

    return pitcher_data_1, pitcher_data_2


def collect_batter_data(driver, year):
    """타자 데이터 수집"""
    batter_data_1 = []
    batter_data_2 = []

    # 타자 탭 선택
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, XPATHS["batter_tab"]))).click()

    # 타자 테이블 1 데이터 수집
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, XPATHS["batter_table_1"])))
    time.sleep(1)  # 안정성 확보를 위해 대기
    ranks_1 = get_rank_data(driver, XPATHS["batter_rank_1"])
    table_1_rows = driver.find_elements(By.XPATH, XPATHS["batter_table_1"] + "//tr")[1:]
    # 테이블 요소를 직접 가져와 강조
    batter_table_1 = driver.find_element(By.XPATH, XPATHS["batter_table_1"])
    highlight_element(driver,batter_table_1)


    for i, row in enumerate(table_1_rows):
        cols = [col.text.strip() for col in row.find_elements(By.TAG_NAME, "td")]
        if cols and i < len(ranks_1):
            name, team = cols[0].split("(",1) if "(" in cols[0] else (cols[0], "")
            team = team.rstrip(")") # 닫는 괄호 제거
            cols[0] = name.strip() # 이름만 남기기
            cols.append(team) # 비고 열에 팀 이름 추가
            batter_data_1.append([year, ranks_1[i]] + cols)

    clear_highlight(driver)

    # 테이블2 버튼 요소를 직접 가져와 강조
    batter_more_button = driver.find_element(By.XPATH, XPATHS["batter_more_button"])
    highlight_element(driver,batter_more_button)
    clear_highlight(driver)

    # 타자 테이블 2 데이터 수집
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, XPATHS["batter_more_button"]))).click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, XPATHS["batter_table_2"])))
    time.sleep(1)  # 안정성 확보를 위해 대기
    ranks_2 = get_rank_data(driver, XPATHS["batter_rank_2"])
    table_2_rows = driver.find_elements(By.XPATH, XPATHS["batter_table_2"] + "//tr")[1:]

    # 테이블 요소를 직접 가져와 강조
    batter_table_2 = driver.find_element(By.XPATH, XPATHS["batter_table_2"])
    highlight_element(driver,batter_table_2)

    for i, row in enumerate(table_2_rows):
        cols = [col.text.strip() for col in row.find_elements(By.TAG_NAME, "td")]
        if cols and i < len(ranks_2):
            name, team = cols[0].split("(",1) if "(" in cols[0] else (cols[0], "")
            team = team.rstrip(")") # 닫는 괄호 제거
            cols[0] = name.strip() # 이름만 남기기
            cols.append(team) # 비고 열에 팀 이름 추가
            batter_data_2.append([year, ranks_2[i]] + cols)

    clear_highlight(driver)

    return batter_data_1, batter_data_2