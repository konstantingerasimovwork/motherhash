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

    TIME_60_SEC_RESEND_CODE_EN = By.XPATH, './/*[contains(text(), "Resend Code: 00:60")]'
    TIME_01_SEC_RESEND_CODE_EN = By.XPATH, './/*[contains(text(), "Resend Code: 00:01")]'
    TIME_60_SEC_RESEND_CODE_RU = By.XPATH, './/*[contains(text(), "Повторная отправка кода: 00:60")]'
    TIME_01_SEC_RESEND_CODE_RU = By.XPATH, './/*[contains(text(), "Повторная отправка кода: 00:01")]'
    TIME_60_SEC_RESEND_CODE_PT = By.XPATH, './/*[contains(text(), "Reenviar código em: 00:60")]'
    TIME_01_SEC_RESEND_CODE_PT = By.XPATH, './/*[contains(text(), "Reenviar código em: 00:01")]'
    
    RESEND_CODE_TEXT_EN = By.XPATH, './/*[contains(text(), "Didn\'t receive an email?")]'
    RESEND_CODE_TEXT_RU = By.XPATH, './/*[contains(text(), "Не получили письмо?")]'
    RESEND_CODE_TEXT_PT = By.XPATH, './/*[contains(text(), "Não recebeu o email?")]'

    RESEND_CODE_LINK_EN = By.XPATH, '//button[text() = "Click to Resend"]'
    RESEND_CODE_LINK_RU = By.XPATH, '//button[text() = "Нажмите, чтобы отправить повторно"]'
    RESEND_CODE_LINK_PT = By.XPATH, '//button[text() = "Clique para reenviar"]'
