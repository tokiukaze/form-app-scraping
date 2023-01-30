import traceback

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.select import Select

options = webdriver.ChromeOptions()
# ヘッドレスモードを有効にする（次の行をコメントインすると画面が表示されない）
# options.add_argument("--headless")
driver: WebDriver = webdriver.Remote(
    command_executor="http://host.docker.internal:4444/wd/hub", options=options
)
driver.implicitly_wait(5)
try:
    # tokiukazeのdemoページにアクセス
    driver.get("https://form-app.tokiukaze.com")

    # セレクトの要素をIDから取得し、valueから選択
    Select(driver.find_element(By.ID, "demo-simple-select")).select_by_value("shigure")

    # テキストの要素をセレクターで取得し、”武蔵”を入力
    driver.find_element(By.CSS_SELECTOR, "#\:r1\:").send_keys("武蔵")

    # チェックボックスの要素をxpathで取得し、クリック
    driver.find_element(
        By.ID,
        "checkbox",
    ).click()

    # 決定ボタンをクリック
    driver.find_element(By.ID, "decision").click()

    # 表を出力
    table = driver.find_element(By.XPATH, "//*[@id='root']/div/div/div[2]/table").text
    print(table)


except Exception as e:
    print(traceback.format_exc())
finally:
    driver.quit()
