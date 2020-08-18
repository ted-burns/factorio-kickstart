import keyring
from getpass import getpass
import requests

SYSTEM_NAME = "digital-ocean-scripts"
USER_NAME = "bearer"

class BearerAuth(requests.auth.AuthBase):
    def __init__(self, token):
        self.token = token
    def __call__(self, r):
        r.headers["authorization"] = "Bearer " + self.token
        return r

def get_token():
    token = keyring.get_password(SYSTEM_NAME, USER_NAME)
    if token is None:
        token = getpass("Enter bearer token: ")
        keyring.set_password(SYSTEM_NAME, USER_NAME, token)
    return token

def delete_token():
    keyring.delete_password(SYSTEM_NAME, USER_NAME)

def get_auth():
    return BearerAuth(get_token())