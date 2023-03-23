import traceback

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.select import Select


def get_value(
    driver: WebDriver, select_value: str, element_key: str
) -> tuple[str, str]:
    select_value_result = ""
    text_field_value_result = ""

    try:
        # セレクトの要素をIDから取得し、valueから選択
        Select(driver.find_element(By.ID, "demo-simple-select")).select_by_value(
            select_value
        )

        # テキストの要素をセレクターで取得し、”武蔵”を入力
        driver.find_element(By.CSS_SELECTOR, "#demo-simple-text").send_keys(element_key)

        # チェックボックスの要素をxpathで取得し、クリック
        driver.find_element(
            By.ID,
            "checkbox",
        ).click()

        # 決定ボタンをクリック
        driver.find_element(By.ID, "decision").click()

        # 表を出力
        table = driver.find_element(
            By.XPATH, "//*[@id='root']/div/div/div[2]/table"
        ).text
        print(table)

        # セレクトの値を取得
        select_value_result = driver.find_element(
            By.XPATH, "//*[@id='root']/div/div/div[2]/table/tbody/tr[1]/td[2]"
        ).text

        # テキストフィールドの値を取得
        text_field_value_result = driver.find_element(
            By.XPATH, "//*[@id='root']/div/div/div[2]/table/tbody/tr[2]/td[2]"
        ).text

    except Exception:
        print(traceback.format_exc())

    finally:
        driver.quit()

    return select_value_result, text_field_value_result
