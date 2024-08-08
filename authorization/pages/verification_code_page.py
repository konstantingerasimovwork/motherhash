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
