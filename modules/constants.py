# 연도별 URL 리스트
YEARS = [2024, 2023, 2022, 2021, 2020]
BASE_URL = "https://sports.news.naver.com/kbaseball/record/index?category=kbo&year="

# XPaths
XPATHS = {
    # 팀 순위 관련
    "team_table": '//*[@id="content"]/div[2]/div/div[2]/table',
    "team_rank": '//*[@id="regularTeamRecordList_table"]/tr/th',

    # 투수 관련
    "pitcher_tab": '//*[@id="_playerTypeList"]/li[1]/a',
    "pitcher_table_1": '//*[@id="_pitcherRecord"]/table[1]',
    "pitcher_rank_1": '//*[@id="_pitcherRecord"]/table[1]/tbody/tr/th',
    "pitcher_table_2": '//*[@id="_pitcherRecord"]/table[2]',
    "pitcher_rank_2": '//*[@id="_pitcherRecord"]/table[2]/tbody/tr/th',
    "pitcher_more_button": '//*[@id="_pitcherRecord"]/a[1]',

    # 타자 관련
    "batter_tab": '//*[@id="_playerTypeList"]/li[2]/a',
    "batter_table_1": '//*[@id="_batterRecord"]/table[1]',
    "batter_rank_1": '//*[@id="_batterRecord"]/table[1]/tbody/tr/th',
    "batter_table_2": '//*[@id="_batterRecord"]/table[2]',
    "batter_rank_2": '//*[@id="_batterRecord"]/table[2]/tbody/tr/th',
    "batter_more_button": '//*[@id="_batterRecord"]/a[1]',
}

# 컬럼 정의
COLUMNS = {
    # 팀 순위 데이터 컬럼
    "team": ["년도", "순위", "팀", "경기수", "승", "패", "무", "승률", "게임차", "득점", "실점", "득실차"],

    # 투수 테이블 1 데이터 컬럼
    "pitcher_table_1": ["년도", "순위", "선수", "평균자책", "경기수", "이닝", "승", "패", "세이브", "홀드", "탈삼진",
                        "피안타", "피홈런", "실점", "볼넷", "사구", "승률", "비고"],

    # 투수 테이블 2 데이터 컬럼
    "pitcher_table_2": ["년도", "순위", "이름", "WHIP", "K/9", "BB/9", "K/BB", "K%", "BB%", "WPA", "WAR", "비고"],

    # 타자 테이블 1 데이터 컬럼
    "batter_table_1": ["년도", "순위", "선수", "타율", "경기수", "타수", "안타", "2루타", "3루타", "홈런", "타점",
                       "득점", "도루", "볼넷", "삼진", "출루율", "장타율", "비고"],

    # 타자 테이블 2 데이터 컬럼
    "batter_table_2": ["년도", "순위", "이름", "OPS", "IsoP", "BABIP", "wOBA", "wRC+", "WPA", "WAR", "비고"],
}
