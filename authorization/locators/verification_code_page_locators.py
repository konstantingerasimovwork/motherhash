from selenium.webdriver.common.by import By


class VerificationCodePageLocators():

    VERIFICATION_CODE_TITLE_EN = By.XPATH, '//p[text() = "Check Your Email"]'
    VERIFICATION_CODE_TITLE_RU = By.XPATH, '//p[text() = "Проверьте свою почту"]'
    VERIFICATION_CODE_TITLE_PT = By.XPATH, '//p[text() = "Verifique seu email"]'

    @staticmethod
    def email_verification_code(fake_email):
        return By.XPATH, f'//p[text() = "{fake_email}"]'

    CHANGE_EMAIL_LINK_EN = By.LINK_TEXT, 'Change email'
    CHANGE_EMAIL_LINK_RU = By.LINK_TEXT, 'Изменить электронную почту'
    CHANGE_EMAIL_LINK_PT = By.LINK_TEXT, 'Alterar email'

    SIGNIN_EMAIL_FIELD = By.NAME, 'email'
    CONTINUE_BUTTON_EN = By.XPATH, '//button[text() = "Continue"]'
    CONTINUE_BUTTON_RU = By.XPATH, '//button[text() = "Продолжить"]'
    CONTINUE_BUTTON_PT = By.XPATH, '//button[text() = "Continuar"]'

    ENTER_PASSWORD_FIELD = By.NAME, 'password'
    REPEATE_PASSWORD_FIELD = By.NAME, 'repeatPassword'
    
