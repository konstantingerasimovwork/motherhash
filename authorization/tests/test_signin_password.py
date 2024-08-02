import time
import allure
import data
from authorization.pages.signin_password_page import SignInPasswordPage


@allure.suite('SignIn Password')
class TestSignInPassword():

    @allure.sub_suite('1. Проверка ввода пароля для зарегистрированного в базе пользователя в поле ввода')
    def test_enter_registered_password(self, browser, login):
        allure.dynamic.title(
            f'{login}  - Проверка ввода пароля для зарегистрированного в базе пользователя в поле ввода')
        language = login
        password = SignInPasswordPage(browser)
        password.find_password_field_and_type_text(data.EXISTING_PASSWORD)
        password.click_enter_button(language)
        password.wait_url_to_be(data.URL_LK_DASHBOARD)
        current_url = password.get_current_url()
        assert current_url == data.URL_LK_DASHBOARD, f'Актуальный адрес страницы ЛК {current_url} не равен ожидаемому {data.URL_LK_DASHBOARD}'

    @allure.sub_suite('2. Проверка ввода пароля, отличного от указанного при успешной регистрации в поле ввода')
    def test_enter_unregistered_password(self, browser, login):
        allure.dynamic.title(
            f'{login}  - Проверка ввода пароля, отличного от указанного при успешной регистрации в поле ввода')
        language = login
        password = SignInPasswordPage(browser)
        password.find_password_field_and_type_text(data.NONEXISTING_PASSWORD)
        password.click_enter_button(language)
        assert password.find_error_message(language), f'Текст ошибки не найден'

    @allure.sub_suite('3. Проверка: Оставить поле пустым')
    def test_empty_password_field(self, browser, login):
        allure.dynamic.title(
            f'{login}  - Проверка: Оставить поле пустым')
        language = login
        password = SignInPasswordPage(browser)
        button = password.find_enter_button(language)
        assert not button.is_enabled()
