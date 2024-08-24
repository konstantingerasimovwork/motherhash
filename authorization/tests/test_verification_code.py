import allure
import pytest
import data
from authorization.pages.verification_code_page import VerificationCodePage
from helpers import fake_random_password
from helpers import fake_email


@allure.suite('Verification Code')
class TestVerificationCodePassword():

    @allure.sub_suite('1. Проверка наличия заголовка Check Your Email / Проверьте свою почту / Проверьте свою почту')
    def test_check_title_on_verification_code_page(self, browser, create_login_and_password):
        allure.dynamic.title(
            f'{create_login_and_password}  - Проверка наличия заголовка Check Your Email / Проверьте свою почту / Проверьте свою почту')
        language = create_login_and_password
        verification_code = VerificationCodePage(browser)
        title = verification_code.get_title_verification_code_page(language)
        if language == 'en':
            excepted_title = data.TITLE_VERIFICATION_CODE_EN
        elif language == 'ru':
            excepted_title = data.TITLE_VERIFICATION_CODE_RU
        elif language == 'pt':
            excepted_title = data.TITLE_VERIFICATION_CODE_PT
        assert title == excepted_title, f'Заголовок {title} не соответствует ожидаемому {excepted_title}'

    @allure.sub_suite('2. Проверка наличия email, введённого ранее на странице входа')
    def test_check_email_text_on_verification_code_page(self, browser, language):
        allure.dynamic.title(
            f'{language}  - Проверка наличия email, введённого ранее на странице входа')
        verification_code = VerificationCodePage(browser)
        unregistred_email = fake_email()
        correct_password = fake_random_password(8)
        verification_code.type_fake_email_and_click_continue_button(unregistred_email, language, data.URL_SIGNUP)
        verification_code.type_new_password_and_click_continue_button(correct_password, language, data.URL_VERIFICATION_CODE)
        email_on_page = verification_code.get_email_verification_code_page(unregistred_email)
        assert unregistred_email == email_on_page, f'Email {email_on_page} не соответствует ожидаемому {unregistred_email}'

    @allure.sub_suite('3. Проверка наличия ссылки Change email/Alterar email/Изменить электронную почту')
    def test_check_change_email_link_on_verification_code_page(self, browser, create_login_and_password):
        allure.dynamic.title(
            f'{create_login_and_password}  - Проверка наличия ссылки Change email/Alterar email/Изменить электронную почту')
        language = create_login_and_password
        password = VerificationCodePage(browser)
        assert password.find_change_email_link(
            language), f'Не нашлась ссылка {language}'

    @allure.sub_suite('4. Проверка перехода по ссылке Change email/Alterar email/Изменить электронную почту')
    def test_click_change_email_link_on_verification_code_page(self, browser, create_login_and_password):
        allure.dynamic.title(
            f'{create_login_and_password}  - Проверка перехода по ссылке Change email/Alterar email/Изменить электронную почту')
        language = create_login_and_password
        password = VerificationCodePage(browser)
        current_url = password.click_change_email_link_and_get_current_url(
            language)
        assert current_url == data.URL_SIGNIN, f'Актуальный url {current_url} не равен ожидаемому {data.URL_SIGNIN}'

    @allure.sub_suite("5. Наличие на странице текста Resend Code / Повторная отправка кода / Reenviar código em и таймера 60 секунд")
    def test_timer_60_sec(self, browser, create_login_and_password):
        allure.dynamic.title(
            f"{create_login_and_password} - Наличие на странице текста Resend Code / Повторная отправка кода / Reenviar código em и таймера 60 секунд")
        language = create_login_and_password
        password = VerificationCodePage(browser)
        result_60_sec = password.find_resend_text_and_timer_60_sec(language)
        result_01_sec = password.find_resend_text_and_timer_01_sec(language)
        assert result_60_sec and result_01_sec, f'Таймер 60 сек не найден {result_60_sec} или таймер 1 сек {result_01_sec} не найден'

    @allure.sub_suite("6. По истечении 60 секунд появляется текст Didn't receive an email? / Не получили письмо? / Não recebeu o email?  \
                      и ссылки с текстом Click to Resend / Нажмите, чтобы отправить повторно / Clique para reenviar под полями для ввода кода подтверждения")
    def test_find_resend_link(self, browser, create_login_and_password):
        allure.dynamic.title(
            f"{create_login_and_password} - По истечении 60 секунд появляется текст Didn't receive an email? / Не получили письмо? / Não recebeu o email?  \
                      и ссылки с текстом Click to Resend / Нажмите, чтобы отправить повторно / Clique para reenviar под полями для ввода кода подтверждения")
        language = create_login_and_password
        password = VerificationCodePage(browser)
        result_resend_quastion = password.find_receive_question(language)
        result_resend_link = password.find_receive_link(language)
        assert result_resend_quastion and result_resend_link, f'Текст вопроса не найден {result_resend_quastion} или ссылка не найдена {result_resend_link}'




        




























###############################################################

    # @allure.sub_suite('4. Проверка ввода корректного кода подтверждения - 5 символов')
    # def test_enter_correct_verification_code(self, browser, create_login_and_password):
    #     allure.dynamic.title(
    #         f'{create_login_and_password} - Проверка ввода корректного кода подтверждения (5 символов) - 00000')
    #     language = create_login_and_password
    #     password = VerificationCodePage(browser)
    #     current_url = password.click_change_email_link_and_get_current_url(
    #         language)
    #     assert current_url == data.URL_SIGNIN, f'Актуальный url {current_url} не равен ожидаемому {data.URL_SIGNIN}'
