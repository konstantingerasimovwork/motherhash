import data
from selenium.webdriver.common.by import By


class SignInPasswordPageLocators():

    SIGNIN_PASSWORD_FIELD = By.NAME, 'password'

    ENTER_BUTTON_EN = By.XPATH, '//button[text() = "Login"]'
    ENTER_BUTTON_RU = By.XPATH, '//button[text() = "Войти"]'
    ENTER_BUTTON_PT = By.XPATH, '//button[text() = "Entrar"]'

    LK_TITLE_EN = By.XPATH, '//p[text() = "Dashboard Overview"]'
    LK_TITLE_RU = By.XPATH, '//p[text()= "Обзор информационной панели"]'
    LK_TITLE_PT = By.XPATH, '//p[text() = "Visão Geral do Painel"]'

    # CREATE_ACCOUNT_TITLE_EN = By.XPATH, '//p[text() = "Create an Account"]'
    # CREATE_ACCOUNT_TITLE_RU = By.XPATH, '//p[text()= "Создать аккаунт"]'
    # CREATE_ACCOUNT_TITLE_PT = By.XPATH, '//p[text() = "Criar uma Conta"]'

    ERROR_MESSAGE_EN = By.XPATH, '//span[text()="Incorrect login password"]'
    ERROR_MESSAGE_RU = By.XPATH, '//span[text()="Неправильный логин/пароль для входа"]'
    ERROR_MESSAGE_PT = By.XPATH, '//span[text()="Senha de login incorreta"]'


#     INCORRECT_LOGIN_PASSWORD_MESSAGE_EN = 'Incorrect login password'


# INCORRECT_LOGIN_PASSWORD_MESSAGE_RU = 'Неправильный логин/пароль для входа'
# INCORRECT_LOGIN_PASSWORD_MESSAGE_PT = 'Senha de login incorreta'
