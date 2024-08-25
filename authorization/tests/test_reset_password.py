import allure
import pytest
import data
from authorization.pages.reset_password_page import ResetPasswordPage
from helpers import fake_random_password, fake_chars_password


@allure.suite('Reset Password')
class TestResetPassword():

    @allure.sub_suite('1. Проверка перехода по ссылке на страницу восстановления пароля')
    def test_go_to_the_reset_password_page(self, browser, login):
        allure.dynamic.title(
            f'{login}  - Проверка перехода по ссылке на страницу восстановления пароля')
        language = login
        password = ResetPasswordPage(browser)
        password.click_forgot_password_button(language)
        password.wait_url_to_be(data.URL_FORGOT_PASSWORD)
        current_url = password.get_current_url()
        assert current_url == data.URL_FORGOT_PASSWORD, f'Актуальный адрес страницы восстановления пароля {current_url} не равен ожидаемому {data.URL_FORGOT_PASSWORD}'

    @allure.sub_suite('2. Проверка наличия заголовка Reset Password / Сброс пароля/ Redefinir Senha')
    def test_check_title_on_reset_password_page(self, browser, login):
        allure.dynamic.title(
            f'{login}  - Проверка наличия заголовка Reset Password / Сброс пароля/ Redefinir Senha')
        language = login
        password = ResetPasswordPage(browser)
        password.click_forgot_password_button(language)
        password.wait_url_to_be(data.URL_FORGOT_PASSWORD)
        title = password.get_title_reset_password_page(language)
        if language == 'en':
            excepted_title = data.TITLE_RESET_PASSWORD_EN
        elif language == 'ru':
            excepted_title = data.TITLE_RESET_PASSWORD_RU
        elif language == 'pt':
            excepted_title = data.TITLE_RESET_PASSWORD_PT
        assert title == excepted_title, f'Заголовок {title} не соответствует ожидаемому {excepted_title}'

    @allure.sub_suite('3. Проверка наличия email, введённого ранее на странице входа')
    def test_check_email_text_on_reset_password_page(self, browser, login):
        allure.dynamic.title(
            f'{login}  - Проверка наличия email, введённого ранее на странице входа')
        language = login
        password = ResetPasswordPage(browser)
        password.click_forgot_password_button(language)
        password.wait_url_to_be(data.URL_FORGOT_PASSWORD)
        email = password.get_email_reset_password_page()
        excepted_email = data.EXISTING_EMAIL
        assert email == excepted_email, f'Email {email} не соответствует ожидаемому {excepted_email}'

    @allure.sub_suite('4. Проверка наличия ссылки Change email/Alterar email/Изменить электронную почту')
    def test_check_change_email_link_on_reset_password_page(self, browser, login):
        allure.dynamic.title(
            f'{login}  - Проверка наличия ссылки Change email/Alterar email/Изменить электронную почту')
        language = login
        password = ResetPasswordPage(browser)
        password.click_forgot_password_button(language)
        password.wait_url_to_be(data.URL_FORGOT_PASSWORD)
        assert password.find_change_email_link(
            language), f'Не нашлась ссылка {language}'

    @allure.sub_suite('5. Проверка перехода по ссылке Change email/Alterar email/Изменить электронную почту')
    def test_click_change_email_link_on_reset_password_page(self, browser, login):
        allure.dynamic.title(
            f'{login}  - Проверка перехода по ссылке Change email/Alterar email/Изменить электронную почту')
        language = login
        password = ResetPasswordPage(browser)
        password.click_forgot_password_button(language)
        password.wait_url_to_be(data.URL_FORGOT_PASSWORD)
        current_url = password.ckick_change_email_link_and_get_current_url(
            language)
        assert current_url == data.URL_SIGNIN, f'Актуальный url {current_url} не равен ожидаемому {data.URL_SIGNIN}'

    @allure.sub_suite('6. Кнопка сброса пароля неактивна при незаполненных полях')
    def test_check_reset_button_with_empty_fields(self, browser, login):
        allure.dynamic.title(
            f'{login}  - Кнопка сброса пароля неактивна при незаполненных полях')
        language = login
        password = ResetPasswordPage(browser)
        password.click_forgot_password_button(language)
        password.wait_url_to_be(data.URL_FORGOT_PASSWORD)
        reset_password_button = password.find_reset_password_button(language)
        assert not reset_password_button.is_enabled(), 'Кнопка сброса пароля активна'

    @allure.sub_suite('7. В первом поле Create Password / Создать пароль / Criar senha присутствует плейсхолдер')
    def test_check_placeholder_in_enter_password_field(self, browser, login):
        allure.dynamic.title(
            f'{login}  - В первом поле Create Password / Создать пароль / Criar senha присутствует плейсхолдер')
        language = login
        password = ResetPasswordPage(browser)
        password.click_forgot_password_button(language)
        password.wait_url_to_be(data.URL_FORGOT_PASSWORD)
        placeholder = password.get_placeholder_from_enter_password_field(language)
        if language == 'en':
            excepted_placeholder = data.PLACEHOLDER_PASSWORD_FIELD_EN
        elif language == 'ru':
            excepted_placeholder = data.PLACEHOLDER_PASSWORD_FIELD_RU
        elif language == 'pt':
            excepted_placeholder = data.PLACEHOLDER_PASSWORD_FIELD_PT
        assert placeholder == excepted_placeholder, f'Актуальный плейсхолдер {placeholder} не соответствует ожидаемому {excepted_placeholder}'

    @allure.sub_suite('8. Проверка на обязательность заполнения: оставить первое поле пустым')
    def test_check_error_message_with_empty_create_password_field(self, browser, login):
        allure.dynamic.title(
            f'{login}  - Проверка на обязательность заполнения: оставить первое поле пустым')
        language = login
        password = ResetPasswordPage(browser)
        password.click_forgot_password_button(language)
        password.wait_url_to_be(data.URL_FORGOT_PASSWORD)
        password.find_repeat_password_field_and_type_text('12345678')
        password.click_reset_password_button(language)
        error_massage = password.find_error_message_create_password(language)
        if language == 'en':
            excepted_error_massage = data.REQUIRED_FIELD_MESSAGE_EN
        elif language == 'ru':
            excepted_error_massage = data.REQUIRED_FIELD_MESSAGE_RU
        elif language == 'pt':
            excepted_error_massage = data.REQUIRED_FIELD_MESSAGE_PT
        assert error_massage == excepted_error_massage, f'Текст ошибки {error_massage} не равен ожидаемому {excepted_error_massage}'

    @allure.sub_suite('9. Проверка на обязательность заполнения: оставить второе поле пустым')
    def test_check_error_message_with_empty_repeat_password_field(self, browser, login):
        allure.dynamic.title(
            f'{login}  - Проверка на обязательность заполнения: оставить второе поле пустым')
        language = login
        password = ResetPasswordPage(browser)
        password.click_forgot_password_button(language)
        password.wait_url_to_be(data.URL_FORGOT_PASSWORD)
        password.find_password_field_and_type_text('12345678')
        password.click_reset_password_button(language)
        error_massage = password.find_error_message_repeat_password(language)
        if language == 'en':
            excepted_error_massage = data.REQUIRED_FIELD_MESSAGE_EN
        elif language == 'ru':
            excepted_error_massage = data.REQUIRED_FIELD_MESSAGE_RU
        elif language == 'pt':
            excepted_error_massage = data.REQUIRED_FIELD_MESSAGE_PT
        assert error_massage == excepted_error_massage, f'Текст ошибки {error_massage} не равен ожидаемому {excepted_error_massage}'

    @allure.sub_suite('10. Проверка ввода 2х разных валидных паролей')
    def test_check_enter_two_different_password(self, browser, login):
        allure.dynamic.title(f'{login}  - Проверка ввода 2х разных валидных паролей')
        language = login
        password = ResetPasswordPage(browser)
        password.click_forgot_password_button(language)
        password.wait_url_to_be(data.URL_FORGOT_PASSWORD)
        password.find_password_field_and_type_text('12345678')
        password.find_repeat_password_field_and_type_text('87654321')
        password.click_reset_password_button(language)
        error_massage = password.find_error_message_repeat_password(language)
        if language == 'en':
            excepted_error_massage = data.MUST_MUTCH_PASSWORD_MESSAGE_EN
        elif language == 'ru':
            excepted_error_massage = data.MUST_MUTCH_PASSWORD_MESSAGE_RU
        elif language == 'pt':
            excepted_error_massage = data.MUST_MUTCH_PASSWORD_MESSAGE_PT
        assert error_massage == excepted_error_massage, f'Текст ошибки {error_massage} не равен ожидаемому {excepted_error_massage}'

    @allure.sub_suite('11. Проверка ввода 2х одинаковых валидных паролей, но в разном регистре')
    def test_check_enter_two_seperate_password_in_different_register(self, browser, login):
        allure.dynamic.title(
            f'{login}  - Проверка ввода 2х одинаковых валидных паролей, но в разном регистре')
        language = login
        password = ResetPasswordPage(browser)
        password.click_forgot_password_button(language)
        password.wait_url_to_be(data.URL_FORGOT_PASSWORD)
        password.find_password_field_and_type_text('asdfghjk')
        password.find_repeat_password_field_and_type_text('ASDFGHJK')
        password.click_reset_password_button(language)
        error_massage = password.find_error_message_repeat_password(language)
        if language == 'en':
            excepted_error_massage = data.MUST_MUTCH_PASSWORD_MESSAGE_EN
        elif language == 'ru':
            excepted_error_massage = data.MUST_MUTCH_PASSWORD_MESSAGE_RU
        elif language == 'pt':
            excepted_error_massage = data.MUST_MUTCH_PASSWORD_MESSAGE_PT
        assert error_massage == excepted_error_massage, f'Текст ошибки {error_massage} не равен ожидаемому {excepted_error_massage}'

    @allure.sub_suite('12. Негативные проверки валидации: Проверка ввода 2х одинаковых невалидных паролей')
    @pytest.mark.parametrize('length_password', [1, 7])
    def test_check_enter_two_seperate_uncorrect_password(self, browser, login, length_password):
        allure.dynamic.title(f'{login}  - {length_password} символов')
        language = login
        password = ResetPasswordPage(browser)
        password.click_forgot_password_button(language)
        password.wait_url_to_be(data.URL_FORGOT_PASSWORD)
        uncorrect_password = fake_chars_password(length_password)
        password.find_password_field_and_type_text(uncorrect_password)
        password.find_repeat_password_field_and_type_text(uncorrect_password)
        password.click_reset_password_button(language)
        repeat_error_massage = create_error_massage = password.find_error_message_create_password(language)
        if language == 'en':
            excepted_create_error_massage = excepted_repeat_error_massage = data.INCORRECT_LENGTH_MASSAGE_EN
        elif language == 'ru':
            excepted_create_error_massage = excepted_repeat_error_massage = data.INCORRECT_LENGTH_MASSAGE_RU
        elif language == 'pt':
            excepted_create_error_massage = excepted_repeat_error_massage = data.INCORRECT_LENGTH_MASSAGE_PT
        assert create_error_massage == excepted_create_error_massage and \
            repeat_error_massage == excepted_repeat_error_massage, \
            f'Текст ошибки под полем создания пароля "{create_error_massage}" не равен ожидаемому "{excepted_create_error_massage}" \
                или текст ошибки под полем повтора пароля "{repeat_error_massage}" не равен ожидаемому "{excepted_repeat_error_massage}"'
    
    @allure.sub_suite('13. Позитивные проверки валидации - Проверка ввода 2х одинаковых валидных паролей')
    @pytest.mark.parametrize('length_password', [8, 9])
    def test_check_enter_two_seperate_correct_password(self, browser, login, length_password):
        allure.dynamic.title(f'{login}  - {length_password} символов')
        language = login
        password = ResetPasswordPage(browser)
        password.click_forgot_password_button(language)
        password.wait_url_to_be(data.URL_FORGOT_PASSWORD)
        correct_password = fake_random_password(length_password)
        password.find_password_field_and_type_text(correct_password)
        password.find_repeat_password_field_and_type_text(correct_password)
        password.click_reset_password_button(language)
        password.wait_url_to_be(data.URL_VERIFICATION_CODE)
        assert password.find_title_verification_code_page(language), f'{language} - Заголовок страницы Verification Code не найден'
