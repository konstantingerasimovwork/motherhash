import pytest
import allure
import data
from selenium import webdriver
# from selenium.webdriver.firefox.options import Options
# from selenium.webdriver.firefox.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from authorization.pages.signin_page import SignInPage


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
@allure.title('Инициализация драйвера')
def browser():
    options = Options()
    options.add_argument('--window-size=1920,1080')
    # options.add_argument("--lang=ru")
    service = Service(
        executable_path='/Users/macbook/Desktop/WebDriver/bin/chromedriver')
    browser = webdriver.Chrome(service=service, options=options)
    yield browser
    browser.quit()


#Ввод зарегистрированного email
@pytest.fixture(scope="function", params=['en', 'ru', 'pt'])
@allure.title('Логин существующего пользователя')
def login(browser, request):
    signin_page = SignInPage(browser)
    browser.get(data.URL_SIGNIN)
    signin_page.change_language(request.param)
    signin_page.find_email_field_and_type_text(data.EXISTING_EMAIL)
    signin_page.click_continue_button(request.param)
    signin_page.wait_signup_url_to_be(data.URL_SIGNIN_PASSWORD)
    return request.param

