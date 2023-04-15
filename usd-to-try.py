import requests
from bs4 import BeautifulSoup

html_text = requests.get('https://www.google.com/search?channel=fs&client=ubuntu-sn&q=usd+to+try').text
soup = BeautifulSoup(html_text, 'lxml')
money = soup.find_all('span')

print(money[22].text + ' turkish liras')