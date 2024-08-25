import time
import allure
from authorization.pages.base_page import BasePage
from authorization.locators.verification_code_page_locators import VerificationCodePageLocators as verification_code

class VerificationCodePage(BasePage):

    @allure.step('Получаем текст заголовка страницы "Verification Code"')
    def get_title_verification_code_page(self, language):
        if language == 'en':
            self.wait_visible_element(verification_code.VERIFICATION_CODE_TITLE_EN)
            return self.get_text_element(verification_code.VERIFICATION_CODE_TITLE_EN)
        elif language == 'ru':
            self.wait_visible_element(
                verification_code.VERIFICATION_CODE_TITLE_RU)
            return self.get_text_element(verification_code.VERIFICATION_CODE_TITLE_RU)
        elif language == 'pt':
            self.wait_visible_element(
                verification_code.VERIFICATION_CODE_TITLE_PT)
            return self.get_text_element(verification_code.VERIFICATION_CODE_TITLE_PT)

    def type_fake_email_and_click_continue_button(self, unregistred_email, language, url):
        self.wait_visible_element(verification_code.SIGNIN_EMAIL_FIELD)
        self.type_text(verification_code.SIGNIN_EMAIL_FIELD, unregistred_email)
        if language == 'en':
            self.click_element(verification_code.CONTINUE_BUTTON_EN)
        elif language == 'ru':
            self.click_element(verification_code.CONTINUE_BUTTON_RU)
        elif language == 'pt':
            self.click_element(verification_code.CONTINUE_BUTTON_PT)
        self.wait_url_to_be(url)

    def type_new_password_and_click_continue_button(self, correct_password, language, url):
        self.wait_visible_element(verification_code.ENTER_PASSWORD_FIELD)
        self.type_text(verification_code.ENTER_PASSWORD_FIELD, correct_password)
        self.wait_visible_element(verification_code.REPEATE_PASSWORD_FIELD)
        self.type_text(verification_code.REPEATE_PASSWORD_FIELD, correct_password)
        if language == 'en':
            self.click_element(verification_code.CONTINUE_BUTTON_EN)
        elif language == 'ru':
            self.click_element(verification_code.CONTINUE_BUTTON_RU)
        elif language == 'pt':
            self.click_element(verification_code.CONTINUE_BUTTON_PT)
        self.wait_url_to_be(url)

    @allure.step('Получаем email под заголовком на странице "Verification Code"')
    def get_email_verification_code_page(self, fake_email):
        self.wait_visible_element(
            verification_code.email_verification_code(fake_email))
        return self.get_text_element(verification_code.email_verification_code(fake_email))

    @allure.step('Находим ссылку "Изменить email"')
    def find_change_email_link(self, language):
        if language == 'en':
            self.wait_visible_element(verification_code.CHANGE_EMAIL_LINK_EN)
            return self.find_element(verification_code.CHANGE_EMAIL_LINK_EN)
        elif language == 'ru':
            self.wait_visible_element(verification_code.CHANGE_EMAIL_LINK_RU)
            return self.find_element(verification_code.CHANGE_EMAIL_LINK_RU)
        elif language == 'pt':
            self.wait_visible_element(verification_code.CHANGE_EMAIL_LINK_PT)
            return self.find_element(verification_code.CHANGE_EMAIL_LINK_PT)

    @allure.step('Клик по ссылке "Изменить email" и получение актуального адреса')
    def click_change_email_link_and_get_current_url(self, language):
        if language == 'en':
            self.wait_visible_element(verification_code.CHANGE_EMAIL_LINK_EN)
            self.click_element(verification_code.CHANGE_EMAIL_LINK_EN)
        elif language == 'ru':
            self.wait_visible_element(verification_code.CHANGE_EMAIL_LINK_RU)
            self.click_element(verification_code.CHANGE_EMAIL_LINK_RU)
        elif language == 'pt':
            self.wait_visible_element(verification_code.CHANGE_EMAIL_LINK_PT)
            self.click_element(verification_code.CHANGE_EMAIL_LINK_PT)
        return self.get_current_url()

    @allure.step('Находим текст повторной отправки кода и таймера 60 сек')
    def find_resend_text_and_timer_60_sec(self, language):
        if language == 'en':
            self.wait_visible_element_by_time(
                verification_code.TIME_60_SEC_RESEND_CODE_EN, 10)
            return self.find_element(verification_code.TIME_60_SEC_RESEND_CODE_EN)
        if language == 'ru':
            self.wait_visible_element_by_time(
                verification_code.TIME_60_SEC_RESEND_CODE_RU, 10)
            return self.find_element(verification_code.TIME_60_SEC_RESEND_CODE_RU)
        if language == 'pt':
            self.wait_visible_element_by_time(
                verification_code.TIME_60_SEC_RESEND_CODE_PT, 10)
            return self.find_element(verification_code.TIME_60_SEC_RESEND_CODE_PT)
    
    @allure.step('Находим текст повторной отправки кода и таймера 0 сек')
    def find_resend_text_and_timer_01_sec(self, language):
        if language == 'en':
            self.wait_visible_element_by_time(
                verification_code.TIME_01_SEC_RESEND_CODE_EN, 70)
            return self.find_element(verification_code.TIME_01_SEC_RESEND_CODE_EN)
        if language == 'ru':
            self.wait_visible_element_by_time(
                verification_code.TIME_01_SEC_RESEND_CODE_RU, 70)
            return self.find_element(verification_code.TIME_01_SEC_RESEND_CODE_RU)
        if language == 'pt':
            self.wait_visible_element_by_time(
                verification_code.TIME_01_SEC_RESEND_CODE_PT, 70)
            return self.find_element(verification_code.TIME_01_SEC_RESEND_CODE_PT)
        
    @allure.step('Находим текст вопроса "Не получили письмо?"')
    def find_resend_question(self, language):
        if language == 'en':
            self.wait_visible_element_by_time(
                verification_code.RESEND_CODE_TEXT_EN, 70)
            return self.find_element(verification_code.RESEND_CODE_TEXT_EN)
        if language == 'ru':
            self.wait_visible_element_by_time(
                verification_code.RESEND_CODE_TEXT_RU, 70)
            return self.find_element(verification_code.RESEND_CODE_TEXT_RU)
        if language == 'pt':
            self.wait_visible_element_by_time(
                verification_code.RESEND_CODE_TEXT_PT, 70)
            return self.find_element(verification_code.RESEND_CODE_TEXT_PT)

    @allure.step('Находим ссылку "Нажмите, чтобы отправить повторно"')
    def find_resend_link(self, language):
        if language == 'en':
            self.wait_visible_element(
                verification_code.RESEND_CODE_LINK_EN)
            return self.find_element(verification_code.RESEND_CODE_LINK_EN)
        if language == 'ru':
            self.wait_visible_element(
                verification_code.RESEND_CODE_LINK_RU)
            return self.find_element(verification_code.RESEND_CODE_LINK_RU)
        if language == 'pt':
            self.wait_visible_element(
                verification_code.RESEND_CODE_LINK_PT)
            return self.find_element(verification_code.RESEND_CODE_LINK_PT)

    @allure.step('Ждём 60 секунд до появления ссылки отправки кода повторно')
    def wait_resend_link(self, language):
        if language == 'en':
            self.wait_visible_element_by_time(
                verification_code.TIME_01_SEC_RESEND_CODE_EN, 70)
            self.wait_visible_element(
                verification_code.RESEND_CODE_LINK_EN)
        if language == 'ru':
            self.wait_visible_element_by_time(
                verification_code.TIME_01_SEC_RESEND_CODE_RU, 70)
            self.wait_visible_element(
                verification_code.RESEND_CODE_LINK_RU)
        if language == 'pt':
            self.wait_visible_element_by_time(
                verification_code.TIME_01_SEC_RESEND_CODE_PT, 70)
            self.wait_visible_element(
                verification_code.RESEND_CODE_LINK_PT)
    
    @allure.step('Нажимаем на ссылку повторной отправки кода и находим таймер 60 секунд')
    def click_resend_link_and_find_60_sec_timer(self, language):
        if language == 'en':
            self.wait_visible_element(
                verification_code.RESEND_CODE_LINK_EN)
            self.click_element(verification_code.RESEND_CODE_LINK_EN)
            self.wait_visible_element(
                verification_code.TIME_60_SEC_RESEND_CODE_EN)
            return self.find_element(verification_code.TIME_60_SEC_RESEND_CODE_EN)
        if language == 'ru':
            self.wait_visible_element(
                verification_code.RESEND_CODE_LINK_RU)
            self.click_element(verification_code.RESEND_CODE_LINK_RU)
            self.wait_visible_element(
                verification_code.TIME_60_SEC_RESEND_CODE_RU)
            return self.find_element(verification_code.TIME_60_SEC_RESEND_CODE_RU)
        if language == 'pt':
            self.wait_visible_element(
                verification_code.RESEND_CODE_LINK_PT)
            self.click_element(verification_code.RESEND_CODE_LINK_PT)
            self.wait_visible_element(
                verification_code.TIME_60_SEC_RESEND_CODE_PT)
            return self.find_element(verification_code.TIME_60_SEC_RESEND_CODE_PT)

    @allure.step('Нажимаем на ссылку повторной отправки кода и находим таймер 60 секунд')
    def type_verification_code(self, number_of_field, code):
        self.wait_presence_of_all_elements_located(
            verification_code.VERIFICATION_CODE_FIELDS_TAG)
        verification_code_fields = self.find_elements(
            verification_code.VERIFICATION_CODE_FIELDS)
        code_list = list(code)
        for field, symbol in zip(verification_code_fields[:number_of_field], code_list):
            field.send_keys(symbol)
    
    @allure.step('Находим кнопку Проверить')
    def find_verify_button(self, language):
        if language == 'en':
            self.wait_visible_element(
                verification_code.VERIFY_BUTTON_EN)
            return self.find_element(verification_code.VERIFY_BUTTON_EN)
        if language == 'ru':
            self.wait_visible_element(
                verification_code.VERIFY_BUTTON_RU)
            return self.find_element(verification_code.VERIFY_BUTTON_RU)
        if language == 'pt':
            self.wait_visible_element(
                verification_code.VERIFY_BUTTON_PT)
            return self.find_element(verification_code.VERIFY_BUTTON_PT)
    
    @allure.step('Проверяем, что кнопки Проверить нет на странице')
    def check_verify_button(self, language):
        if language == 'en':
            return self.invisibility_of_element_located(
                verification_code.VERIFY_BUTTON_EN)
        if language == 'ru':
            return self.invisibility_of_element_located(
                verification_code.VERIFY_BUTTON_RU)
        if language == 'pt':
            return self.invisibility_of_element_located(
                verification_code.VERIFY_BUTTON_PT)

    @allure.step('Кликаем по кнопке Проверить')
    def click_verify_button(self, language):
        if language == 'en':
            self.wait_visible_element(
                verification_code.VERIFY_BUTTON_EN)
            self.click_element(
                verification_code.VERIFY_BUTTON_EN)
        if language == 'ru':
            self.wait_visible_element(
                verification_code.VERIFY_BUTTON_RU)
            self.click_element(
                verification_code.VERIFY_BUTTON_RU)
        if language == 'pt':
            self.wait_visible_element(
                verification_code.VERIFY_BUTTON_PT)
            self.click_element(
                verification_code.VERIFY_BUTTON_PT)

    @allure.step('Находим и получаем текст ошибки')
    def find_and_get_error_message(self, language):
        if language == 'en':
            self.wait_visible_element(verification_code.ERROR_MESSAGE_EN)
            return self.find_element(verification_code.ERROR_MESSAGE_EN)
        if language == 'ru':
            self.wait_visible_element(verification_code.ERROR_MESSAGE_RU)
            return self.find_element(verification_code.ERROR_MESSAGE_RU)
        if language == 'pt':
            self.wait_visible_element(verification_code.ERROR_MESSAGE_PT)
            return self.find_element(verification_code.ERROR_MESSAGE_PT)
    
    def wait_lk_url_to_be(self, url):
        return self.wait_url_to_be(url)
    
    @allure.step('Проверяем наличие заголовка главной страницы ЛК "Обзорная панель"')
    def get_title_dashboard_overview_page(self, language):
        if language == 'en':
            self.wait_visible_element(
                verification_code.DASHBOARD_OVERVIEW_TITLE_EN)
            return self.find_element(verification_code.DASHBOARD_OVERVIEW_TITLE_EN)
        elif language == 'ru':
            self.wait_visible_element(
                verification_code.DASHBOARD_OVERVIEW_TITLE_RU)
            return self.find_element(verification_code.DASHBOARD_OVERVIEW_TITLE_RU)
        elif language == 'pt':
            self.wait_visible_element(
                verification_code.DASHBOARD_OVERVIEW_TITLE_PT)
            return self.get_text_element(verification_code.DASHBOARD_OVERVIEW_TITLE_PT)
