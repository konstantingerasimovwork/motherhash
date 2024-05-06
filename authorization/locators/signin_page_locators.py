import data
from selenium.webdriver.common.by import By


class SignInPageLocators():

    LANGUAGE_BUTTON = By.CSS_SELECTOR, 'button.MuiButtonBase-root span.MuiStack-root'
    LANGUAGE_MENU = By.CLASS_NAME, 'MuiMenu-list'
    LANGUAGE_EN = By.XPATH, './/ul/li[1]/div'
    LANGUAGE_PT = By.XPATH, './/ul/li[2]/div'
    LANGUAGE_RU = By.XPATH, './/ul/li[3]/div'

    SIGNIN_EMAIL_FIELD = By.NAME, 'email'

    CONTINUE_BUTTON_EN = By.XPATH, '//button[text() = "Continue"]'
    CONTINUE_BUTTON_RU = By.XPATH, '//button[text() = "Продолжить"]'
    CONTINUE_BUTTON_PT = By.XPATH, '//button[text() = "Continuar"]'

    WELCOME_TITLE_EN = By.XPATH, '//p[text() = "Welcome"]'
    WELCOME_TITLE_RU = By.XPATH, '//p[text()= "Добро пожаловать"]'
    WELCOME_TITLE_PT = By.XPATH, '//p[text() = "Bem-vindo"]'

    CREATE_ACCOUNT_TITLE_EN = By.XPATH, '//p[text() = "Create an Account"]'
    CREATE_ACCOUNT_TITLE_RU = By.XPATH, '//p[text()= "Создать аккаунт"]'
    CREATE_ACCOUNT_TITLE_PT = By.XPATH, '//p[text() = "Criar uma Conta"]'

