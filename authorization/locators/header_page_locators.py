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
    HOW_TO_START_EN = By.XPATH, './/a[contains(text(), "How to Start")]'
    HOW_TO_START_PT = By.XPATH, './/a[contains(text(), "Como Começar")]'
    HOW_TO_START_RU = By.XPATH, './/a[contains(text(), "Как начать")]'
    HOW_TO_START_LOCATOR = By.ID, 'howToStart'
    HOW_TO_START_H1_LOCATOR = By.XPATH, '//*[@id="howToStart"]/h1'
    
    CONTRACT_EN = By.XPATH, './/a[contains(text(), "Contracts")]'
    CONTRACT_PT = By.XPATH, './/a[contains(text(), "Criar Contrato")]'
    CONTRACT_RU = By.XPATH, './/a[contains(text(), "Контракты")]'
    CONTRACT_LOCATOR = By.ID, 'createContract'
    CONTRACT_H1_LOCATOR = By.XPATH, '//*[@id="createContract"]/h1'

    FAQ = By.XPATH, './/a[contains(text(), "FAQ")]'
    FAQ_LOCATOR = By.ID, 'faq'
    FAQ_H1_LOCATOR = By.XPATH, '//*[@id="faq"]/h1'
