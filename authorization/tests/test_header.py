import time
import pytest
import data
from authorization.pages.header_page import HeaderPage
from authorization.locators.header_page_locators import HeaderPageLocators as hp


class TestHeader():
    
    #Проверка наличия логотипа и перехода на главную страницу лендинга
    @pytest.mark.parametrize('language, logo, main_url', [(hp.LANGUAGE_EN, hp.LOGO_EN, data.URL_MAIN_PAGE_EN),
                                                          (hp.LANGUAGE_RU, hp.LOGO_RU, data.URL_MAIN_PAGE_RU),
                                                          (hp.LANGUAGE_PT, hp.LOGO_PT, data.URL_MAIN_PAGE_PT)])
    def test_header_logo(self, browser, language, logo, main_url):
        header_page = HeaderPage(browser)
        browser.get(data.URL_SIGNIN)
        header_page.change_language(language)
        header_page.find_element_and_click(logo)
        header_page.wait_main_url_to_be(main_url)
        current_url = header_page.get_current_main_url()
        result = header_page.find_logo_on_main_page()
        assert result and current_url == main_url, f'Лого на главной странице не найдено или {current_url} не равен {main_url}'

    # Проверка перехода по пункту меню “How to Start/Как начать/Como Comecar“ на раздел How to Start/Как начать/Como Comecar на главной странице лендинга
    @pytest.mark.parametrize('language, how_to_start_link, how_to_start_url, text', [(hp.LANGUAGE_EN, hp.HOW_TO_START_EN, data.URL_HOW_TO_START_EN, data.HOW_TO_START_EN_TEXT),
                                                                                     (hp.LANGUAGE_RU, hp.HOW_TO_START_RU, data.URL_HOW_TO_START_RU, data.HOW_TO_START_RU_TEXT),
                                                                                     (hp.LANGUAGE_PT, hp.HOW_TO_START_PT, data.URL_HOW_TO_START_PT, data.HOW_TO_START_PT_TEXT)])
    def test_header_how_to_start(self, browser, language, how_to_start_link, how_to_start_url, text):
        header_page = HeaderPage(browser)
        browser.get(data.URL_SIGNIN)
        header_page.change_language(language)
        header_page.find_element_and_click(how_to_start_link)
        header_page.wait_main_url_to_be(how_to_start_url)
        current_url = header_page.get_current_main_url()
        result = header_page.get_lending_how_to_start_block_text()
        assert result == text and current_url == how_to_start_url, \
                        f'Текст заголовка how to start "{result}" не равен ожидаемому тексту "{text}" или {current_url} не равен {how_to_start_url}'

    # Проверка перехода по пункту меню “Contracts/Контракты/Criar Contrato“ на раздел Contracts/Контракты/Criar Contrato на главной странице лендинга
    @pytest.mark.parametrize('language, create_contract_link, create_contract_url, text', [(hp.LANGUAGE_EN, hp.CONTRACT_EN, data.URL_CONTRACT_EN, data.CONTRACT_EN_TEXT),
                                                                                     (hp.LANGUAGE_RU, hp.CONTRACT_RU, data.URL_CONTRACT_RU, data.CONTRACT_RU_TEXT),
                                                                                     (hp.LANGUAGE_PT, hp.CONTRACT_PT, data.URL_CONTRACT_PT, data.CONTRACT_PT_TEXT)])
    def test_header_create_contract(self, browser, language, create_contract_link, create_contract_url, text):
        header_page = HeaderPage(browser)
        browser.get(data.URL_SIGNIN)
        header_page.change_language(language)
        header_page.find_element_and_click(create_contract_link)
        header_page.wait_main_url_to_be(create_contract_url)
        current_url = header_page.get_current_main_url()
        result = header_page.get_lending_create_contract_block_text()
        assert result == text and current_url == create_contract_url, \
            f'Текст заголовка create contract "{result}" не равен ожидаемому тексту "{text}" или {current_url} не равен {create_contract_url}'

    # Проверка перехода по пункту меню "FAQ" на раздел "FAQ/FAQ/Perguntas frequentes" главной страницы лендинга
    @pytest.mark.parametrize('language, create_faq_link, create_faq_url, text', [(hp.LANGUAGE_EN, hp.FAQ, data.URL_FAQ_EN, data.FAQ_EN_TEXT),
                                                                                           (hp.LANGUAGE_RU, hp.FAQ, data.URL_FAQ_RU, data.FAQ_RU_TEXT),
                                                                                           (hp.LANGUAGE_PT, hp.FAQ, data.URL_FAQ_PT, data.FAQ_PT_TEXT)])
    def test_header_create_faq(self, browser, language, create_faq_link, create_faq_url, text):
        header_page = HeaderPage(browser)
        browser.get(data.URL_SIGNIN)
        header_page.change_language(language)
        header_page.find_element_and_click(create_faq_link)
        header_page.wait_main_url_to_be(create_faq_url)
        current_url = header_page.get_current_main_url()
        result = header_page.get_lending_create_faq_block_text()
        assert result == text and current_url == create_faq_url, \
            f'Текст заголовка faq "{result}" не равен ожидаемому тексту "{text}" или {current_url} не равен {create_faq_url}'
