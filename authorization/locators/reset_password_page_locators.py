import data
from selenium.webdriver.common.by import By


class ResetPasswordPageLocators():

    ENTER_PASSWORD_FIELD = By.NAME, 'password'
    REPEATE_PASSWORD_FIELD = By.NAME, 'repeatPassword'

    FORGOT_PASWWORD_BUTTON_EN = By.XPATH, '//button[text() = "Forgot password?"]'
    FORGOT_PASWWORD_BUTTON_RU = By.XPATH, '//button[text() = "Забыли пароль?"]'
    FORGOT_PASWWORD_BUTTON_PT = By.XPATH, '//button[text() = "Esqueceu a senha?"]'

    RESET_PASSWORD_TITLE_EN = By.XPATH, '//p[text() = "Reset Password"]'
    RESET_PASSWORD_TITLE_RU = By.XPATH, '//p[text() = "Сброс пароля"]'
    RESET_PASSWORD_TITLE_PT = By.XPATH, '//p[text() = "Redefinir senha"]'

    EMAIL_RESET_PASSWORD = By.XPATH, '//p[text() = "test@test.com"]'

    CHANGE_EMAIL_LINK_EN = By.LINK_TEXT, 'Change email'
    CHANGE_EMAIL_LINK_RU = By.LINK_TEXT, 'Изменить электронную почту'
    CHANGE_EMAIL_LINK_PT = By.LINK_TEXT, 'Alterar email'

    RESET_PASSWORD_BUTTON_EN = By.XPATH, '//button[text() = "Reset Password"]'
    RESET_PASSWORD_BUTTON_RU = By.XPATH, '//button[text() = "Сбросить пароль"]'
    RESET_PASSWORD_BUTTON_PT = By.XPATH, '//button[text() = "Redefinir senha"]'

    ERROR_MESSAGE_ENTER_PASSWORD_EN = By.XPATH, '//label[text()="Create Password"]/following-sibling::span'
    ERROR_MESSAGE_ENTER_PASSWORD_RU = By.XPATH, '//label[text()="Создать пароль"]/following-sibling::span'
    ERROR_MESSAGE_ENTER_PASSWORD_PT = By.XPATH, '//label[text()="Criar senha"]/following-sibling::span'

    ERROR_MESSAGE_REPEAT_PASSWORD_EN = By.XPATH, '//label[text()="Repeat Password"]/following-sibling::span'
    ERROR_MESSAGE_REPEAT_PASSWORD_RU = By.XPATH, '//label[text()="Повторите пароль"]/following-sibling::span'
    ERROR_MESSAGE_REPEAT_PASSWORD_PT = By.XPATH, '//label[text()="Repetir senha"]/following-sibling::span'

    VERIFICATION_CODE_TITLE_EN = By.XPATH, '//p[text() = "Check Your Email"]'
    VERIFICATION_CODE_TITLE_RU = By.XPATH, '//p[text() = "Проверьте свою почту"]'
    VERIFICATION_CODE_TITLE_PT = By.XPATH, '//p[text() = "Verifique seu email"]'

    # LK_TITLE_EN = By.XPATH, '//p[text() = "Dashboard Overview"]'
    # LK_TITLE_RU = By.XPATH, '//p[text()= "Обзор информационной панели"]'
    # LK_TITLE_PT = By.XPATH, '//p[text() = "Visão Geral do Painel"]'

    # CREATE_ACCOUNT_TITLE_EN = By.XPATH, '//p[text() = "Create an Account"]'
    # CREATE_ACCOUNT_TITLE_RU = By.XPATH, '//p[text()= "Создать аккаунт"]'
    # CREATE_ACCOUNT_TITLE_PT = By.XPATH, '//p[text() = "Criar uma Conta"]'

    # ERROR_MESSAGE_EN = By.XPATH, '//span[text()="Incorrect login password"]'
    # ERROR_MESSAGE_RU = By.XPATH, '//span[text()="Неправильный логин/пароль для входа"]'
    # ERROR_MESSAGE_PT = By.XPATH, '//span[text()="Senha de login incorreta"]'


#     INCORRECT_LOGIN_PASSWORD_MESSAGE_EN = 'Incorrect login password'


# INCORRECT_LOGIN_PASSWORD_MESSAGE_RU = 'Неправильный логин/пароль для входа'
# INCORRECT_LOGIN_PASSWORD_MESSAGE_PT = 'Senha de login incorreta'
