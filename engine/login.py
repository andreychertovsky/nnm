from config import *
import requests
import re
import json

def stringSplit(codeURL):
    try:
        return codeURL.split('token?code=')[1]
    except IndexError as e:
        return 0

URLMOBILE   = config['data']['urlMobile']
URL         = config['data']['urlCode']+config['app']['clientID']+"&redirect_uri="+config['app']['redirectUri']
URLCODE     = config['data']['urlCodeGrant']+config['app']['redirectUri']+'&response_type=code&client_id='+config['app']['clientID']

headers ={
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:49.0) Gecko/20100101 Firefox/49.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate, br'
}

headersToken = {
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:49.0) Gecko/20100101 Firefox/49.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate, br',
        "Content-Type":"application/x-www-form-urlencoded"
}

def obtainCode():
    s = requests.Session()

    setCookie   = s.get(URLMOBILE, headers=headers)
    loginPost = {
        '_xsrf':setCookie.cookies.get('_xsrf', domain='.hh.ru'),
        'username':config['test']['login'],
        'password':config['test']['pass'],
        'backUrl':'https://m.hh.ru',
        'failUrl':'/account/login?backurl=/'
    }

    loginGrant = {
        '_xsrf':setCookie.cookies.get('_xsrf', domain='.hh.ru'),
        'grant': '1',
        'redirect_uri':config['app']['redirectUri']
    }
    loginMobile = s.post(URLMOBILE, headers=headers, params=loginPost)
    getCode     = s.get(URL, headers=headers)
    return stringSplit(getCode.url)
    match = re.search(r'\grant\b', getCode.text)
    if match:
        getCodeGrant = s.post(URLCODE, headers=headers, params=loginGrant)
        return stringSplit(getCodeGrant.url)

def obtainToken():
    code = obtainCode()
    print(code)
    dataToken = {
        "grant_type":"authorization_code",
        "client_id":config['app']['clientID'],
        "client_secret":config['app']['clientSecret'],
        "code":code,
        "redirect_uri":config['app']['redirectUri']
    }
    getToken = requests.post('https://hh.ru/oauth/token', headers=headersToken, data=dataToken)
    print(getToken.json())

if __name__ == '__main__':
    #obtainCode()
    obtainToken()
