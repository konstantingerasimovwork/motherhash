import allure
import pytest
import data
from authorization.pages.signin_page import SignInPage
from helpers import fake_email


@allure.suite('SignIn Email')
class TestSignInEmail():

    @allure.sub_suite('1. Проверка ввода зарегистрированного в базе email в поле ввода')
    @pytest.mark.parametrize('language', ['en', 'ru', 'pt'])
    def test_enter_registered_email(self, browser, language):
        allure.dynamic.title(
            f'{language}  - Проверка ввода зарегистрированного в базе email в поле ввода')
        signin_page = SignInPage(browser)
        browser.get(data.URL_SIGNIN)
        signin_page.change_language(language)
        signin_page.find_email_field_and_type_text(data.EXISTING_EMAIL)
        signin_page.click_continue_button(language)
        signin_page.wait_password_url_to_be(data.URL_SIGNIN_PASSWORD)
        current_url = signin_page.get_welcome_page_url()
        result = signin_page.find_welcome_title(language)
        assert current_url == data.URL_SIGNIN_PASSWORD and result, f'{current_url} не равен {data.URL_SIGNIN_PASSWORD} или не найден заголовок'

    @allure.sub_suite('2. Проверка ввода незарегистрированного в базе email в поле ввода')
    @pytest.mark.parametrize('language', ['en', 'ru', 'pt'])
    def test_enter_unregistered_email(self, browser, language):
        allure.dynamic.title(
            f'{language}  - Проверка ввода незарегистрированного в базе email в поле ввода')
        signin_page = SignInPage(browser)
        browser.get(data.URL_SIGNIN)
        signin_page.change_language(language)
        email = fake_email()
        signin_page.find_email_field_and_type_text(email)
        signin_page.click_continue_button(language)
        signin_page.wait_signup_url_to_be(data.URL_SIGNUP)
        current_url = signin_page.get_signup_page_url()
        result = signin_page.find_create_account_title(language)
        assert current_url == data.URL_SIGNUP and result, f'{current_url} не равен {data.URL_SIGNUP} или не найден заголовок'

    @allure.sub_suite('3. Позитивные проверки для набора значений')
    @pytest.mark.parametrize('email, description', [('123@example.com', 'Только цифры в локальном имени'),
                                                    ('имэйл@example.com', 'Кириллица в локальном имени'),
                                                    ('email@123.com', 'Только цифры в доменном имени'),
                                                    ('email123@example.com', 'Цифры после букв в локальном имени'),
                                                    ('123email@example.com', 'Цифры до букв в локальном имени'),
                                                    ('em!#ail@example.com', 'Спецсимволы в локальном имени'),
                                                    ('email@example123.com', 'Цифры после букв в доменном имени'),
                                                    ('email@123example.com', 'Цифры до букв в доменном имени'),
                                                    ('email@exa-mple.com', 'Дефис в середине доменного имени'),
                                                    ('email@эксемпл.com', 'Кириллица в доменном имени')])
    @allure.title('Позитивные проверки для набора значений - {email}')
    def test_valid_email_set_of_values(self, browser, email, description):
        allure.dynamic.title(
            f'Проверка ввода незарегистрированного в базе email в поле ввода - {description}')
        signin_page = SignInPage(browser)
        browser.get(data.URL_SIGNIN)
        signin_page.find_email_field_and_type_text(email)
        signin_page.click_continue_button('en')
        signin_page.wait_signup_url_to_be(data.URL_SIGNUP)
        current_url = signin_page.get_signup_page_url()
        result = signin_page.find_create_account_title('en')
        assert current_url == data.URL_SIGNUP and result, f'{current_url} не равен {data.URL_SIGNUP} или не найден заголовок'

    @allure.sub_suite('4. Позитивные проверки для диапазона')
    @pytest.mark.parametrize('email, description', [('e@example.com', 'Длинна локального имени 1 символ'),
                                                    ('em@example.com', 'Длинна локального имени 2 символа'),
                                                    ('emailemailemailemailemailemailemailemailemailemailemailemailema@example.com', 'Длинна локального имени 63 символа'),
                                                    ('emailemailemailemailemailemailemailemailemailemailemailemailemai@example.com', 'Длинна локального имени 64 символа'),
                                                    ('email@e.com', 'Длина доменного имени 1 символ'),
                                                    ('email@em.com', 'Длина доменного имени 2 символа'),
                                                    ('email@exampleexampleexampleexampleexampleexampleexampleexampleexampl.com', 'Длина доменного имени 62 символа'),
                                                    ('email@exampleexampleexampleexampleexampleexampleexampleexampleexample.com', 'Длина доменного имени 63 символа')])
    def test_valid_email_range(self, browser, email, description):
        allure.dynamic.title(
            f'Проверка ввода незарегистрированного в базе email в поле ввода - {description}')
        signin_page = SignInPage(browser)
        browser.get(data.URL_SIGNIN)
        signin_page.find_email_field_and_type_text(email)
        signin_page.click_continue_button('en')
        signin_page.wait_signup_url_to_be(data.URL_SIGNUP)
        current_url = signin_page.get_signup_page_url()
        result = signin_page.find_create_account_title('en')
        assert current_url == data.URL_SIGNUP and result, f'{current_url} не равен {data.URL_SIGNUP} или не найден заголовок'

    @allure.sub_suite('5. Негативные проверки: Пустое поле')
    @pytest.mark.parametrize('language, expected_error_message', [('en', data.REQUIRED_FIELD_MESSAGE_EN),
                                                                  ('ru', data.REQUIRED_FIELD_MESSAGE_RU), 
                                                                  ('pt', data.REQUIRED_FIELD_MESSAGE_PT)])
    def test_empty_email_field_en(self, browser, language, expected_error_message):
        allure.dynamic.title(
            f'{language}  - Негативные проверки: Пустое поле')
        signin_page = SignInPage(browser)
        browser.get(data.URL_SIGNIN)
        signin_page.change_language(language)
        signin_page.click_continue_button(language)
        error_message = signin_page.find_and_get_error_message()
        assert error_message == expected_error_message, f'Сообщение об ошибке {error_message} не равно {expected_error_message}'

    @allure.sub_suite('6. EN - Негативные проверки для набора значений')
    @pytest.mark.parametrize('email, description', [('emailexample.com', 'Отсутствие знака @'),
                                                    ('email@email@example.com', 'Несколько @@'),
                                                    ('email @example.com', 'Пробел в середине строки'),
                                                    ('@example.com', 'Отсутствие локального имени'),
                                                    ('.email@example.com', 'Точка в начале локального имени'),
                                                    ('email.@example.com', 'Точка в конце локального имени'),
                                                    ('email@', 'Отсутствие доменного имени'),
                                                    ('email@ -example.com', 'Дефис в начале доменного имени'),
                                                    ('email@example-.com', 'Дефис в конце доменного имени')])
    def test_invalid_email_set_of_values_en(self, browser, email, description):
        allure.dynamic.title(
            f'EN - Негативные проверки для набора значений - {description}')
        signin_page = SignInPage(browser)
        browser.get(data.URL_SIGNIN)
        signin_page.change_language('en')
        signin_page.find_email_field_and_type_text(email)
        signin_page.click_continue_button('en')
        error_message = signin_page.find_and_get_error_message()
        assert error_message == data.INCORRECT_FORMAT_MESSAGE_EN, f'Сообщение об ошибке {error_message} не равно {data.INCORRECT_FORMAT_MESSAGE_EN}'

    @allure.sub_suite('7. RU - Негативные проверки для набора значений')
    @pytest.mark.parametrize('email, description', [('emailexample.com', 'Отсутствие знака @'),
                                                    ('email@email@example.com', 'Несколько @@'),
                                                    ('email @example.com', 'Пробел в середине строки'),
                                                    ('@example.com', 'Отсутствие локального имени'),
                                                    ('.email@example.com', 'Точка в начале локального имени'),
                                                    ('email.@example.com', 'Точка в конце локального имени'),
                                                    ('email@', 'Отсутствие доменного имени'),
                                                    ('email@ -example.com', 'Дефис в начале доменного имени'),
                                                    ('email@example-.com', 'Дефис в конце доменного имени')])
    def test_invalid_email_set_of_values_ru(self, browser, email, description):
        allure.dynamic.title(
            f'RU - Негативные проверки для набора значений - {description}')
        signin_page = SignInPage(browser)
        browser.get(data.URL_SIGNIN)
        signin_page.change_language('ru')
        signin_page.find_email_field_and_type_text(email)
        signin_page.click_continue_button('ru')
        error_message = signin_page.find_and_get_error_message()
        assert error_message == data.INCORRECT_FORMAT_MESSAGE_RU, f'Сообщение об ошибке {error_message} не равно {data.INCORRECT_FORMAT_MESSAGE_RU}'

    @allure.sub_suite('8. PT - Негативные проверки для набора значений')
    @pytest.mark.parametrize('email, description', [('emailexample.com', 'Отсутствие знака @'),
                                                    ('email@email@example.com', 'Несколько @@'),
                                                    ('email @example.com', 'Пробел в середине строки'),
                                                    ('@example.com', 'Отсутствие локального имени'),
                                                    ('.email@example.com', 'Точка в начале локального имени'),
                                                    ('email.@example.com', 'Точка в конце локального имени'),
                                                    ('email@', 'Отсутствие доменного имени'),
                                                    ('email@ -example.com', 'Дефис в начале доменного имени'),
                                                    ('email@example-.com', 'Дефис в конце доменного имени')])
    def test_invalid_email_set_of_values_pt(self, browser, email, description):
        allure.dynamic.title(
            f'PT - Негативные проверки для набора значений - {description}')
        signin_page = SignInPage(browser)
        browser.get(data.URL_SIGNIN)
        signin_page.change_language('pt')
        signin_page.find_email_field_and_type_text(email)
        signin_page.click_continue_button('pt')
        error_message = signin_page.find_and_get_error_message()
        assert error_message == data.INCORRECT_FORMAT_MESSAGE_PT, f'Сообщение об ошибке {error_message} не равно {data.INCORRECT_FORMAT_MESSAGE_PT}'

    @allure.sub_suite('9. EN - Негативные проверки для диапазона')
    @pytest.mark.parametrize('email, description', [('emailemailemailemailemailemailemailemailemailemailemailemailemail@example.com', 'Длинна локального имени 65 символов'),
                                       ('emailemailemailemailemailemailemailemailemailemailemailemailemaile@example.com', 'Длинна локального имени 66 символов'),
                                       ('email@exampleexampleexampleexampleexampleexampleexampleexampleexamplee.com', 'Длина доменного имени 64 символа'),
                                       ('email@exampleexampleexampleexampleexampleexampleexampleexampleexampleex.com', 'Длина доменного имени 65 символов')])
    def test_invalid_email_range_en(self, browser, email, description):
        allure.dynamic.title(
            f'EN - Негативные проверки для диапазона - {description}')
        signin_page = SignInPage(browser)
        browser.get(data.URL_SIGNIN)
        signin_page.change_language('en')
        signin_page.find_email_field_and_type_text(email)
        signin_page.click_continue_button('en')
        error_message = signin_page.find_and_get_error_message()
        assert error_message == data.INCORRECT_FORMAT_MESSAGE_EN, f'Сообщение об ошибке {error_message} не равно {data.INCORRECT_FORMAT_MESSAGE_EN}'

    @allure.sub_suite('10. RU - Негативные проверки для диапазона')
    @pytest.mark.parametrize('email, description', [('emailemailemailemailemailemailemailemailemailemailemailemailemail@example.com', 'Длинна локального имени 65 символов'),
                                       ('emailemailemailemailemailemailemailemailemailemailemailemailemaile@example.com', 'Длинна локального имени 66 символов'),
                                       ('email@exampleexampleexampleexampleexampleexampleexampleexampleexamplee.com', 'Длина доменного имени 64 символа'),
                                       ('email@exampleexampleexampleexampleexampleexampleexampleexampleexampleex.com', 'Длина доменного имени 65 символов')])
    def test_invalid_email_range_ru(self, browser, email, description):
        allure.dynamic.title(
            f'RU - Негативные проверки для диапазона - {description}')
        signin_page = SignInPage(browser)
        browser.get(data.URL_SIGNIN)
        signin_page.change_language('ru')
        signin_page.find_email_field_and_type_text(email)
        signin_page.click_continue_button('ru')
        error_message = signin_page.find_and_get_error_message()
        assert error_message == data.INCORRECT_FORMAT_MESSAGE_RU, f'Сообщение об ошибке {error_message} не равно {data.INCORRECT_FORMAT_MESSAGE_RU}'

    @allure.sub_suite('11. PT - Негативные проверки для диапазона')
    @pytest.mark.parametrize('email, description', [('emailemailemailemailemailemailemailemailemailemailemailemailemail@example.com', 'Длинна локального имени 65 символов'),
                                       ('emailemailemailemailemailemailemailemailemailemailemailemailemaile@example.com', 'Длинна локального имени 66 символов'),
                                       ('email@exampleexampleexampleexampleexampleexampleexampleexampleexamplee.com', 'Длина доменного имени 64 символа'),
                                       ('email@exampleexampleexampleexampleexampleexampleexampleexampleexampleex.com', 'Длина доменного имени 65 символов')])
    def test_invalid_email_range_pt(self, browser, email, description):
        allure.dynamic.title(
            f' PT - Негативные проверки для диапазона - {description}')
        signin_page = SignInPage(browser)
        browser.get(data.URL_SIGNIN)
        signin_page.change_language('pt')
        signin_page.find_email_field_and_type_text(email)
        signin_page.click_continue_button('pt')
        error_message = signin_page.find_and_get_error_message()
        assert error_message == data.INCORRECT_FORMAT_MESSAGE_PT, f'Сообщение об ошибке {error_message} не равно {data.INCORRECT_FORMAT_MESSAGE_PT}'
