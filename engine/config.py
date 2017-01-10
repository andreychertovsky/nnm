# https://hh.ru/oauth/authorize?response_type=code&client_id={client_id}&state={state}&redirect_uri={redirect_uri}
# https://hh.ru/oauth/token?grant_type=authorization_code&client_id={client_id}&client_secret={client_secret}&code={authorization_code}&redirect_uri={redirect_uri}

config = {
    "app": {
        "clientID":"KP0E202GQ0O6DQ07VD2N6QMAATMTA1FUUL4S2AEIPRC84LG592T56E2J5KGUDQ0V",
        "clientSecret":"J42GPFV64RBHPBUSN17B0Q30H5MCSD950PGMK238GG156805JC8S7DFUID4I6FG7",
        "redirectUri":"http://195.46.163.240/token"
    },
    "test":{
        "login":"vv.email27@gmail.com",
        "pass":"fyfkmuby51",
        "login2":"andreychertovsky88@gmail.com",
        "pass2":"fyfkmuby51-15",
        "login3":"afdwefsdffdsgdsfdfsg@mail.ru",
        "pass3":"fyfkmuby51"
    },
    "data":{
        "urlCode":"https://hh.ru/oauth/authorize?response_type=code&client_id=",
        "urlToken":"https://hh.ru/oauth/token?grant_type=authorization_code&client_id=",
        "urlMobile":'https://m.hh.ru/account/login',
        "urlCodeGrant":"https://hh.ru/oauth/authorize?redirect_uri="
    }
}
