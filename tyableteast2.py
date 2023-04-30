from bs4 import BeautifulSoup , NavigableString
import requests
import csv
import pandas as pd

source = requests.get('https://www.merinolaminates.com/en/design/10002-mangfall-beech/?cat=65')
soup = BeautifulSoup(source.content, 'lxml')


dfs = pd.read_html(source.text)
print(dfs)