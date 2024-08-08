import allure
from authorization.pages.base_page import BasePage
from authorization.locators.signin_password_page_locators import SignInPasswordPageLocators as signin_password

class SignInPasswordPage(BasePage):

    def find_welcome_title(self, language):
        if language == 'en':
            return self.visibility_of_element_located(signin_password.WELCOME_TITLE_EN)
        elif language == 'ru':
            return self.visibility_of_element_located(signin_password.WELCOME_TITLE_RU)
        elif language == 'pt':
            return self.visibility_of_element_located(signin_password.WELCOME_TITLE_PT)
    
    @allure.step('Получаем email под заголовком на странице "Забыли пароль?"')
    def get_email_signin_password_page(self):
        return self.get_text_element(signin_password.EMAIL_SIGNIN_PASSWORD)
    
    @allure.step('Находим ссылку "Изменить email"')
    def find_change_email_link(self, language):
        if language == 'en':
            return self.find_element(signin_password.CHANGE_EMAIL_LINK_EN)
        elif language == 'ru':
            return self.find_element(signin_password.CHANGE_EMAIL_LINK_RU)
        elif language == 'pt':
            return self.find_element(signin_password.CHANGE_EMAIL_LINK_PT)
        
    @allure.step('Клик по ссылке "Изменить email" и получение актуального адреса')
    def ckick_change_email_link_and_get_current_url(self, language):
        if language == 'en':
            self.click_element(signin_password.CHANGE_EMAIL_LINK_EN)
        elif language == 'ru':
            self.click_element(signin_password.CHANGE_EMAIL_LINK_RU)
        elif language == 'pt':
            self.click_element(signin_password.CHANGE_EMAIL_LINK_PT)
        return self.get_current_url()
    
    @allure.step('Находим поле ввода пароля и вводим пароль')
    def find_password_field_and_type_text(self, password):
        self.wait_visible_element(signin_password.SIGNIN_PASSWORD_FIELD)
        self.type_text(signin_password.SIGNIN_PASSWORD_FIELD, password)

    @allure.step('Клик по кнопке "Войти"')
    def click_enter_button(self, language):
        if language == 'en':
            self.click_element(signin_password.ENTER_BUTTON_EN)
        elif language == 'ru':
            self.click_element(signin_password.ENTER_BUTTON_RU)
        elif language == 'pt':
            self.click_element(signin_password.ENTER_BUTTON_PT)

    @allure.step('Получаем url главной страницы ЛК')
    def get_lk_page_url(self):
        return self.get_current_url()

    @allure.step('Находим сообщение об ошибке')
    def find_error_message(self, language):
        if language == 'en':
            return self.visibility_of_element_located(signin_password.ERROR_MESSAGE_EN)
        elif language == 'ru':
            return self.visibility_of_element_located(signin_password.ERROR_MESSAGE_RU)
        elif language == 'pt':
            return self.visibility_of_element_located(signin_password.ERROR_MESSAGE_PT)

    @allure.step('Находим кнопку "Войти"')
    def find_enter_button(self, language):
        if language == 'en':
            return self.find_element(signin_password.ENTER_BUTTON_EN)
        elif language == 'ru':
            return self.find_element(signin_password.ENTER_BUTTON_RU)
        elif language == 'pt':
            return self.find_element(signin_password.ENTER_BUTTON_PT)
