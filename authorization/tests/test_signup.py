import allure
import pytest
import data
from authorization.pages.signup_password_page import SignUpPasswordPage
from helpers import fake_random_password, fake_chars_password
from helpers import fake_email


@allure.suite('SignUp Password')
class TestSignUpPassword():

    @allure.sub_suite('1. Проверка наличия заголовка Create an Account / Создать аккаунт / Criar conta')
    def test_check_title_on_signup_page(self, browser, create_login):
        allure.dynamic.title(
            f'{create_login}  - Проверка наличия заголовка Create an Account / Создать аккаунт / Criar conta')
        language = create_login
        password = SignUpPasswordPage(browser)
        title = password.get_title_signup_password_page(language)
        if language == 'en':
            excepted_title = data.TITLE_SIGNUP_PASSWORD_EN
        elif language == 'ru':
            excepted_title = data.TITLE_SIGNUP_PASSWORD_RU
        elif language == 'pt':
            excepted_title = data.TITLE_SIGNUP_PASSWORD_PT
        assert title == excepted_title, f'Заголовок {title} не соответствует ожидаемому {excepted_title}'

    @allure.sub_suite('2. Проверка наличия email, введённого ранее на странице входа')
    def test_check_email_text_on_signup_page(self, browser, language):
        allure.dynamic.title(
            f'{language}  - Проверка наличия email, введённого ранее на странице входа')
        unregistred_email = fake_email()
        password = SignUpPasswordPage(browser)
        password.find_email_field_and_type_text(unregistred_email)
        password.click_continue_button(language)
        password.wait_signup_url_to_be(data.URL_SIGNUP)
        email_on_page = password.get_email_signup_password_page(unregistred_email)
        assert unregistred_email == email_on_page, f'Email {email_on_page} не соответствует ожидаемому {unregistred_email}'

    @allure.sub_suite('3. Проверка наличия ссылки Change email/Alterar email/Изменить электронную почту')
    def test_check_change_email_link_on_signup_page(self, browser, create_login):
        allure.dynamic.title(
            f'{create_login}  - Проверка наличия ссылки Change email/Alterar email/Изменить электронную почту')
        language = create_login
        password = SignUpPasswordPage(browser)
        assert password.find_change_email_link(
            language), f'Не нашлась ссылка {language}'

    @allure.sub_suite('4. Проверка перехода по ссылке Change email/Alterar email/Изменить электронную почту')
    def test_click_change_email_link_on_signup_page(self, browser, create_login):
        allure.dynamic.title(
            f'{create_login}  - Проверка перехода по ссылке Change email/Alterar email/Изменить электронную почту')
        language = create_login
        password = SignUpPasswordPage(browser)
        current_url = password.ckick_change_email_link_and_get_current_url(
            language)
        assert current_url == data.URL_SIGNIN, f'Актуальный url {current_url} не равен ожидаемому {data.URL_SIGNIN}'

    @allure.sub_suite('5. Кнопка Продолжить неактивна при незаполненных полях')
    def test_check_reset_button_with_empty_fields(self, browser, create_login):
        allure.dynamic.title(
            f'{create_login}  - Кнопка Продолжить неактивна при незаполненных полях')
        language = create_login
        password = SignUpPasswordPage(browser)
        reset_password_button = password.find_continue_button(language)
        assert not reset_password_button.is_enabled(), 'Кнопка Продолжить активна'

    @allure.sub_suite('6. В первом поле Create Password / Создать пароль / Criar senha присутствует плейсхолдер')
    def test_check_placeholder_in_enter_password_field(self, browser, create_login):
        allure.dynamic.title(
            f'{create_login}  - В первом поле Create Password / Создать пароль / Criar senha присутствует плейсхолдер')
        language = create_login
        password = SignUpPasswordPage(browser)
        placeholder = password.get_placeholder_from_enter_password_field(
            language)
        if language == 'en':
            excepted_placeholder = data.PLACEHOLDER_PASSWORD_FIELD_EN
        elif language == 'ru':
            excepted_placeholder = data.PLACEHOLDER_PASSWORD_FIELD_RU
        elif language == 'pt':
            excepted_placeholder = data.PLACEHOLDER_PASSWORD_FIELD_PT
        assert placeholder == excepted_placeholder, f'Актуальный плейсхолдер {placeholder} не соответствует ожидаемому {excepted_placeholder}'

    @allure.sub_suite('7. Проверка на обязательность заполнения: оставить первое поле пустым')
    def test_check_error_message_with_empty_create_password_field(self, browser, create_login):
        allure.dynamic.title(
            f'{create_login}  - Проверка на обязательность заполнения: оставить первое поле пустым')
        language = create_login
        password = SignUpPasswordPage(browser)
        password.find_repeat_password_field_and_type_text('12345678')
        password.click_continue_button(language)
        error_massage = password.find_error_message_create_password(language)
        if language == 'en':
            excepted_error_massage = data.REQUIRED_FIELD_MESSAGE_EN
        elif language == 'ru':
            excepted_error_massage = data.REQUIRED_FIELD_MESSAGE_RU
        elif language == 'pt':
            excepted_error_massage = data.REQUIRED_FIELD_MESSAGE_PT
        assert error_massage == excepted_error_massage, f'Текст ошибки {error_massage} не равен ожидаемому {excepted_error_massage}'

    @allure.sub_suite('8. Проверка на обязательность заполнения: оставить второе поле пустым')
    def test_check_error_message_with_empty_repeat_password_field(self, browser, create_login):
        allure.dynamic.title(
            f'{create_login}  - Проверка на обязательность заполнения: оставить второе поле пустым')
        language = create_login
        password = SignUpPasswordPage(browser)
        password.find_password_field_and_type_text('12345678')
        password.click_continue_button(language)
        error_massage = password.find_error_message_repeat_password(language)
        if language == 'en':
            excepted_error_massage = data.REQUIRED_FIELD_MESSAGE_EN
        elif language == 'ru':
            excepted_error_massage = data.REQUIRED_FIELD_MESSAGE_RU
        elif language == 'pt':
            excepted_error_massage = data.REQUIRED_FIELD_MESSAGE_PT
        assert error_massage == excepted_error_massage, f'Текст ошибки {error_massage} не равен ожидаемому {excepted_error_massage}'

    @allure.sub_suite('9. Проверка ввода 2х разных валидных паролей')
    def test_check_enter_two_different_password(self, browser, create_login):
        allure.dynamic.title(
            f'{create_login}  - Проверка ввода 2х разных валидных паролей')
        language = create_login
        password = SignUpPasswordPage(browser)
        password.find_password_field_and_type_text('12345678')
        password.find_repeat_password_field_and_type_text('87654321')
        password.click_continue_button(language)
        error_massage = password.find_error_message_repeat_password(language)
        if language == 'en':
            excepted_error_massage = data.MUST_MUTCH_PASSWORD_MESSAGE_EN
        elif language == 'ru':
            excepted_error_massage = data.MUST_MUTCH_PASSWORD_MESSAGE_RU
        elif language == 'pt':
            excepted_error_massage = data.MUST_MUTCH_PASSWORD_MESSAGE_PT
        assert error_massage == excepted_error_massage, f'Текст ошибки {error_massage} не равен ожидаемому {excepted_error_massage}'

    @allure.sub_suite('10. Проверка ввода 2х одинаковых валидных паролей, но в разном регистре')
    def test_check_enter_two_seperate_password_in_different_register(self, browser, create_login):
        allure.dynamic.title(
            f'{create_login}  - Проверка ввода 2х одинаковых валидных паролей, но в разном регистре')
        language = create_login
        password = SignUpPasswordPage(browser)
        password.find_password_field_and_type_text('asdfghjk')
        password.find_repeat_password_field_and_type_text('ASDFGHJK')
        password.click_continue_button(language)
        error_massage = password.find_error_message_repeat_password(language)
        if language == 'en':
            excepted_error_massage = data.MUST_MUTCH_PASSWORD_MESSAGE_EN
        elif language == 'ru':
            excepted_error_massage = data.MUST_MUTCH_PASSWORD_MESSAGE_RU
        elif language == 'pt':
            excepted_error_massage = data.MUST_MUTCH_PASSWORD_MESSAGE_PT
        assert error_massage == excepted_error_massage, f'Текст ошибки {error_massage} не равен ожидаемому {excepted_error_massage}'

    @allure.sub_suite('11. Негативные проверки валидации: Проверка ввода 2х одинаковых невалидных паролей')
    @pytest.mark.parametrize('length_password', [1, 7])
    def test_check_enter_two_seperate_uncorrect_password(self, browser, create_login, length_password):
        allure.dynamic.title(f'{create_login}  - {length_password} символов')
        language = create_login
        password = SignUpPasswordPage(browser)
        uncorrect_password = fake_chars_password(length_password)
        password.find_password_field_and_type_text(uncorrect_password)
        password.find_repeat_password_field_and_type_text(uncorrect_password)
        password.click_continue_button(language)
        repeat_error_massage = create_error_massage = password.find_error_message_create_password(
            language)
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

    @allure.sub_suite('12. Позитивные проверки валидации - Проверка ввода 2х одинаковых валидных паролей')
    @pytest.mark.parametrize('length_password', [8, 9])
    def test_check_enter_two_seperate_correct_password(self, browser, create_login, length_password):
        allure.dynamic.title(f'{create_login}  - {length_password} символов')
        language = create_login
        password = SignUpPasswordPage(browser)
        correct_password = fake_random_password(length_password)
        password.find_password_field_and_type_text(correct_password)
        password.find_repeat_password_field_and_type_text(correct_password)
        password.click_continue_button(language)
        password.wait_verification_code_url_to_be(data.URL_VERIFICATION_CODE)
        assert password.find_title_verification_code_page(
            language), f'{language} - Заголовок страницы Verification Code не найдет'
