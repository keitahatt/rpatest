from bs4.element import Comment
import requests
import glob
from bs4 import BeautifulSoup
import re
from selenium import webdriver
import MySQLdb

# データベースへの接続とカーソルの生成
connection = MySQLdb.connect(
    host='localhost',
    user='root',
    passwd='tkvip24week',
    db='pytest',
# テーブル内部で日本語を扱うために追加
    charset='utf8'
)

cursor = connection.cursor()

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

tmp_num = 1

for w in contents:
    titles.append(w.get_text())
    ul.append(w.get('href'))

#for a,b in zip(titles,ul):
#    cursor.execute("INSERT INTO rpa_data VALUES (?,?);",(a,b))


for a,b in zip(titles, ul):
    cursor.execute("INSERT INTO rpa_data(title,url) VALUES(%s,%s);",(a,b))
#cursor.executemany("INSERT INTO rpa_data(title) VALUES (%s,%s)", titles)
#cursor.executemany("INSERT INTO rpa_data(url) VALUES (%s)", ul)
# 保存を実行

connection.commit()

# 一覧の表示

# 接続を閉じる
connection.close()

