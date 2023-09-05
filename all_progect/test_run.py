from authpage import OperationsHelper
from aboutpage import OperationsContact
import yaml
import time
import requests

with open("config.yaml") as f:
    testdata = yaml.safe_load(f)
    username = testdata["login"]
    password = testdata["password"]
    url_api = testdata["url_api"]



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


def test_one_username(get_token_auth):
    header = {
        "X-Auth-Token": get_token_auth["token"]
    }
    con = requests.get(url=(url_api + str(get_token_auth["id"])), headers=header)
    assert get_token_auth["username"] == con.json()["username"], "not created"
