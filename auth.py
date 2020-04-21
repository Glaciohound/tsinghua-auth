import yaml
import requests
import hashlib
from argparse import ArgumentParser
import getpass


login_url = "http://net.tsinghua.edu.cn/do_login.php"
user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1)" \
    " AppleWebKit/537.36 (KHTML, like Gecko) Chrome/" \
    "54.0.2840.98 Safari/537.36"


def load_config(path="config/account.yaml"):
    with open(path) as f:
        config = yaml.load(f)
        username = config["account"]["username"]
        password = config["account"]["password"]

        return username, password


def hex_md5_password(password):
    password = hashlib.md5(password.encode('utf-8')).hexdigest()
    return "{MD5_HEX}%s" % password


def try_connections():
    try:
        res = requests.get("http://www.baidu.com")
    except requests.HTTPError:
        return False
    return res.status_code == 200


def go_online():
    '''
    username, password = load_config()
    '''
    username = input("username: ")
    password = getpass.getpass()
    param = {
        "action": "login",
        "username": username,
        "password": hex_md5_password(password),
        "ac_id": 1
    }
    res = requests.post(login_url, param)
    if res.status_code != 200:
        return False
    else:
        return True


def check_online():
    param = {
        "action": "check_online",
        "ac_id": 1
    }
    res = requests.post(login_url, param)
    return res.text


def go_offline():
    param = {
        "action": "logout",
        "ac_id": 1
    }
    res = requests.post(login_url, param)
    if res.status_code != 200:
        return False
    else:
        return True


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument("--connect", action='store_true')
    parser.add_argument("--disconnect", action='store_true')
    parser.add_argument("--check", action='store_true')
    args = parser.parse_args()

    if args.connect:
        go_online()
        print(check_online())
    elif args.disconnect:
        go_offline()
        print(check_online())
    elif args.check:
        print(check_online())
    else:
        print("Please specify the action from `--connect`'\
        ' `--check` and `--disconnect`")
