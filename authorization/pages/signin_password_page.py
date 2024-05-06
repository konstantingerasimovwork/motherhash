import data
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from authorization.pages.base_page import BasePage
from authorization.locators.signin_password_page_locators import SignInPasswordPageLocators as signin_password

class SignInPasswordPage(BasePage):

    def find_password_field_and_type_text(self, password):
        self.wait_visible_element(signin_password.SIGNIN_PASSWORD_FIELD)
        self.type_text(signin_password.SIGNIN_PASSWORD_FIELD, password)

    # def click_enter_en_button(self):
    #     self.click_element(signin_password.ENTER_BUTTON_EN)

    # def click_enter_ru_button(self):
    #     self.click_element(signin_password.ENTER_BUTTON_RU)

    # def click_enter_pt_button(self):
    #     self.click_element(signin_password.ENTER_BUTTON_PT)

    def click_enter_button(self, language):
        if language == 'en':
            self.click_element(signin_password.ENTER_BUTTON_EN)
        elif language == 'ru':
            self.click_element(signin_password.ENTER_BUTTON_RU)
        elif language == 'pt':
            self.click_element(signin_password.ENTER_BUTTON_PT)

    def get_lk_page_url(self):
        return self.get_current_url()
    
    # def find_and_get_error_message(self):
    #     self.wait_visible_element(signin_password.ERROR_MESSAGE)
    #     return self.get_text_element(signin_password.ERROR_MESSAGE)

    # def find_lk_title_en(self):
    #     return expected_conditions.visibility_of_element_located((signin_password.LK_TITLE_EN))

    # def find_lk_title_ru(self):
    #     return expected_conditions.visibility_of_element_located((signin_password.LK_TITLE_RU))

    # def find_lk_title_pt(self):
    #     return expected_conditions.visibility_of_element_located((signin_password.LK_TITLE_PT))
    
    def find_error_message(self, language):
        if language == 'en':
            return expected_conditions.visibility_of_element_located((signin_password.ERROR_MESSAGE_EN))
        elif language == 'ru':
            return expected_conditions.visibility_of_element_located((signin_password.ERROR_MESSAGE_RU))
        elif language == 'pt':
            return expected_conditions.visibility_of_element_located((signin_password.ERROR_MESSAGE_PT))

    def find_enter_button(self, language):
        if language == 'en':
            return self.find_element(signin_password.ENTER_BUTTON_EN)
        elif language == 'ru':
            return self.find_element(signin_password.ENTER_BUTTON_RU)
        elif language == 'pt':
            return self.find_element(signin_password.ENTER_BUTTON_PT)
