import time
import allure
import pytest
import data
from authorization.pages.signin_password_page import SignInPasswordPage
from authorization.locators.signin_password_page_locators import SignInPasswordPageLocators as signin_password


class TestSignInPassword():

    def test_enter_registered_password(self, browser, login):
        language = login
        password = SignInPasswordPage(browser)
        password.find_password_field_and_type_text(data.EXISTING_PASSWORD)
        password.click_enter_button(language)
        password.wait_url_to_be(data.URL_LK_DASHBOARD)
        current_url = password.get_current_url()
        assert current_url == data.URL_LK_DASHBOARD, f'Актуальный адрес страницы ЛК {current_url} не равен ожидаемому {data.URL_LK_DASHBOARD}'
    
    def test_enter_unregistered_password(self, browser, login):
        language = login
        password = SignInPasswordPage(browser)
        password.find_password_field_and_type_text(data.NONEXISTING_PASSWORD)
        password.click_enter_button(language)
        assert password.find_error_message(language), f'Текст ошибки не найден'

    def test_empty_password_field(self, browser, login):
        language = login
        password = SignInPasswordPage(browser)
        button = password.find_enter_button(language)
        assert not button.is_enabled()
