import allure
import pytest
import data
from authorization.pages.signin_page import SignInPage
from authorization.locators.signin_page_locators import SignInPageLocators as signin
from helpers import fake_email


class TestSignInEmail():

    @pytest.mark.parametrize('language', ['en', 'ru', 'pt'])
    @allure.title('Проверка ввода зарегистрированного в базе email в поле ввода - {language}')
    def test_enter_registered_email_en(self, browser, language):
        signin_page = SignInPage(browser)
        browser.get(data.URL_SIGNIN)
        signin_page.change_language(language)
        signin_page.find_email_field_and_type_text(data.EXISTING_EMAIL)
        signin_page.click_continue_button(language)
        signin_page.wait_password_url_to_be(data.URL_SIGNIN_PASSWORD)
        current_url = signin_page.get_welcome_page_url()
        result = signin_page.find_welcome_title_en()
        assert current_url == data.URL_SIGNIN_PASSWORD and result, f'{current_url} не равен {data.URL_SIGNIN_PASSWORD} или не найден заголовок'

    @pytest.mark.parametrize('language', ['en', 'ru', 'pt'])
    @allure.title('Проверка ввода незарегистрированного в базе email в поле ввода - {language}')
    def test_enter_unregistered_email_en(self, browser, language):
        signin_page = SignInPage(browser)
        browser.get(data.URL_SIGNIN)
        signin_page.change_language(language)
        signin_page.find_email_field_and_type_text(fake_email)
        signin_page.click_continue_button(language)
        signin_page.wait_signup_url_to_be(data.URL_SIGNUP)
        current_url = signin_page.get_signup_page_url()
        result = signin_page.find_create_account_title_en()
        assert current_url == data.URL_SIGNUP and result, f'{current_url} не равен {data.URL_SIGNUP} или не найден заголовок'

    # 1. Только цифры в локальном имени
    # 2. Кириллица в локальном имени
    # 3. Только цифры в доменном имени
    # 4. Цифры после букв в локальном имени
    # 5. Цифры до букв в локальном имени
    # 6. Спецсимволы в локальном имени
    # 7. Цифры после букв в доменном имени
    # 8. Цифры до букв в доменном имени
    # 9. Дефис в середине доменного имени
    # 10. Кириллица в доменном имени
    @pytest.mark.parametrize('email,', ['123@example.com', 'имэйл@example.com',
                                       'email@123.com', 'email123@example.com',
                                       '123email@example.com', 'em!#ail@example.com',
                                       'email@example123.com', 'email@123example.com',
                                       'email@exa-mple.com', 'email@эксемпл.com'])
    @allure.title('Позитивные проверки для набора значений - {email}')
    def test_valid_email_set_of_values(self, browser, email):
        signin_page = SignInPage(browser)
        browser.get(data.URL_SIGNIN)
        signin_page.find_email_field_and_type_text(email)
        signin_page.click_continue_button('en')
        signin_page.wait_signup_url_to_be(data.URL_SIGNUP)
        current_url = signin_page.get_signup_page_url()
        result = signin_page.find_create_account_title_en()
        assert current_url == data.URL_SIGNUP and result, f'{current_url} не равен {data.URL_SIGNUP} или не найден заголовок'

    # 1. Длинна локального имени 1 символ
    # 2. Длинна локального имени 2 символа
    # 3. Длинна локального имени 63 символа
    # 4. Длинна локального имени 64 символа
    # 5. Длина доменного имени 1 символ
    # 6. Длина доменного имени 2 символа
    # 7. Длина доменного имени 62 символа
    # 8. Длина доменного имени 63 символа
    @pytest.mark.parametrize('email', ['e@example.com', 'em@example.com',
                                       'emailemailemailemailemailemailemailemailemailemailemailemailema@example.com',
                                       'emailemailemailemailemailemailemailemailemailemailemailemailemai@example.com',
                                       'email@e.com', 'email@em.com', 
                                       'email@exampleexampleexampleexampleexampleexampleexampleexampleexampl.com',
                                       'email@exampleexampleexampleexampleexampleexampleexampleexampleexample.com'])
    @allure.title('Позитивные проверки для диапазона - {email}')
    def test_valid_email_range(self, browser, email):
        signin_page = SignInPage(browser)
        browser.get(data.URL_SIGNIN)
        signin_page.find_email_field_and_type_text(email)
        signin_page.click_continue_button('en')
        signin_page.wait_signup_url_to_be(data.URL_SIGNUP)
        current_url = signin_page.get_signup_page_url()
        result = signin_page.find_create_account_title_en()
        assert current_url == data.URL_SIGNUP and result, f'{current_url} не равен {data.URL_SIGNUP} или не найден заголовок'

    @pytest.mark.parametrize('language, expected_error_message', [('en', data.REQUIRED_FIELD_MESSAGE_EN),
                                                                  ('ru', data.REQUIRED_FIELD_MESSAGE_RU), 
                                                                  ('pt', data.REQUIRED_FIELD_MESSAGE_PT)])
    @allure.title('Негативные проверки - {language}: Пустое поле')
    def test_empty_email_field_en(self, browser, language, expected_error_message):
        signin_page = SignInPage(browser)
        browser.get(data.URL_SIGNIN)
        signin_page.change_language(language)
        signin_page.click_continue_button(language)
        error_message = signin_page.find_and_get_error_message()
        assert error_message == expected_error_message, f'Сообщение об ошибке {error_message} не равно {expected_error_message}'

    # 1. Отсутствие знака @
    # 2. Несколько @@
    # 3. Пробел в середине строки
    # 4. Отсутствие локального имени
    # 5. Точка в начале локального имени
    # 6. Точка в конце локального имени
    # 7. Отсутствие доменного имени
    # 8. Дефис в начале доменного имени
    # 9. Дефис в конце доменного имени
    @pytest.mark.parametrize('email', ['emailexample.com',
                                       'email@email@example.com',
                                       'email @example.com',
                                       '@example.com',
                                       '.email@example.com',
                                       'email.@example.com',
                                       'email@',
                                       'email@ -example.com',
                                       'email@example-.com'])
    @allure.title('Негативные проверки для набора значений - EN - {email}')
    def test_invalid_email_set_of_values_en(self, browser, email):
        signin_page = SignInPage(browser)
        browser.get(data.URL_SIGNIN)
        signin_page.change_language('en')
        signin_page.find_email_field_and_type_text(email)
        signin_page.click_continue_button('en')
        error_message = signin_page.find_and_get_error_message()
        assert error_message == data.INCORRECT_FORMAT_MESSAGE_EN, f'Сообщение об ошибке {error_message} не равно {data.INCORRECT_FORMAT_MESSAGE_EN}'

    # 1. Отсутствие знака @
    # 2. Несколько @@
    # 3. Пробел в середине строки
    # 4. Отсутствие локального имени
    # 5. Точка в начале локального имени
    # 6. Точка в конце локального имени
    # 7. Отсутствие доменного имени
    # 8. Дефис в начале доменного имени
    # 9. Дефис в конце доменного имени
    @pytest.mark.parametrize('email', ['emailexample.com',
                                       'email@email@example.com',
                                       'email @example.com',
                                       '@example.com',
                                       '.email@example.com',
                                       'email.@example.com',
                                       'email@',
                                       'email@ -example.com',
                                       'email@example-.com'])
    @allure.title('Негативные проверки для набора значений - RU - {email}')
    def test_invalid_email_set_of_values_ru(self, browser, email):
        signin_page = SignInPage(browser)
        browser.get(data.URL_SIGNIN)
        signin_page.change_language('ru')
        signin_page.find_email_field_and_type_text(email)
        signin_page.click_continue_button('ru')
        error_message = signin_page.find_and_get_error_message()
        assert error_message == data.INCORRECT_FORMAT_MESSAGE_RU, f'Сообщение об ошибке {error_message} не равно {data.INCORRECT_FORMAT_MESSAGE_RU}'

    # 1. Отсутствие знака @
    # 2. Несколько @@
    # 3. Пробел в середине строки
    # 4. Отсутствие локального имени
    # 5. Точка в начале локального имени
    # 6. Точка в конце локального имени
    # 7. Отсутствие доменного имени
    # 8. Дефис в начале доменного имени
    # 9. Дефис в конце доменного имени
    @pytest.mark.parametrize('email', ['emailexample.com',
                                       'email@email@example.com',
                                       'email @example.com',
                                       '@example.com',
                                       '.email@example.com',
                                       'email.@example.com',
                                       'email@',
                                       'email@ -example.com',
                                       'email@example-.com'])
    @allure.title('Негативные проверки для набора значений - PT - {email}')
    def test_invalid_email_set_of_values_pt(self, browser, email):
        signin_page = SignInPage(browser)
        browser.get(data.URL_SIGNIN)
        signin_page.change_language('pt')
        signin_page.find_email_field_and_type_text(email)
        signin_page.click_continue_button('pt')
        error_message = signin_page.find_and_get_error_message()
        assert error_message == data.INCORRECT_FORMAT_MESSAGE_PT, f'Сообщение об ошибке {error_message} не равно {data.INCORRECT_FORMAT_MESSAGE_PT}'

    # 1. Длинна локального имени 65 символов
    # 2. Длинна локального имени 66 символов
    # 3. Длина доменного имени 64 символа
    # 4. Длина доменного имени 65 символов
    @pytest.mark.parametrize('email', ['emailemailemailemailemailemailemailemailemailemailemailemailemail@example.com',
                                       'emailemailemailemailemailemailemailemailemailemailemailemailemaile@example.com',
                                       'email@exampleexampleexampleexampleexampleexampleexampleexampleexamplee.com',
                                       'email@exampleexampleexampleexampleexampleexampleexampleexampleexampleex.com'])
    @allure.title('Негативные проверки для диапазона - EN - {email}')
    def test_invalid_email_range_en(self, browser, email):
        signin_page = SignInPage(browser)
        browser.get(data.URL_SIGNIN)
        signin_page.change_language('en')
        signin_page.find_email_field_and_type_text(email)
        signin_page.click_continue_button('en')
        error_message = signin_page.find_and_get_error_message()
        assert error_message == data.INCORRECT_FORMAT_MESSAGE_EN, f'Сообщение об ошибке {error_message} не равно {data.INCORRECT_FORMAT_MESSAGE_EN}'

    # 1. Длинна локального имени 65 символов
    # 2. Длинна локального имени 66 символов
    # 3. Длина доменного имени 64 символа
    # 4. Длина доменного имени 65 символов
    @pytest.mark.parametrize('email', ['emailemailemailemailemailemailemailemailemailemailemailemailemail@example.com',
                                       'emailemailemailemailemailemailemailemailemailemailemailemailemaile@example.com',
                                       'email@exampleexampleexampleexampleexampleexampleexampleexampleexamplee.com',
                                       'email@exampleexampleexampleexampleexampleexampleexampleexampleexampleex.com'])
    @allure.title('Негативные проверки для диапазона - RU - {email}')
    def test_invalid_email_range_ru(self, browser, email):
        signin_page = SignInPage(browser)
        browser.get(data.URL_SIGNIN)
        signin_page.change_language('ru')
        signin_page.find_email_field_and_type_text(email)
        signin_page.click_continue_button('ru')
        error_message = signin_page.find_and_get_error_message()
        assert error_message == data.INCORRECT_FORMAT_MESSAGE_RU, f'Сообщение об ошибке {error_message} не равно {data.INCORRECT_FORMAT_MESSAGE_RU}'

    # 1. Длинна локального имени 65 символов
    # 2. Длинна локального имени 66 символов
    # 3. Длина доменного имени 64 символа
    # 4. Длина доменного имени 65 символов
    @pytest.mark.parametrize('email', ['emailemailemailemailemailemailemailemailemailemailemailemailemail@example.com',
                                       'emailemailemailemailemailemailemailemailemailemailemailemailemaile@example.com',
                                       'email@exampleexampleexampleexampleexampleexampleexampleexampleexamplee.com',
                                       'email@exampleexampleexampleexampleexampleexampleexampleexampleexampleex.com'])
    @allure.title('Негативные проверки для диапазона - PT - {email}')
    def test_invalid_email_range_pt(self, browser, email):
        signin_page = SignInPage(browser)
        browser.get(data.URL_SIGNIN)
        signin_page.change_language('pt')
        signin_page.find_email_field_and_type_text(email)
        signin_page.click_continue_button('pt')
        error_message = signin_page.find_and_get_error_message()
        assert error_message == data.INCORRECT_FORMAT_MESSAGE_PT, f'Сообщение об ошибке {error_message} не равно {data.INCORRECT_FORMAT_MESSAGE_PT}'
