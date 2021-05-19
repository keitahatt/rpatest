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

# データの追加
cursor.execute("""INSERT INTO rpa_data (title, url)
    VALUES ('ナダルのハメ撮り', 'hdsgdkdkfofjfsl;'),
    ('で。あります', 'jkufhshdreiloldsilejh'),
    ('おいしい水富士山', 'hdo')
    """)

# 一覧の表示
cursor.execute("SELECT * FROM rpa_data")

for row in cursor:
    print(row)

# 保存を実行
connection.commit()

# 接続を閉じる
connection.close()