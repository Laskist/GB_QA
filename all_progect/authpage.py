from BaseApp import BasePage
from selenium.webdriver.common.by import By
import yaml


class TestSearchLocators:
    ids = dict()
    with open('locators.yaml') as f:
        locators = yaml.safe_load(f)

    for locator in locators['xpath'].keys():
        ids[locator] = (By.XPATH, locators['xpath'][locator])

    for locator in locators['css'].keys():
        ids[locator] = (By.CSS_SELECTOR, locators['css'][locator])


class OperationsHelper(BasePage):
    def enter_login(self, word):
        return self.enter_text_into_field(TestSearchLocators.ids["LOCATOR_LOGIN_FIELD"], word, description="login form")

    def enter_pass(self, word):
        return self.enter_text_into_field(TestSearchLocators.ids["LOCATOR_PASSWORD_FIELD"], word,
                                          description="password form")

    def click_login_button(self):
        return self.click_button(TestSearchLocators.ids["LOCATOR_LOGIN_BTN"], description="button login")

    def get_auth_text(self):
        auth_check = self.find_element(TestSearchLocators.ids["LOCATOR_AUTH_FIELD"], time=3)
        return auth_check.text


