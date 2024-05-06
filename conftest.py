import pytest
from selenium import webdriver
# from selenium.webdriver.firefox.options import Options
# from selenium.webdriver.firefox.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service


# @pytest.fixture(scope="function")
# def browser():
#     options = Options()
#     options.add_argument('--window-size=1920,1080')
#     browser = webdriver.Firefox(service=Service(
#         GeckoDriverManager().install()), options=options)
#     yield browser
#     browser.quit()

# подключение драйвера Chrome
@pytest.fixture(scope="function")
def browser():
    options = Options()
    options.add_argument('--window-size=1920,1080')
    # options.add_argument("--lang=ru")
    service = Service(
        executable_path='/Users/macbook/Desktop/WebDriver/bin/chromedriver')
    browser = webdriver.Chrome(service=service, options=options)
    yield browser
    browser.quit()


    

