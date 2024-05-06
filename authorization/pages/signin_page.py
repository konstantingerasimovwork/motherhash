import data
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from authorization.pages.base_page import BasePage
from authorization.locators.signin_page_locators import SignInPageLocators as signin


class SignInPage(BasePage):

    def change_language(self, chose_language):
        # self.wait_visible_element(language_button)
        self.wait_visible_element(signin.LANGUAGE_BUTTON)
        self.click_element(signin.LANGUAGE_BUTTON)
        self.wait_visible_element(signin.LANGUAGE_MENU)
        self.find_element(chose_language).click()

    def find_email_field_and_type_text(self, email):
        self.wait_visible_element(signin.SIGNIN_EMAIL_FIELD)
        self.type_text(signin.SIGNIN_EMAIL_FIELD, email)

    def click_continue_button(self, button):
        self.click_element(button)

    def get_welcome_page_url(self):
        return self.get_current_url()

    def find_welcome_title(self, title):
        return expected_conditions.visibility_of_element_located((title))
    
    def wait_password_url_to_be(self, url):
        self.wait_url_to_be(url)
    
    def wait_signup_url_to_be(self, url):
        self.wait_url_to_be(url)
    
    def get_signup_page_url(self):
        return self.get_current_url()
