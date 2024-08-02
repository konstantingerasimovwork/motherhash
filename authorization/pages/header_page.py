import allure
from selenium.webdriver.support import expected_conditions
from authorization.pages.base_page import BasePage
from authorization.locators.header_page_locators import HeaderPageLocators as hp


class HeaderPage(BasePage):

    @allure.step('Изменяем язык {chose_language}')
    def change_language(self, chose_language):
        # self.wait_visible_element(language_button)
        self.wait_visible_element(hp.LANGUAGE_BUTTON)
        self.click_element(hp.LANGUAGE_BUTTON)
        self.wait_visible_element(hp.LANGUAGE_MENU)
        self.find_element(chose_language).click()
    
    @allure.step('Ищем лого на странице авторизации и кликаем по нему')
    def find_logo_on_authorization_page_and_click(self, element):
        self.click_element(element)

    @allure.step('Ищем пункт меню "Create contract" и кликаем по нему')
    def find_create_contact_in_menu_and_click(self, element):
        self.click_element(element)

    @allure.step('Ищем пункт меню "Advantages" и кликаем по нему')
    def find_advantages_in_menu_and_click(self, element):
        self.click_element(element)

    @allure.step('Ищем пункт меню "FAQ" и кликаем по нему')
    def find_faq_in_menu_and_click(self, element):
        self.click_element(element)
    
    @allure.step('Находим лого на главной странице лендинга')
    def find_logo_on_main_page(self):
        return expected_conditions.visibility_of_element_located((hp.MAIN_PAGE_LOGO))
    
    @allure.step('Ожидаем смены адреса главной страницы лендинга - {url}')
    def wait_main_url_to_be(self, url):
        self.wait_url_to_be(url)

    @allure.step('Получаем актуальную ссылку')
    def get_current_main_url(self):
        return self.get_current_url()
    
    @allure.step('Получаем текст заголовка блока Advantages')
    def get_lending_advantages_block_text(self):
        self.wait_visible_element(hp.ADVANTAGES_LOCATOR)
        return self.get_text_element(hp.ADVANTAGES_H1_LOCATOR)

    @allure.step('Получаем текст заголовка блока Create contract')
    def get_lending_create_contract_block_text(self):
        self.wait_visible_element(hp.CONTRACT_LOCATOR)
        return self.get_text_element(hp.CONTRACT_H1_LOCATOR)
    
    @allure.step('Получаем текст заголовка блока FAQ')
    def get_lending_faq_block_text(self):
        self.wait_visible_element(hp.FAQ_LOCATOR)
        return self.get_text_element(hp.FAQ_H1_LOCATOR)
