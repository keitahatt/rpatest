from bs4.element import Comment
import requests
import glob
from bs4 import BeautifulSoup
import re
from selenium import webdriver

driver = webdriver.Chrome("C:/Users/原敬太/Documents/python_test/chromedriver")
url = 'https://news.yahoo.co.jp/categories/sports/'
driver.get(url)
#ドライバーを閉じる
driver.quit()

response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")
elems = soup.find_all(href=re.compile("news.yahoo.co.jp/categories/sports/pickup"))
contents = soup.find_all('a', class_="sc-esjQYD")

titles = []
ul = []


for w in contents:
     titles.append(w.get_text())
     titles.append(w.get('href'))
    #titles.format(w.get_text(), w.get('href'))
   # ul.append(w.get('href')) 

print(titles)