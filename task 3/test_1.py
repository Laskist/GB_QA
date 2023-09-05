import requests
import yaml

with open("config.yaml") as f:
    data = yaml.safe_load(f)


def one_username(get_token_auth):
    header = {
        "X-Auth-Token": get_token_auth["token"]
    }
    # con = requests.get(url=(data["url_api"] + str(get_token_auth["id"])), headers=header)
    # assert get_token_auth["username"] == con.json()["username"], "not created"
    con = requests.get(url=(data["url_api"] + str(get_token_auth["id"])), headers=header)
    return con.json()["username"]

print(one_username(get_token_auth))
