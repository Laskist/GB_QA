from use_nikto import checkout
import yaml

with open('config.yaml') as f:
    data = yaml.safe_load(f)


def test_step1():
    res = checkout("nikto -h {} -ssl -Tuning 4".format(data["address"]), "0 error(s)")
    assert res, 'test1 fail'