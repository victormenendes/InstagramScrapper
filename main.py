import requests, json, random
from pprint import pprint
usernames = ["Anitta", "Xurrasco"]
proxy = "http://username:password@PROXY_SERVER:PORT"
output = {}
def get_headers(username):
    headers = {
        "authority"
    }