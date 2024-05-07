import time
import allure
import pytest
import data
from authorization.pages.reset_password_page import ResetPasswordPage
from authorization.locators.reset_password_page_locators import ResetPasswordPageLocators as reset_password


class TestResetPassword():

    def test_go_to_the_reset_password_page(self, browser, login):
        language = login
        password = ResetPasswordPage(browser)
        password.click_forgot_password_button(language)
        password.wait_url_to_be(data.URL_FORGOT_PASSWORD)
        current_url = password.get_current_url()
        assert current_url == data.URL_FORGOT_PASSWORD, f'Актуальный адрес страницы восстановления пароля {current_url} не равен ожидаемому {data.URL_FORGOT_PASSWORD}'

    def test_check_reset_button_with_empty_fields(self, browser, login):
        language = login
        password = ResetPasswordPage(browser)
        password.click_forgot_password_button(language)
        password.wait_url_to_be(data.URL_FORGOT_PASSWORD)
        reset_password_button = password.find_reset_password_button(language)
        assert not reset_password_button.is_enabled(), 'Кнопка Сброс пароля активна'

    def test_check_placeholder_in_enter_password_field(self, browser, login):
        language = login
        password = ResetPasswordPage(browser)
        password.click_forgot_password_button(language)
        placeholder = password.get_placeholder_from_enter_password_field(language)
        if language == 'en':
            excepted_placeholder = data.PLACEHOLDER_PASSWORD_FIELD_EN
        elif language == 'ru':
            excepted_placeholder = data.PLACEHOLDER_PASSWORD_FIELD_RU
        elif language == 'pt':
            excepted_placeholder = data.PLACEHOLDER_PASSWORD_FIELD_PT
        assert placeholder == excepted_placeholder, f'Актуальный плейсхолдер {placeholder} не соответствует ожидаемому {excepted_placeholder}'

    def test_check_error_message_with_empty_enter_password_field(self, browser, login):
        language = login
        password = ResetPasswordPage(browser)
        password.click_forgot_password_button(language)

