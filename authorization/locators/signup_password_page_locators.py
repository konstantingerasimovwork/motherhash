import data
from selenium.webdriver.common.by import By


class SignUpPasswordPageLocators():

    ENTER_PASSWORD_FIELD = By.NAME, 'password'
    REPEATE_PASSWORD_FIELD = By.NAME, 'repeatPassword'

    CREATE_PASSWORD_TITLE_EN = By.XPATH, '//p[text() = "Create an Account"]'
    CREATE_PASSWORD_TITLE_RU = By.XPATH, '//p[text() = "Создать аккаунт"]'
    CREATE_PASSWORD_TITLE_PT = By.XPATH, '//p[text() = "Criar conta"]'

    @staticmethod
    def email_signup_password(fake_email):
        return By.XPATH, f'//p[text() = "{fake_email}"]'

    CHANGE_EMAIL_LINK_EN = By.LINK_TEXT, 'Change email'
    CHANGE_EMAIL_LINK_RU = By.LINK_TEXT, 'Изменить электронную почту'
    CHANGE_EMAIL_LINK_PT = By.LINK_TEXT, 'Alterar email'

    CONTINUE_BUTTON_EN = By.XPATH, '//button[text() = "Continue"]'
    CONTINUE_BUTTON_RU = By.XPATH, '//button[text() = "Продолжить"]'
    CONTINUE_BUTTON_PT = By.XPATH, '//button[text() = "Continuar"]'

    ERROR_MESSAGE_ENTER_PASSWORD_EN = By.XPATH, '//label[text()="Create Password"]/following-sibling::span'
    ERROR_MESSAGE_ENTER_PASSWORD_RU = By.XPATH, '//label[text()="Создать пароль"]/following-sibling::span'
    ERROR_MESSAGE_ENTER_PASSWORD_PT = By.XPATH, '//label[text()="Criar senha"]/following-sibling::span'

    ERROR_MESSAGE_REPEAT_PASSWORD_EN = By.XPATH, '//label[text()="Repeat Password"]/following-sibling::span'
    ERROR_MESSAGE_REPEAT_PASSWORD_RU = By.XPATH, '//label[text()="Повторите пароль"]/following-sibling::span'
    ERROR_MESSAGE_REPEAT_PASSWORD_PT = By.XPATH, '//label[text()="Repetir senha"]/following-sibling::span'

    VERIFICATION_CODE_TITLE_EN = By.XPATH, '//p[text() = "Check Your Email"]'
    VERIFICATION_CODE_TITLE_RU = By.XPATH, '//p[text() = "Проверьте свою почту"]'
    VERIFICATION_CODE_TITLE_PT = By.XPATH, '//p[text() = "Verifique seu email"]'

    SIGNIN_EMAIL_FIELD = By.NAME, 'email'

    CONTINUE_BUTTON_EN = By.XPATH, '//button[text() = "Continue"]'
    CONTINUE_BUTTON_RU = By.XPATH, '//button[text() = "Продолжить"]'
    CONTINUE_BUTTON_PT = By.XPATH, '//button[text() = "Continuar"]'
