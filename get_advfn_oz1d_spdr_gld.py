#!/usr/bin/env python
# coding: utf-8
import base64
import datetime
import os
import random
import time

import pandas as pd
import requests
from dotenv import find_dotenv, load_dotenv

from converte_datetime_pt import parse_pt_date

load_dotenv(find_dotenv())


def load_useragents():
    uas = []
    with open("user-agents.txt", 'rb') as uaf:
        for ua in uaf.readlines():
            if ua:
                uas.append(ua.strip()[0:-1-0])
    random.shuffle(uas)
    return uas


def get_magic_cookies():
    __urls__ = {'url_login': 'https://secure.advfn.com/login/secure'}

    payload = {
        'redirect_url': base64.b64encode(b'https://br.advfn.com'),
        'site': 'br',
        'login_username': os.environ.get('ADVFN_USERNAME'),
        'login_password': os.environ.get('ADVFN_PASSWORD')
    }

    headers = {'User-Agent': random.choice(load_useragents())}

    _req = requests.post(__urls__['url_login'], data=payload, headers=headers)

    account_login = _req.history[0].headers['location']
    # Request for get SID values in content
    req_gsv = requests.get(account_login)

    return req_gsv.history[0].cookies


# url base advfn
url_base = 'https://br.advfn.com/bolsa-de-valores'

# dados do ADFN - OZ1
ticker = 'OZ1D'
url = f"{url_base}/bmf/{'OZ1D'}/historico/mais-dados-historicos"
response = requests.get(url, cookies=get_magic_cookies())

# transforma o response recebido num dataframe pandas
df = pd.read_html(response.text, decimal=',', thousands='.')[1]
df['Fechamento'] = df['Fechamento'].round(2)
df['Data'] = df['Data'].apply(lambda x: parse_pt_date(x))
df['ticker'] = ticker
print(df.head())


# dados do ADFN - GLD
ticker = 'GLD'
url = f"{url_base}/amex/{ticker}/historico/mais-dados-historicos"
response = requests.get(url, cookies=get_magic_cookies())

# transforma o response recebido num dataframe pandas
df = pd.read_html(response.text, decimal=',', thousands='.')[1]
df['Fechamento'] = df['Fechamento'].round(2)
df['Data'] = df['Data'].apply(lambda x: parse_pt_date(x))
df['ticker'] = ticker
print(df.head())
