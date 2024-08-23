import allure
import data
from authorization.pages.base_page import BasePage
from authorization.locators.signup_password_page_locators import SignUpPasswordPageLocators as signup_password


class SignUpPasswordPage(BasePage):

    @allure.step('Получаем текст заголовока страницы "Создать аккаунт"')
    def get_title_signup_password_page(self, language):
        if language == 'en':
            self.wait_visible_element(signup_password.CREATE_PASSWORD_TITLE_EN)
            return self.get_text_element(signup_password.CREATE_PASSWORD_TITLE_EN)
        elif language == 'ru':
            self.wait_visible_element(signup_password.CREATE_PASSWORD_TITLE_RU)
            return self.get_text_element(signup_password.CREATE_PASSWORD_TITLE_RU)
        elif language == 'pt':
            self.wait_visible_element(signup_password.CREATE_PASSWORD_TITLE_PT)
            return self.get_text_element(signup_password.CREATE_PASSWORD_TITLE_PT)

    @allure.step('Получаем email под заголовком на странице "Создать аккаунт"')
    def get_email_signup_password_page(self, fake_email):
        return self.get_text_element(signup_password.email_signup_password(fake_email))

    @allure.step('Находим ссылку "Изменить email"')
    def find_change_email_link(self, language):
        if language == 'en':
            return self.find_element(signup_password.CHANGE_EMAIL_LINK_EN)
        elif language == 'ru':
            return self.find_element(signup_password.CHANGE_EMAIL_LINK_RU)
        elif language == 'pt':
            return self.find_element(signup_password.CHANGE_EMAIL_LINK_PT)

    @allure.step('Клик по ссылке "Изменить email" и получение актуального адреса')
    def ckick_change_email_link_and_get_current_url(self, language):
        if language == 'en':
            self.click_element(signup_password.CHANGE_EMAIL_LINK_EN)
        elif language == 'ru':
            self.click_element(signup_password.CHANGE_EMAIL_LINK_RU)
        elif language == 'pt':
            self.click_element(signup_password.CHANGE_EMAIL_LINK_PT)
        return self.get_current_url()

    @allure.step('Получаем плейсхолдер в поле "Создать пароль"')
    def get_placeholder_from_enter_password_field(self, language):
        if language == 'en':
            self.text_to_be_present_in_element_attribute(
                signup_password.ENTER_PASSWORD_FIELD, 'placeholder', data.PLACEHOLDER_PASSWORD_FIELD_EN)
        elif language == 'ru':
            self.text_to_be_present_in_element_attribute(
                signup_password.ENTER_PASSWORD_FIELD, 'placeholder', data.PLACEHOLDER_PASSWORD_FIELD_RU)
        elif language == 'pt':
            self.text_to_be_present_in_element_attribute(
                signup_password.ENTER_PASSWORD_FIELD, 'placeholder', data.PLACEHOLDER_PASSWORD_FIELD_PT)
        return self.find_element(signup_password.ENTER_PASSWORD_FIELD).get_attribute('placeholder')

    @allure.step('Находим кнопку "Продолжить"')
    def find_continue_button(self, language):
        if language == 'en':
            return self.find_element(signup_password.CONTINUE_BUTTON_EN)
        elif language == 'ru':
            return self.find_element(signup_password.CONTINUE_BUTTON_RU)
        elif language == 'pt':
            return self.find_element(signup_password.CONTINUE_BUTTON_PT)

    @allure.step('Находим поле "Создать пароль" и вводим пароль {password}')
    def find_password_field_and_type_text(self, password):
        self.wait_visible_element(signup_password.ENTER_PASSWORD_FIELD)
        self.type_text(signup_password.ENTER_PASSWORD_FIELD, password)

    @allure.step('Находим поле "Повторите пароль пароль" и вводим пароль {password}')
    def find_repeat_password_field_and_type_text(self, password):
        self.wait_visible_element(signup_password.REPEATE_PASSWORD_FIELD)
        self.type_text(signup_password.REPEATE_PASSWORD_FIELD, password)

    @allure.step('Получаем текст ошибки под полем "Создать пароль"')
    def find_error_message_create_password(self, language):
        if language == 'en':
            self.wait_visible_element(
                signup_password.ERROR_MESSAGE_ENTER_PASSWORD_EN)
            return self.get_text_element(signup_password.ERROR_MESSAGE_ENTER_PASSWORD_EN)
        elif language == 'ru':
            self.wait_visible_element(
                signup_password.ERROR_MESSAGE_ENTER_PASSWORD_RU)
            return self.get_text_element(signup_password.ERROR_MESSAGE_ENTER_PASSWORD_RU)
        elif language == 'pt':
            self.wait_visible_element(
                signup_password.ERROR_MESSAGE_ENTER_PASSWORD_PT)
            return self.get_text_element(signup_password.ERROR_MESSAGE_ENTER_PASSWORD_PT)

    @allure.step('Получаем текст ошибки под полем "Повторите пароль"')
    def find_error_message_repeat_password(self, language):
        if language == 'en':
            self.wait_visible_element(
                signup_password.ERROR_MESSAGE_REPEAT_PASSWORD_EN)
            return self.get_text_element(signup_password.ERROR_MESSAGE_REPEAT_PASSWORD_EN)
        elif language == 'ru':
            self.wait_visible_element(
                signup_password.ERROR_MESSAGE_REPEAT_PASSWORD_RU)
            return self.get_text_element(signup_password.ERROR_MESSAGE_REPEAT_PASSWORD_RU)
        elif language == 'pt':
            self.wait_visible_element(
                signup_password.ERROR_MESSAGE_REPEAT_PASSWORD_PT)
            return self.get_text_element(signup_password.ERROR_MESSAGE_REPEAT_PASSWORD_PT)

    @allure.step('Находим заголовок страницы ввода кода подтверждения ')
    def find_title_verification_code_page(self, language):
        if language == 'en':
            self.wait_visible_element(
                signup_password.VERIFICATION_CODE_TITLE_EN)
            return self.find_element(signup_password.VERIFICATION_CODE_TITLE_EN)
        elif language == 'ru':
            self.wait_visible_element(
                signup_password.VERIFICATION_CODE_TITLE_RU)
            return self.find_element(signup_password.VERIFICATION_CODE_TITLE_RU)
        elif language == 'pt':
            self.wait_visible_element(
                signup_password.VERIFICATION_CODE_TITLE_PT)
            return self.find_element(signup_password.VERIFICATION_CODE_TITLE_PT)


    @allure.step('Находим поле email и ввести {email}')
    def find_email_field_and_type_text(self, email):
        self.wait_visible_element(signup_password.SIGNIN_EMAIL_FIELD)
        self.type_text(signup_password.SIGNIN_EMAIL_FIELD, email)

    @allure.step('Нажимаем на кнопку "Продолжить"')
    def click_continue_button(self, language):
        if language == 'en':
            self.click_element(signup_password.CONTINUE_BUTTON_EN)
        elif language == 'ru':
            self.click_element(signup_password.CONTINUE_BUTTON_RU)
        elif language == 'pt':
            self.click_element(signup_password.CONTINUE_BUTTON_PT)

    @allure.step('Ожидаем смены ссылки verification_code {url}')
    def wait_verification_code_url_to_be(self, url):
        self.wait_url_to_be(url)

    def wait_signup_url_to_be(self, url):
        self.wait_url_to_be(url)
