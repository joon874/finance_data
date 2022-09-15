from email import header
import requests
from bs4 import BeautifulSoup
import json
import os
import sys

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'}
url = 'https://finance.yahoo.com/quote/AAPL?p'

r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')

print(soup.title.text)

title = soup.find('h1', {'class': 'D(ib) Fz(18px)'}).text
print(title)

closed_price = soup.find('fin-streamer', {'class': 'Fw(b) Fz(36px) Mb(-4px) D(ib)'}).text
print(closed_price)

data = {'title':title, 'price':closed_price}

with open(os.path.join(BASE_DIR, 'stock.json'), 'w+',encoding='utf-8') as json_file:
    json.dump(data, json_file, ensure_ascii = False, indent='\t')



