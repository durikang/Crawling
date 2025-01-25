import time

def highlight_element(driver, element):
    """
    특정 요소를 빨간색 박스로 강조하여 스크롤 이동 및 시각적 확인을 용이하게 합니다.
    """
    driver.execute_script(
        "arguments[0].style.border='3px solid red'; arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});",
        element
    )
    time.sleep(0.5)  # 강조 효과를 확인할 수 있도록 대기


def clear_highlight(driver):
    """
    강조 효과를 초기화하여 페이지의 모든 강조된 스타일을 제거합니다.
    """
    driver.execute_script("""
        var elements = document.querySelectorAll('*');
        elements.forEach(function(el) {
            el.style.border = '';
        });
    """)


def get_rank_data(driver, rank_xpath):
    """
    주어진 XPath를 기준으로 순위 데이터를 추출합니다.
    :param driver: Selenium WebDriver
    :param rank_xpath: 순위 데이터가 위치한 XPath
    :return: 순위 데이터를 포함한 리스트
    """
    rank_elements = driver.find_elements("xpath", rank_xpath)
    return [rank.text.strip() for rank in rank_elements]


def wait_for_element(driver, xpath, timeout=10):
    """
    지정된 XPath의 요소가 로드될 때까지 대기합니다.
    :param driver: Selenium WebDriver
    :param xpath: 요소를 찾기 위한 XPath
    :param timeout: 대기 시간 (초)
    :return: 찾은 WebElement
    """
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC

    return WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.XPATH, xpath)))


def get_table_data(driver, table_xpath, rank_xpath=None):
    """
    테이블 데이터와 선택적으로 순위 데이터를 함께 추출합니다.
    :param driver: Selenium WebDriver
    :param table_xpath: 테이블의 XPath
    :param rank_xpath: 순위 데이터의 XPath (선택적)
    :return: 순위와 테이블 데이터를 포함한 리스트
    """
    if rank_xpath:
        ranks = get_rank_data(driver, rank_xpath)
    else:
        ranks = []

    table_rows = driver.find_elements("xpath", f"{table_xpath}//tr")
    data = []
    for i, row in enumerate(table_rows[1:]):  # 첫 번째 행(헤더)은 제외
        cols = [col.text.strip() for col in row.find_elements_by_tag_name("td")]
        if cols:
            if ranks and i < len(ranks):
                data.append([ranks[i]] + cols)
            else:
                data.append(cols)
    return data
