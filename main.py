import requests, json, random
from pprint import pprint
usernames = ["Anitta", "Xurrasco"]
proxy = "http://username:password@PROXY_SERVER:PORT"
output = {}
def get_headers(username):
    headers = {
        "authority": "www.instagram.com",
        "method": "GET",
        "path": "/{0}/".format(username),
        "scheme": "https",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "en-GB, en-US;q=0.9,en;q=0.8",
        "upgrade-insecure-requests": "1",
        "Connection": "close",
        "user-agent" : random.choice([
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.80 Safari/537.36",
            "Mozilla/5.0 (Windows NT 10.0; Win64; X64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36",
            "Mozilla/5.0 (Windows NT 6.1; Win64; X64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"
            "Mozilla/5.0 (Windows NT 10.0; Win64; X64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"
            "Mozilla/5.0 (Windows NT 10.0; Win64; X64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"
            "Mozilla/5.0 (Windows NT 6.1; Win64; X64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"
        ])
    }
    return headers
def main():
    for username in usernames:
        url = f"https://www.instagram.com/{username}/?__a=1&__d=dis"
        response = requests.get(url, headers=get_headers(username), proxies = {'http': proxy, 'https': proxy})
        if response.status_code == 200:
            try:
                resp_json = json.loads(response.text)
            except:
                print ("NAO FUNCIONOU CARALHO")
                continue
            else:
                user_data = resp_json[]
if __name__ == '__main__':
    main()
    pprint(output)