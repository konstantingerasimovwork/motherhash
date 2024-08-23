import allure
import data
from authorization.pages.signin_password_page import SignInPasswordPage


@allure.suite('SignIn Password')
class TestSignInPassword():

    @allure.sub_suite('1. Проверка наличия заголовка Welcome / Добро пожаловать / Bem-vindo')
    def test_check_welcome_title(self, browser, login):
        allure.dynamic.title(
            f'{login}  - Проверка ввода пароля для зарегистрированного в базе пользователя в поле ввода')
        language = login
        password = SignInPasswordPage(browser)
        result = password.find_welcome_title(language)
        assert result, f'Заголовок не найден'
    
    @allure.sub_suite('2. Проверка наличия email, введённого ранее на странице входа')
    def test_check_email_text_on_welcome_page(self, browser, login):
        allure.dynamic.title(
            f'{login}  - Проверка наличия email, введённого ранее на странице входа')
        password = SignInPasswordPage(browser)
        email = password.get_email_signin_password_page()
        excepted_email = data.EXISTING_EMAIL
        assert email == excepted_email, f'Email {email} не соответствует ожидаемому {excepted_email}'

    @allure.sub_suite('3. Проверка наличия ссылки Change email/Alterar email/Изменить электронную почту')
    def test_check_change_email_link_on_welcome_page(self, browser, login):
        allure.dynamic.title(
            f'{login}  - Проверка наличия ссылки Change email/Alterar email/Изменить электронную почту')
        language = login
        password = SignInPasswordPage(browser)
        assert password.find_change_email_link(
            language), f'Не нашлась ссылка {language}'

    @allure.sub_suite('4. Проверка перехода по ссылке Change email/Alterar email/Изменить электронную почту')
    def test_click_change_email_link_on_welcome_page(self, browser, login):
        allure.dynamic.title(
            f'{login}  - Проверка перехода по ссылке Change email/Alterar email/Изменить электронную почту')
        language = login
        password = SignInPasswordPage(browser)
        current_url = password.ckick_change_email_link_and_get_current_url(
            language)
        assert current_url == data.URL_SIGNIN, f'Актуальный url {current_url} не равен ожидаемому {data.URL_SIGNIN}'

    @allure.sub_suite('5. Проверка ввода пароля для зарегистрированного в базе пользователя в поле ввода')
    def test_enter_registered_password(self, browser, login):
        allure.dynamic.title(
            f'{login}  - Проверка ввода пароля для зарегистрированного в базе пользователя в поле ввода')
        language = login
        password = SignInPasswordPage(browser)
        password.find_password_field_and_type_text(data.EXISTING_PASSWORD)
        password.click_enter_button(language)
        password.wait_lk_url_to_be(data.URL_LK_DASHBOARD)
        current_url = password.get_lk_page_url()
        assert current_url == data.URL_LK_DASHBOARD, f'Актуальный адрес страницы ЛК {current_url} не равен ожидаемому {data.URL_LK_DASHBOARD}'

    @allure.sub_suite('6. Проверка ввода пароля, отличного от указанного при успешной регистрации в поле ввода')
    def test_enter_unregistered_password(self, browser, login):
        allure.dynamic.title(
            f'{login}  - Проверка ввода пароля, отличного от указанного при успешной регистрации в поле ввода')
        language = login
        password = SignInPasswordPage(browser)
        password.find_password_field_and_type_text(data.NONEXISTING_PASSWORD)
        password.click_enter_button(language)
        assert password.find_error_message(language), f'Текст ошибки не найден'

    @allure.sub_suite('7. Проверка: Оставить поле пустым')
    def test_empty_password_field(self, browser, login):
        allure.dynamic.title(
            f'{login}  - Проверка: Оставить поле пустым')
        language = login
        password = SignInPasswordPage(browser)
        button = password.find_enter_button(language)
        assert not button.is_enabled()
