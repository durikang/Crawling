# .\venv\Scripts\activate
# https://www.youtube.com/watch?v=zRKm0BkzSM8
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
options.add_experimental_option('detach', True) # 브라우저 바로 닫힘 방지
options.add_experimental_option('excludeSwitches', ['enable-logging']) # 불필요한 메시지 제거

# 1
# chrome_driver = ChromeDriverManager().install()
# print(chrome_driver)
# 설치경로 C:\Users\newstep\.wdm\drivers\chromedriver\win64\120.0.6099.109\chromedriver-win32/chromedriver.exe
service = Service(ChromeDriverManager().install()) # 크롬드라이버 업데이트 되어도 신경 안써도 된다
# service = Service(ChromeDriverManager(path="DRIVER").install()) # 원하는 경로에 설치

driver = webdriver.Chrome(service=service, options=options)

driver.get('https://naver.com')