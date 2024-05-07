import data
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
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

    def find_reset_password_button(self, language):
        if language == 'en':
            return self.find_element(reset_password.RESET_PASSWORD_BUTTON_EN)
        elif language == 'ru':
            return self.find_element(reset_password.RESET_PASSWORD_BUTTON_RU)
        elif language == 'pt':
            return self.find_element(reset_password.RESET_PASSWORD_BUTTON_PT)

    def find_password_field_and_type_text(self, password):
        self.wait_visible_element(reset_password.ENTER_PASSWORD_FIELD)
        self.type_text(reset_password.ENTER_PASSWORD_FIELD, password)

    def find_repeat_password_field_and_type_text(self, password):
        self.wait_visible_element(reset_password.REPEATE_PASSWORD_FIELD)
        self.type_text(reset_password.REPEATE_PASSWORD_FIELD, password)

    def find_error_message_create_password(self, language):
        if language == 'en':
            self.wait_visible_element(
                reset_password.ERROR_MESSAGE_ENTER_PASSWORD_EN)
            return self.get_text_element(reset_password.ERROR_MESSAGE_ENTER_PASSWORD_EN)
        elif language == 'ru':
            self.wait_visible_element(
                reset_password.ERROR_MESSAGE_ENTER_PASSWORD_EN)
            return self.get_text_element(reset_password.ERROR_MESSAGE_ENTER_PASSWORD_RU)
        elif language == 'pt':
            self.wait_visible_element(
                reset_password.ERROR_MESSAGE_ENTER_PASSWORD_EN)
            return self.get_text_element(reset_password.ERROR_MESSAGE_ENTER_PASSWORD_PT)
        
    def find_error_message_repeat_password(self, language):
        if language == 'en':
            self.wait_visible_element(
                reset_password.ERROR_MESSAGE_REPEAT_PASSWORD_EN)
            return self.get_text_element(reset_password.ERROR_MESSAGE_REPEAT_PASSWORD_EN)
        elif language == 'ru':
            self.wait_visible_element(
                reset_password.ERROR_MESSAGE_REPEAT_PASSWORD_EN)
            return self.get_text_element(reset_password.ERROR_MESSAGE_REPEAT_PASSWORD_EN)
        elif language == 'pt':
            self.wait_visible_element(
                reset_password.ERROR_MESSAGE_REPEAT_PASSWORD_EN)
            return self.get_text_element(reset_password.ERROR_MESSAGE_REPEAT_PASSWORD_EN)









    def get_lk_page_url(self):
        return self.get_current_url()

    # def find_lk_title_en(self):
    #     return expected_conditions.visibility_of_element_located((signin_password.LK_TITLE_EN))

    # def find_lk_title_ru(self):
    #     return expected_conditions.visibility_of_element_located((signin_password.LK_TITLE_RU))

    # def find_lk_title_pt(self):
    #     return expected_conditions.visibility_of_element_located((signin_password.LK_TITLE_PT))

    
