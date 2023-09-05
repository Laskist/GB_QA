from BaseApp import BasePage
from selenium.webdriver.common.by import By
import yaml

class ContactLocators:
    ids = dict()
    with open('locators.yaml') as f:
        locators = yaml.safe_load(f)
    for locator in locators['xpath'].keys():
        ids[locator] = (By.XPATH, locators['xpath'][locator])
    for locator in locators['css'].keys():
        ids[locator] = (By.CSS_SELECTOR, locators['css'][locator])

class OperationsContact(BasePage):
    def click_about_button(self):
        self.find_element(ContactLocators.ids["LOCATOR_ABOUT_BTN"]).click()

    def check_about_page(self):
        check_title_about_page = self.find_element(ContactLocators.ids["LOCATOR_ABOUT_PAGE"])
        return check_title_about_page


