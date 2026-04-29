import requests
from bs4 import BeautifulSoup
import csv
import datetime

# 実行日時を記録
今日 = datetime.datetime.now().strftime("%Y年%m月%d日 %H時%M分")
print(今日 + "実行開始")

# 日付ごとにファイルを保存
ファイル名 = datetime.datetime.now().strftime("%Y%m%d") + "_books.csv"

# CSVファイルを準備
with open(ファイル名, "w", newline="", encoding="utf-8-sig") as f: # Excelの場合は-sigをつける
    writer = csv.writer(f) # csvに書き込む命令
    writer.writerow(["タイトル", "価格"]) # ヘッダー行

    # 1ページ目から5ページ目まで巡回
    for page in range(1, 6):
        print(str(page) + "ページ目を取得中...")

        # 1ページ目だけURLが違う
        if page == 1:
            url = "http://books.toscrape.com/"
        else:
            url = "http://books.toscrape.com/catalogue/page-" + str(page) + ".html"
    
        response = requests.get(url) # サイトの情報を取得
        response.encoding = "utf-8" # 日本語が文字化けしないようにする設定
        soup = BeautifulSoup(response.text, "html.parser")

        # 本のタイトルと価格を取得
        titles = soup.find_all("h3")
        prices = soup.find_all("p", class_="price_color")

        for title, price in zip(titles, prices): # zip()は２つのリストを同時に取り出す命令
            writer.writerow([title.text.strip(), price.text.strip()]) # .stripは文字列の前後の余計なスペースや改行を取り除く命令

print(ファイル名 + "に保存しました！")