import pytest
import allure
import data
from selenium import webdriver
# from selenium.webdriver.firefox.options import Options
# from selenium.webdriver.firefox.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from authorization.pages.signin_page import SignInPage
from authorization.pages.signup_password_page import SignUpPasswordPage
from helpers import fake_email, fake_random_password


# @pytest.fixture(scope="function")
# def browser():
#     options = Options()
#     options.add_argument('--window-size=1920,1080')
#     browser = webdriver.Firefox(service=Service(
#         GeckoDriverManager().install()), options=options)
#     yield browser
#     browser.quit()

# @pytest.fixture(scope="function")
# @allure.title('Инициализация драйвера Chrome')
# def browser():
#     options = Options()
#     options.add_argument("--headless")
#     options.add_argument('--window-size=1920,1080')
#     service = Service(
#         executable_path='/Users/macbook/Desktop/WebDriver/bin/chromedriver')
#     browser = webdriver.Chrome(service=service, options=options)
#     yield browser
#     browser.quit()

@pytest.fixture(scope="function")
@allure.title('Инициализация драйвера Chrome')
def browser():
    options = Options()
    options.add_argument("--headless")
    options.add_argument('--window-size=1920,1080')
    browser = webdriver.Chrome(options=options)
    yield browser
    browser.quit()

@pytest.fixture(scope="function", params=['en', 'ru', 'pt'])
@allure.title('Смена языка')
def language(browser, request):
    signin_page = SignInPage(browser)
    browser.get(data.URL_SIGNIN)
    signin_page.change_language(request.param)
    return request.param


@pytest.fixture(scope="function")
@allure.title('Логин существующего пользователя')
def login(browser, language):
    signin_page = SignInPage(browser)
    signin_page.find_email_field_and_type_text(data.EXISTING_EMAIL)
    signin_page.click_continue_button(language)
    signin_page.wait_password_url_to_be(data.URL_SIGNIN_PASSWORD)
    return language


@pytest.fixture(scope="function")
@allure.title('Создание логина для несуществующего пользователя')
def create_login(browser, language):
    signin_page = SignInPage(browser)
    email = fake_email()
    signin_page.find_email_field_and_type_text(email)
    signin_page.click_continue_button(language)
    signin_page.wait_signup_url_to_be(data.URL_SIGNUP)
    return language


@pytest.fixture(scope="function")
@allure.title('Создание логина и пароля для несуществующего пользователя')
def create_login_and_password(browser, language):
    login = SignInPage(browser)
    email = fake_email()
    login.find_email_field_and_type_text(email)
    login.click_continue_button(language)
    login.wait_signup_url_to_be(data.URL_SIGNUP)
    correct_password = fake_random_password(8)
    password = SignUpPasswordPage(browser)
    password.find_password_field_and_type_text(correct_password)
    password.find_repeat_password_field_and_type_text(correct_password)
    password.click_continue_button(language)
    password.wait_verification_code_url_to_be(data.URL_VERIFICATION_CODE)
    return language
