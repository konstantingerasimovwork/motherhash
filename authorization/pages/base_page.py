from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class BasePage():

    def __init__(self, browser):
        self.browser = browser

    def find_element(self, locator):
        return self.browser.find_element(*locator)

    def find_elements(self, locator):
        return self.browser.find_elements(*locator)

    def click_element(self, locator):
        self.find_element(locator).click()

    def type_text(self, locator, text):
        self.find_element(locator).send_keys(text)

    def wait_visible_element(self, locator):
        WebDriverWait(self.browser, 5).until(expected_conditions.visibility_of_element_located(locator))

    def get_title(self):
        return self.browser.title

    def wait_url_changes(self, url):
        WebDriverWait(self.browser, 5).until(expected_conditions.url_changes(url))

    def wait_url_to_be(self, url):
        WebDriverWait(self.browser, 5).until(
            expected_conditions.url_to_be(url))

    def get_text_element(self, locator):
        return self.find_element(locator).text
    
    def get_current_url(self):
        return self.browser.current_url