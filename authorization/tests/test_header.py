import allure
import pytest
import data
from authorization.pages.header_page import HeaderPage
from authorization.locators.header_page_locators import HeaderPageLocators as hp


@allure.suite('Header')
class TestHeader():
    
    @allure.sub_suite('1. Проверка перехода по логотипу на главную страницу лендинга')
    @pytest.mark.parametrize('language_locator, logo, main_url, language', [(hp.LANGUAGE_EN, hp.LOGO_EN, data.URL_MAIN_PAGE_EN, 'EN'),
                                                          (hp.LANGUAGE_RU, hp.LOGO_RU, data.URL_MAIN_PAGE_RU, 'RU'),
                                                          (hp.LANGUAGE_PT, hp.LOGO_PT, data.URL_MAIN_PAGE_PT, 'PT')])
    def test_header_logo(self, browser, language_locator, logo, main_url, language):
        allure.dynamic.title(
            f'{language}  - Проверка перехода по логотипу на главную страницу лендинга')
        header_page = HeaderPage(browser)
        browser.get(data.URL_SIGNIN)
        header_page.change_language(language_locator)
        header_page.find_logo_on_authorization_page_and_click(logo)
        header_page.wait_main_url_to_be(main_url)
        current_url = header_page.get_current_main_url()
        result = header_page.find_logo_on_main_page()
        assert result and current_url == main_url, f'Лого на главной странице не найдено или {current_url} не равен {main_url}'

    @allure.sub_suite('2. Проверка перехода по пункту меню “Create contract/Создание контракта/Criar Contrato“ на раздел Create contract/Создание контракта/Criar Contrato на главной странице лендинга')
    @pytest.mark.parametrize('language_locator, create_contract_link, create_contract_url, text, language', [(hp.LANGUAGE_EN, hp.CONTRACT_EN, data.URL_CONTRACT_EN, data.CONTRACT_EN_TEXT, 'EN'),
                                                                                     (hp.LANGUAGE_RU, hp.CONTRACT_RU, data.URL_CONTRACT_RU, data.CONTRACT_RU_TEXT, 'RU'),
                                                                                     (hp.LANGUAGE_PT, hp.CONTRACT_PT, data.URL_CONTRACT_PT, data.CONTRACT_PT_TEXT, 'PT')])
    def test_header_create_contract(self, browser, language_locator, create_contract_link, create_contract_url, text, language):
        allure.dynamic.title(
            f'{language}  - Проверка перехода по пункту меню “Create contract/Создание контракта/Criar Contrato“ на раздел Create contract/Создание контракта/Criar Contrato на главной странице лендинга')
        header_page = HeaderPage(browser)
        browser.get(data.URL_SIGNIN)
        header_page.change_language(language_locator)
        header_page.find_create_contact_in_menu_and_click(create_contract_link)
        header_page.wait_main_url_to_be(create_contract_url)
        current_url = header_page.get_current_main_url()
        result = header_page.get_lending_create_contract_block_text()
        assert result == text and current_url == create_contract_url, \
            f'Текст заголовка create contract "{result}" не равен ожидаемому тексту "{text}" или {current_url} не равен {create_contract_url}'

    @allure.sub_suite('3. Проверка перехода по пункту меню “Advantages/Преимущества/Vantagens“ на раздел Advantages/Преимущества/Vantagens на главной странице лендинга')
    @pytest.mark.parametrize('language_locator, advantages_link, advantages_url, text, language', [(hp.LANGUAGE_EN, hp.ADVANTAGES_EN, data.URL_ADVANTAGES_EN, data.ADVANTAGES_EN_TEXT, 'EN'),
                                                                                     (hp.LANGUAGE_RU, hp.ADVANTAGES_RU, data.URL_ADVANTAGES_RU, data.ADVANTAGES_RU_TEXT, 'RU'),
                                                                                     (hp.LANGUAGE_PT, hp.ADVANTAGES_PT, data.URL_ADVANTAGES_PT, data.ADVANTAGES_PT_TEXT, 'PT')])
    def test_header_advantages(self, browser, language_locator, advantages_link, advantages_url, text, language):
        allure.dynamic.title(
            f'{language}  - Проверка перехода по пункту меню “Advantages/Преимущества/Vantagens“ на раздел Advantages/Преимущества/Vantagens на главной странице лендинга')
        header_page = HeaderPage(browser)
        browser.get(data.URL_SIGNIN)
        header_page.change_language(language_locator)
        header_page.find_advantages_in_menu_and_click(advantages_link)
        header_page.wait_main_url_to_be(advantages_url)
        current_url = header_page.get_current_main_url()
        result = header_page.get_lending_advantages_block_text()
        assert result == text and current_url == advantages_url, \
            f'Текст заголовка how to start "{result}" не равен ожидаемому тексту "{text}" или {current_url} не равен {advantages_url}'

    @allure.sub_suite('4. Проверка перехода по пункту меню "FAQ" на раздел "FAQ/FAQ/Perguntas frequentes" главной страницы лендинга')
    @pytest.mark.parametrize('language_locator, create_faq_link, create_faq_url, text, language', [(hp.LANGUAGE_EN, hp.FAQ, data.URL_FAQ_EN, data.FAQ_EN_TEXT, 'EN'),
                                                                                           (hp.LANGUAGE_RU, hp.FAQ, data.URL_FAQ_RU, data.FAQ_RU_TEXT, 'RU'),
                                                                                           (hp.LANGUAGE_PT, hp.FAQ, data.URL_FAQ_PT, data.FAQ_PT_TEXT, 'PT')])
    def test_header_create_faq(self, browser, language_locator, create_faq_link, create_faq_url, text, language):
        allure.dynamic.title(
            f'{language}  - Проверка перехода по пункту меню "FAQ" на раздел "FAQ/FAQ/Perguntas frequentes" главной страницы лендинга')
        header_page = HeaderPage(browser)
        browser.get(data.URL_SIGNIN)
        header_page.change_language(language_locator)
        header_page.find_faq_in_menu_and_click(create_faq_link)
        header_page.wait_main_url_to_be(create_faq_url)
        current_url = header_page.get_current_main_url()
        result = header_page.get_lending_faq_block_text()
        assert result == text and current_url == create_faq_url, \
            f'Текст заголовка faq "{result}" не равен ожидаемому тексту "{text}" или {current_url} не равен {create_faq_url}'
