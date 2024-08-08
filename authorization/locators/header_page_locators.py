import data
from selenium.webdriver.common.by import By


class HeaderPageLocators():

    LOGO_RU = By.XPATH, f'.//a[@href="{data.URL_MAIN_PAGE_RU}/"]'
    LOGO_EN = By.XPATH, f'.//a[@href="{data.URL_MAIN_PAGE_EN}en/"]'
    LOGO_PT = By.XPATH, f'.//a[@href="{data.URL_MAIN_PAGE_PT}/"]'
    LANGUAGE_BUTTON = By.CSS_SELECTOR, 'button.MuiButtonBase-root span.MuiStack-root'
    LANGUAGE_MENU = By.CLASS_NAME, 'MuiMenu-list'
    LANGUAGE_EN = By.XPATH, './/ul/li[1]/div'
    LANGUAGE_PT = By.XPATH, './/ul/li[2]/div'
    LANGUAGE_RU = By.XPATH, './/ul/li[3]/div'

    MAIN_PAGE_LOGO = By.XPATH, './/img[@alt="logo"]'
    
    CONTRACT_EN = By.XPATH, './/a[contains(text(), "Create contract")]'
    CONTRACT_PT = By.XPATH, './/a[contains(text(), "Criar contrato")]'
    CONTRACT_RU = By.XPATH, './/a[contains(text(), "Создание контракта")]'
    CONTRACT_LOCATOR = By.ID, 'createContract'
    CONTRACT_H1_LOCATOR = By.XPATH, '//*[@id="createContract"]//h1'

    ADVANTAGES_EN = By.XPATH, './/a[contains(text(), "Advantages")]'
    ADVANTAGES_PT = By.XPATH, './/a[contains(text(), "Vantagens")]'
    ADVANTAGES_RU = By.XPATH, './/a[contains(text(), "Преимущества")]'
    ADVANTAGES_LOCATOR = By.ID, 'advantages'
    ADVANTAGES_H1_LOCATOR = By.XPATH, '//*[@id="advantages"]//h1'

    FAQ = By.XPATH, './/a[contains(text(), "FAQ")]'
    FAQ_LOCATOR = By.ID, 'faq'
    FAQ_H1_LOCATOR = By.XPATH, '//*[@id="faq"]//h1'
