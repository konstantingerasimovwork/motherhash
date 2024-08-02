import allure
from authorization.pages.base_page import BasePage
from authorization.locators.signin_page_locators import SignInPageLocators as signin


class SignInPage(BasePage):

    @allure.step('Сменить язык - {language}')
    def change_language(self, language):
        self.wait_visible_element(signin.LANGUAGE_BUTTON)
        self.click_element(signin.LANGUAGE_BUTTON)
        self.wait_visible_element(signin.LANGUAGE_MENU)
        if language == 'en':
            self.find_element(signin.LANGUAGE_EN).click()
        elif language == 'ru':
            self.find_element(signin.LANGUAGE_RU).click()
        elif language == 'pt':
            self.find_element(signin.LANGUAGE_PT).click()

    @allure.step('Находим поле email и ввести {email}')
    def find_email_field_and_type_text(self, email):
        self.wait_visible_element(signin.SIGNIN_EMAIL_FIELD)
        self.type_text(signin.SIGNIN_EMAIL_FIELD, email)

    @allure.step('Нажимаем на кнопку "Продолжить"')
    def click_continue_button(self, language):
        if language == 'en':
            self.click_element(signin.CONTINUE_BUTTON_EN)
        elif language == 'ru':
            self.click_element(signin.CONTINUE_BUTTON_RU)
        elif language == 'pt':
            self.click_element(signin.CONTINUE_BUTTON_PT)

    @allure.step('Получаем адрес страницы ввода пароля "Добро пожаловать"')
    def get_welcome_page_url(self):
        return self.get_current_url()

    @allure.step('Получаем заголовок страницы ввода пароля "Добро пожаловать"')
    def find_welcome_title(self, language):
        if language == 'en':
            return self.visibility_of_element_located(signin.WELCOME_TITLE_EN)
        elif language == 'ru':
            return self.visibility_of_element_located(signin.WELCOME_TITLE_RU)
        elif language == 'pt':
            return self.visibility_of_element_located(signin.WELCOME_TITLE_PT)
    
    @allure.step('Получаем заголовок страницы создания нового пароля "Создать аккаунт"')
    def find_create_account_title(self, language):
        if language == 'en':
            return self.visibility_of_element_located(signin.CREATE_ACCOUNT_TITLE_EN)
        elif language == 'ru':
            return self.visibility_of_element_located(signin.CREATE_ACCOUNT_TITLE_RU)
        elif language == 'pt':
            return self.visibility_of_element_located(signin.CREATE_ACCOUNT_TITLE_PT)

    @allure.step('Ожидаем смены ссылки {url}')
    def wait_password_url_to_be(self, url):
        self.wait_url_to_be(url)

    @allure.step('Ожидаем смены ссылки {url}')
    def wait_signup_url_to_be(self, url):
        self.wait_url_to_be(url)
    
    @allure.step('Получаем ссылку страницы SignUp')
    def get_signup_page_url(self):
        return self.get_current_url()
    
    @allure.step('Находим и получаем текст ошибки')
    def find_and_get_error_message(self):
        self.wait_visible_element(signin.ERROR_MESSAGE)
        return self.get_text_element(signin.ERROR_MESSAGE)