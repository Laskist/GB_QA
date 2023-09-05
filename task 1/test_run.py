from authpage import OperationsHelper
from aboutpage import OperationsContact
import yaml
import time


with open("config.yaml") as f:
    testdata = yaml.safe_load(f)
    username = testdata["login"]
    password = testdata["password"]



def test_auth(browser):
    testpage = OperationsHelper(browser)
    testpage.go_to_site()
    testpage.enter_login(username)
    testpage.enter_pass(password)
    testpage.click_login_button()
    assert testpage.get_auth_text() == f"Hello, {username}"


def test_about(browser):
    testpage = OperationsContact(browser)
    testpage.click_about_button()
    time.sleep(1)
    assert testpage.check_about_page().text == "About Page"


def test_about_font_size(browser):
    testpage = OperationsContact(browser)
    testpage.click_about_button()
    time.sleep(1)
    assert testpage.check_about_page().value_of_css_property("font-size") == "32px"


