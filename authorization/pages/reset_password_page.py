import allure
import data
from authorization.pages.base_page import BasePage
from authorization.locators.reset_password_page_locators import ResetPasswordPageLocators as reset_password


class ResetPasswordPage(BasePage):

    
    def click_forgot_password_button(self, language):
        if language == 'en':
            self.click_element(reset_password.FORGOT_PASWWORD_BUTTON_EN)
        elif language == 'ru':
            self.click_element(reset_password.FORGOT_PASWWORD_BUTTON_RU)
        elif language == 'pt':
            self.click_element(reset_password.FORGOT_PASWWORD_BUTTON_PT)

    @allure.step('Получаем текст заголовока страницы "Забыли пароль?"')
    def get_title_reset_password_page(self, language):
        if language == 'en':
            return self.get_text_element(reset_password.RESET_PASSWORD_TITLE_EN)
        elif language == 'ru':
            return self.get_text_element(reset_password.RESET_PASSWORD_TITLE_RU)
        elif language == 'pt':
            return self.get_text_element(reset_password.RESET_PASSWORD_TITLE_PT)

    @allure.step('Получаем email под заголовком на странице "Забыли пароль?"')
    def get_email_reset_password_page(self):
        return self.get_text_element(reset_password.EMAIL_RESET_PASSWORD)

    @allure.step('Находим ссылку "Изменить email"')
    def find_change_email_link(self, language):
        if language == 'en':
            return self.find_element(reset_password.CHANGE_EMAIL_LINK_EN)
        elif language == 'ru':
            return self.find_element(reset_password.CHANGE_EMAIL_LINK_RU)
        elif language == 'pt':
            return self.find_element(reset_password.CHANGE_EMAIL_LINK_PT)

    @allure.step('Клик по ссылке "Изменить email" и получение актуального адреса')
    def ckick_change_email_link_and_get_current_url(self, language):
        if language == 'en':
            self.click_element(reset_password.CHANGE_EMAIL_LINK_EN)
        elif language == 'ru':
            self.click_element(reset_password.CHANGE_EMAIL_LINK_RU)
        elif language == 'pt':
            self.click_element(reset_password.CHANGE_EMAIL_LINK_PT)
        return self.get_current_url()

    @allure.step('Получаем плейсхолдер в поле "Создать пароль"')
    def get_placeholder_from_enter_password_field(self, language):
        if language == 'en':
            self.text_to_be_present_in_element_attribute(
                reset_password.ENTER_PASSWORD_FIELD, 'placeholder', data.PLACEHOLDER_PASSWORD_FIELD_EN)
        elif language == 'ru':
            self.text_to_be_present_in_element_attribute(
                reset_password.ENTER_PASSWORD_FIELD, 'placeholder', data.PLACEHOLDER_PASSWORD_FIELD_RU)
        elif language == 'pt':
            self.text_to_be_present_in_element_attribute(
                reset_password.ENTER_PASSWORD_FIELD, 'placeholder', data.PLACEHOLDER_PASSWORD_FIELD_PT)
        return self.find_element(reset_password.ENTER_PASSWORD_FIELD).get_attribute('placeholder')

    @allure.step('Находим кнопку "Сбросить пароль"')
    def find_reset_password_button(self, language):
        if language == 'en':
            return self.find_element(reset_password.RESET_PASSWORD_BUTTON_EN)
        elif language == 'ru':
            return self.find_element(reset_password.RESET_PASSWORD_BUTTON_RU)
        elif language == 'pt':
            return self.find_element(reset_password.RESET_PASSWORD_BUTTON_PT)

    @allure.step('Находим поле "Создать пароль" и вводим пароль {password}')
    def find_password_field_and_type_text(self, password):
        self.wait_visible_element(reset_password.ENTER_PASSWORD_FIELD)
        self.type_text(reset_password.ENTER_PASSWORD_FIELD, password)

    @allure.step('Находим поле "Повторите пароль пароль" и вводим пароль {password}')
    def find_repeat_password_field_and_type_text(self, password):
        self.wait_visible_element(reset_password.REPEATE_PASSWORD_FIELD)
        self.type_text(reset_password.REPEATE_PASSWORD_FIELD, password)

    @allure.step('Клик по кнопке "Сбросить пароль"')
    def click_reset_password_button(self, language):
        if language == 'en':
            return self.click_element(reset_password.RESET_PASSWORD_BUTTON_EN)
        elif language == 'ru':
            return self.click_element(reset_password.RESET_PASSWORD_BUTTON_RU)
        elif language == 'pt':
            return self.click_element(reset_password.RESET_PASSWORD_BUTTON_PT)

    @allure.step('Получаем текст ошибки под полем "Создать пароль"')
    def find_error_message_create_password(self, language):
        if language == 'en':
            self.wait_visible_element(
                reset_password.ERROR_MESSAGE_ENTER_PASSWORD_EN)
            return self.get_text_element(reset_password.ERROR_MESSAGE_ENTER_PASSWORD_EN)
        elif language == 'ru':
            self.wait_visible_element(
                reset_password.ERROR_MESSAGE_ENTER_PASSWORD_RU)
            return self.get_text_element(reset_password.ERROR_MESSAGE_ENTER_PASSWORD_RU)
        elif language == 'pt':
            self.wait_visible_element(
                reset_password.ERROR_MESSAGE_ENTER_PASSWORD_PT)
            return self.get_text_element(reset_password.ERROR_MESSAGE_ENTER_PASSWORD_PT)

    @allure.step('Получаем текст ошибки под полем "Повторите пароль"')
    def find_error_message_repeat_password(self, language):
        if language == 'en':
            self.wait_visible_element(
                reset_password.ERROR_MESSAGE_REPEAT_PASSWORD_EN)
            return self.get_text_element(reset_password.ERROR_MESSAGE_REPEAT_PASSWORD_EN)
        elif language == 'ru':
            self.wait_visible_element(
                reset_password.ERROR_MESSAGE_REPEAT_PASSWORD_RU)
            return self.get_text_element(reset_password.ERROR_MESSAGE_REPEAT_PASSWORD_RU)
        elif language == 'pt':
            self.wait_visible_element(
                reset_password.ERROR_MESSAGE_REPEAT_PASSWORD_PT)
            return self.get_text_element(reset_password.ERROR_MESSAGE_REPEAT_PASSWORD_PT)

    @allure.step('Находим заголовок страницы ввода кода подтверждения ')
    def find_title_verification_code_page(self, language):
        if language == 'en':
            self.wait_visible_element(
                reset_password.VERIFICATION_CODE_TITLE_EN)
            return self.find_element(reset_password.VERIFICATION_CODE_TITLE_EN)
        elif language == 'ru':
            self.wait_visible_element(
                reset_password.VERIFICATION_CODE_TITLE_RU)
            return self.find_element(reset_password.VERIFICATION_CODE_TITLE_RU)
        elif language == 'pt':
            self.wait_visible_element(
                reset_password.VERIFICATION_CODE_TITLE_PT)
            return self.find_element(reset_password.VERIFICATION_CODE_TITLE_PT)
