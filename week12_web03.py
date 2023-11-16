import urllib.request
from bs4 import BeautifulSoup
import pandas as pd
import datetime

shops = list()

for i in range(1, 52):
    url = f"https://www.hollys.co.kr/store/korea/korStore2.do?pageNo={i}&sido=&gugun=&store="
    print(url)
    page = urllib.request.urlopen(url)
    soup = BeautifulSoup(page, "html.parser")
    tbody = soup.find('tbody')
    trs = tbody.find_all('tr')

    for tr in trs:
        tds = tr.find_all('td')
        shop_name = tds[1].string  # 매장명
        shop_addr = tds[3].string  # 주소
        shop_phone = tds[5].string  # 전화번호

        shops.append([shop_name]+[shop_addr]+[shop_phone]+[datetime.datetime.now()])  # 2d list

# print(shops)
hollys_df = pd.DataFrame(shops, columns=('매장명', '주소', 'Tel', '일시'))
hollys_df.to_csv('holly.csv', mode='w', encoding='cp949')
