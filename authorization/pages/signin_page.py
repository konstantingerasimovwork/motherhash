import data
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from authorization.pages.base_page import BasePage
from authorization.locators.signin_page_locators import SignInPageLocators as signin


class SignInPage(BasePage):

    def change_en_language(self):
        self.wait_visible_element(signin.LANGUAGE_BUTTON)
        self.click_element(signin.LANGUAGE_BUTTON)
        self.wait_visible_element(signin.LANGUAGE_MENU)
        self.find_element(signin.LANGUAGE_EN).click()

    def change_ru_language(self):
        self.wait_visible_element(signin.LANGUAGE_BUTTON)
        self.click_element(signin.LANGUAGE_BUTTON)
        self.wait_visible_element(signin.LANGUAGE_MENU)
        self.find_element(signin.LANGUAGE_RU).click()

    def change_pt_language(self):
        self.wait_visible_element(signin.LANGUAGE_BUTTON)
        self.click_element(signin.LANGUAGE_BUTTON)
        self.wait_visible_element(signin.LANGUAGE_MENU)
        self.find_element(signin.LANGUAGE_PT).click()

    def find_email_field_and_type_text(self, email):
        self.wait_visible_element(signin.SIGNIN_EMAIL_FIELD)
        self.type_text(signin.SIGNIN_EMAIL_FIELD, email)

    def click_continue_en_button(self):
        self.click_element(signin.CONTINUE_BUTTON_EN)
    
    def click_continue_ru_button(self):
        self.click_element(signin.CONTINUE_BUTTON_RU)

    def click_continue_pt_button(self):
        self.click_element(signin.CONTINUE_BUTTON_PT)

    def get_welcome_page_url(self):
        return self.get_current_url()

    def find_welcome_title_en(self):
        return expected_conditions.visibility_of_element_located((signin.WELCOME_TITLE_EN))
    
    def find_welcome_title_ru(self):
        return expected_conditions.visibility_of_element_located((signin.WELCOME_TITLE_RU))
    
    def find_welcome_title_pt(self):
        return expected_conditions.visibility_of_element_located((signin.WELCOME_TITLE_PT))
    
    def find_create_account_title_en(self):
        return expected_conditions.visibility_of_element_located((signin.CREATE_ACCOUNT_TITLE_EN))

    def find_create_account_title_ru(self):
        return expected_conditions.visibility_of_element_located((signin.CREATE_ACCOUNT_TITLE_RU))

    def find_create_account_title_pt(self):
        return expected_conditions.visibility_of_element_located((signin.CREATE_ACCOUNT_TITLE_RU))
    
    def wait_password_url_to_be(self, url):
        self.wait_url_to_be(url)
    
    def wait_signup_url_to_be(self, url):
        self.wait_url_to_be(url)
    
    def get_signup_page_url(self):
        return self.get_current_url()
    
    def find_and_get_error_message(self):
        self.wait_visible_element(signin.ERROR_MESSAGE)
        return self.get_text_element(signin.ERROR_MESSAGE)