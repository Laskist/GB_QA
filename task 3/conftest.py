import pytest
import requests
import yaml

with open("config.yaml") as f:
    data = yaml.safe_load(f)


# @pytest.fixture()
def get_token_auth():
    params = {
        "username": data["username"],
        "password": data["password"]
    }
    r = requests.post(url=data["url"], data=params)
    return r.json()

def one_username():
    header = {
        "X-Auth-Token": get_token_auth()["token"]
    }
    # con = requests.get(url=(data["url_api"] + str(get_token_auth["id"])), headers=header)
    # assert get_token_auth["username"] == con.json()["username"], "not created"
    con = requests.get(url=(data["url_api"] + str(get_token_auth()["id"])), headers=header)
    return con.json()

print(one_username())
