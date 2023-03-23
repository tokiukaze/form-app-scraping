import traceback

from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver

from selenium_sample.main import get_value


# get_value()のテスト
def test_get_value() -> None:
    options = webdriver.ChromeOptions()
    # ヘッドレスモードを有効にする（次の行をコメントインすると画面が表示されない）
    # options.add_argument("--headless")
    driver: WebDriver = webdriver.Remote(
        command_executor="http://host.docker.internal:4444/wd/hub", options=options
    )
    driver.implicitly_wait(5)
    # tokiukazeのdemoページにアクセス
    driver.get("https://form-app.tokiukaze.com")
    # テスト用のwebdriverを渡して、get_value()を実行
    select_value, text_field_value = get_value(driver, "shigure", "武蔵")
    # セレクトの値が”shigure”であることを確認
    assert select_value == "shigure"
    # テキストフィールドの値が”武蔵”であることを確認
    assert text_field_value == "武蔵"
