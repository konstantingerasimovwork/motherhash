import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from authorization.pages.base_page import BasePage
from selenium.common.exceptions import TimeoutException
from authorization.locators.header_page_locators import HeaderPageLocators as hp


class HeaderPage(BasePage):

    def change_language(self, chose_language):
        # self.wait_visible_element(language_button)
        self.wait_visible_element(hp.LANGUAGE_BUTTON)
        self.click_element(hp.LANGUAGE_BUTTON)
        self.wait_visible_element(hp.LANGUAGE_MENU)
        self.find_element(chose_language).click()
    
    
    def find_element_and_click(self, element):
        self.click_element(element)
        
    def find_logo_on_main_page(self):
        return expected_conditions.visibility_of_element_located((hp.MAIN_PAGE_LOGO))
    
    def wait_main_url_to_be(self, url):
        self.wait_url_to_be(url)

    def find_main_logo(self, logo):
        self.find_element(logo)

    def get_current_main_url(self):
        return self.get_current_url()
    
    def get_lending_how_to_start_block_text(self):
        self.wait_visible_element(hp.HOW_TO_START_LOCATOR)
        return self.get_text_element(hp.HOW_TO_START_H1_LOCATOR)

    def get_lending_create_contract_block_text(self):
        self.wait_visible_element(hp.CONTRACT_LOCATOR)
        return self.get_text_element(hp.CONTRACT_H1_LOCATOR)
    
    def get_lending_create_faq_block_text(self):
        self.wait_visible_element(hp.FAQ_LOCATOR)
        return self.get_text_element(hp.FAQ_H1_LOCATOR)
