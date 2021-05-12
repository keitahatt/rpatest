import requests
from bs4 import BeautifulSoup
url = 'https://news.yahoo.co.jp'
res = requests.get(url)
soup = BeautifulSoup(res.text, 'html.parser')
# title_text = soup.find_all( 'a',class_="sc-esjQYD")
contents = soup.find_all('a', class_="sc-esjQYD")
print('-------------------------')
print('-------------------------')
print('-------------------------')
print('-------------------------')
# print(contents)
for w in contents:
    print(w.get_text())
# print(title_text)
print('-------------------------')
print('-------------------------')
print('-------------------------')
print('-------------------------')