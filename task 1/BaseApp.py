from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://test-stand.gb.ru"

    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                        message=f"Cant find element by locator {locator}")


    def get_element_property(self, locator, property):
        element = self.find_element(locator)
        return element.value_of_css_property(property)


    def go_to_site(self):
        return self.driver.get(self.base_url)

    def enter_text_into_field(self, locator, word):
        field = self.find_element(locator)
        field.clear()
        field.send_keys(word)


    def click_button(self, locator):
        button = self.find_element(locator)
        button.click()

    def get_text_from_element(self, locator):
        return WebDriverWait(self.driver).until(EC.presence_of_element_located(locator),
                                    message=f"Cant find element by locator {locator}")

