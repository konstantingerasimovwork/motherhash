from selenium.webdriver.common.by import By

class SignInPasswordPageLocators():

    SIGNIN_PASSWORD_FIELD = By.NAME, 'password'

    ENTER_BUTTON_EN = By.XPATH, '//button[text() = "Login"]'
    ENTER_BUTTON_RU = By.XPATH, '//button[text() = "Войти"]'
    ENTER_BUTTON_PT = By.XPATH, '//button[text() = "Entrar"]'

    LK_TITLE_EN = By.XPATH, '//p[text() = "Dashboard Overview"]'
    LK_TITLE_RU = By.XPATH, '//p[text()= "Обзор информационной панели"]'
    LK_TITLE_PT = By.XPATH, '//p[text() = "Visão Geral do Painel"]'

    ERROR_MESSAGE_EN = By.XPATH, '//span[text()="Incorrect login password"]'
    ERROR_MESSAGE_RU = By.XPATH, '//span[text()="Неправильный логин/пароль для входа"]'
    ERROR_MESSAGE_PT = By.XPATH, '//span[text()="Senha de login incorreta"]'

    WELCOME_TITLE_EN = By.XPATH, '//p[text() = "Welcome"]'
    WELCOME_TITLE_RU = By.XPATH, '//p[text()= "Добро пожаловать"]'
    WELCOME_TITLE_PT = By.XPATH, '//p[text() = "Bem-vindo"]'

    EMAIL_SIGNIN_PASSWORD = By.XPATH, '//p[text() = "test@test.com"]'

    CHANGE_EMAIL_LINK_EN = By.LINK_TEXT, 'Change email'
    CHANGE_EMAIL_LINK_RU = By.LINK_TEXT, 'Изменить электронную почту'
    CHANGE_EMAIL_LINK_PT = By.LINK_TEXT, 'Alterar email'
