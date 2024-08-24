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
    def find_receive_question(self, language):
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
    def find_receive_link(self, language):
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
