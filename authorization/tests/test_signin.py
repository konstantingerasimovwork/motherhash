import time
import pytest
import data
from authorization.pages.signin_page import SignInPage
from authorization.locators.signin_page_locators import SignInPageLocators as signin
from helpers import fake_email


class TestSignIn():

    # Проверка ввода зарегистрированного в базе email в поле ввода
    @pytest.mark.parametrize('language, continue_button, title', [(signin.LANGUAGE_EN, signin.CONTINUE_BUTTON_EN, signin.WELCOME_TITLE_EN),
                                                                  (signin.LANGUAGE_RU, signin.CONTINUE_BUTTON_RU, signin.WELCOME_TITLE_RU),
                                                                  (signin.LANGUAGE_PT, signin.CONTINUE_BUTTON_PT, signin.WELCOME_TITLE_PT)])
    def test_enter_registered_email(self, browser, language, continue_button, title):
        signin_page = SignInPage(browser)
        browser.get(data.URL_SIGNIN)
        signin_page.change_language(language)
        signin_page.find_email_field_and_type_text(data.EXISTING_EMAIL)
        signin_page.click_continue_button(continue_button)
        signin_page.wait_password_url_to_be(data.URL_SIGNIN_PASSWORD)
        current_url = signin_page.get_welcome_page_url()
        result = signin_page.find_welcome_title(title)
        assert current_url == data.URL_SIGNIN_PASSWORD and result, f'{current_url} не равен {data.URL_SIGNIN_PASSWORD} или не найден заголовок'

    # Проверка ввода незарегистрированного в базе email в поле ввода
    @pytest.mark.parametrize('language, continue_button, title', [(signin.LANGUAGE_EN, signin.CONTINUE_BUTTON_EN, signin.CREATE_ACCOUNT_TITLE_EN),
                                                                  (signin.LANGUAGE_RU, signin.CONTINUE_BUTTON_RU, signin.CREATE_ACCOUNT_TITLE_RU),
                                                                  (signin.LANGUAGE_PT, signin.CONTINUE_BUTTON_PT, signin.CREATE_ACCOUNT_TITLE_PT)])
    def test_enter_unregistered_email(self, browser, language, continue_button, title):
        signin_page = SignInPage(browser)
        browser.get(data.URL_SIGNIN)
        signin_page.change_language(language)
        signin_page.find_email_field_and_type_text(fake_email)
        signin_page.click_continue_button(continue_button)
        signin_page.wait_signup_url_to_be(data.URL_SIGNUP)
        current_url = signin_page.get_signup_page_url()
        result = signin_page.find_welcome_title(title)
        assert current_url == data.URL_SIGNUP and result, f'{current_url} не равен {data.URL_SIGNUP} или не найден заголовок'

    # Позитивные проверки для набора значений:
    # 1. Только цифры в локальном имени
    # 2. Цифры после букв в локальном имени
    # 3. Цифры до букв в локальном имени
    # 4. Спецсимволы в локальном имени
    # 5. Цифры после букв в доменном имени
    # 6. Цифры до букв в доменном имени
    # 7. Дефис в середине доменного имени
    # 8. Кириллица в доменном имени
    @pytest.mark.parametrize('email, continue_button, title', [('123@example.com', signin.CONTINUE_BUTTON_EN, signin.WELCOME_TITLE_EN),
                                                               ('email123@example.com', signin.CONTINUE_BUTTON_EN, signin.WELCOME_TITLE_EN),
                                                               ('123email@example.com', signin.CONTINUE_BUTTON_EN, signin.WELCOME_TITLE_EN),
                                                               ('em!#ail@example.com', signin.CONTINUE_BUTTON_EN, signin.WELCOME_TITLE_EN),
                                                               ('email@example123.com', signin.CONTINUE_BUTTON_EN, signin.WELCOME_TITLE_EN),
                                                               ('email@123example.com', signin.CONTINUE_BUTTON_EN, signin.WELCOME_TITLE_EN),
                                                               ('email@exa-mple.com', signin.CONTINUE_BUTTON_EN, signin.WELCOME_TITLE_EN),
                                                               ('email@эксемпл.com', signin.CONTINUE_BUTTON_EN, signin.WELCOME_TITLE_EN)])
    def test_valid_email_set_of_values(self, browser, email, continue_button, title):
        signin_page = SignInPage(browser)
        browser.get(data.URL_SIGNIN)
        signin_page.find_email_field_and_type_text(email)
        signin_page.click_continue_button(continue_button)
        signin_page.wait_signup_url_to_be(data.URL_SIGNUP)
        current_url = signin_page.get_signup_page_url()
        result = signin_page.find_welcome_title(title)
        assert current_url == data.URL_SIGNUP and result, f'{current_url} не равен {data.URL_SIGNUP} или не найден заголовок'

    # Позитивные проверки для диапазона:
    # 1. Длинна локального имени 1 символ
    # 2. Длинна локального имени 2 символа
    # 3. Длинна локального имени 63 символа
    # 4. Длинна локального имени 64 символа
    # 5. Длина доменного имени 1 символ
    # 6. Длина доменного имени 2 символа
    # 7. Длина доменного имени 62 символа
    # 8. Длина доменного имени 63 символа
    @pytest.mark.parametrize('email, continue_button, title', [('e@example.com', signin.CONTINUE_BUTTON_EN, signin.WELCOME_TITLE_EN),
                                                               ('em@example.com', signin.CONTINUE_BUTTON_EN, signin.WELCOME_TITLE_EN),
                                                               ('emailemailemailemailemailemailemailemailemailemailemailemailema@example.com',
                                                                signin.CONTINUE_BUTTON_EN, signin.WELCOME_TITLE_EN),
                                                               ('emailemailemailemailemailemailemailemailemailemailemailemailemai@example.com', 
                                                                signin.CONTINUE_BUTTON_EN, signin.WELCOME_TITLE_EN),
                                                               ('email@e.com', signin.CONTINUE_BUTTON_EN,
                                                                signin.WELCOME_TITLE_EN),
                                                               ('email@em.com', signin.CONTINUE_BUTTON_EN,
                                                                signin.WELCOME_TITLE_EN),
                                                               ('email@exampleexampleexampleexampleexampleexampleexampleexampleexampl.com',
                                                                signin.CONTINUE_BUTTON_EN, signin.WELCOME_TITLE_EN),
                                                               ('email@exampleexampleexampleexampleexampleexampleexampleexampleexample.com', 
                                                                signin.CONTINUE_BUTTON_EN, signin.WELCOME_TITLE_EN),])
    def test_valid_email_range(self, browser, email, continue_button, title):
        signin_page = SignInPage(browser)
        browser.get(data.URL_SIGNIN)
        signin_page.find_email_field_and_type_text(email)
        signin_page.click_continue_button(continue_button)
        signin_page.wait_signup_url_to_be(data.URL_SIGNUP)
        current_url = signin_page.get_signup_page_url()
        result = signin_page.find_welcome_title(title)
        assert current_url == data.URL_SIGNUP and result, f'{current_url} не равен {data.URL_SIGNUP} или не найден заголовок'

    # # Позитивные проверки для набора значений:
    # # 1. Только цифры в локальном имени
    # # 2. Цифры после букв в локальном имени
    # # 3. Цифры до букв в локальном имени
    # # 4. Спецсимволы в локальном имени
    # # 5. Цифры после букв в доменном имени
    # # 6. Цифры до букв в доменном имени
    # # 7. Дефис в середине доменного имени
    # # 8. Кириллица в доменном имени
    # @pytest.mark.parametrize('email, continue_button, title', [('123@example.com', signin.CONTINUE_BUTTON_EN, signin.WELCOME_TITLE_EN),
    #                                                            ('email123@example.com', signin.CONTINUE_BUTTON_EN, signin.WELCOME_TITLE_EN),
    #                                                            ('123email@example.com', signin.CONTINUE_BUTTON_EN, signin.WELCOME_TITLE_EN),
    #                                                            ('em!#ail@example.com', signin.CONTINUE_BUTTON_EN, signin.WELCOME_TITLE_EN),
    #                                                            ('email@example123.com', signin.CONTINUE_BUTTON_EN, signin.WELCOME_TITLE_EN),
    #                                                            ('email@123example.com', signin.CONTINUE_BUTTON_EN, signin.WELCOME_TITLE_EN),
    #                                                            ('email@exa-mple.com', signin.CONTINUE_BUTTON_EN, signin.WELCOME_TITLE_EN),
    #                                                            ('email@эксемпл.com', signin.CONTINUE_BUTTON_EN, signin.WELCOME_TITLE_EN)])
    # def test_valid_email_set_of_values(self, browser, email, continue_button, title):
    #     signin_page = SignInPage(browser)
    #     browser.get(data.URL_SIGNIN)
    #     signin_page.find_email_field_and_type_text(email)
    #     signin_page.click_continue_button(continue_button)
    #     signin_page.wait_signup_url_to_be(data.URL_SIGNUP)
    #     current_url = signin_page.get_signup_page_url()
    #     result = signin_page.find_welcome_title(title)
    #     assert current_url == data.URL_SIGNUP and result, f'{current_url} не равен {data.URL_SIGNUP} или не найден заголовок'