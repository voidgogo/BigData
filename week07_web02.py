import urllib.request
from bs4 import BeautifulSoup

api = 'https://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp'
urls = urllib.request.urlopen(api).read()
soup = BeautifulSoup(urls, 'html.parser')

cities = soup.find_all("city")
wfs = soup.find_all("wf")
wfs.pop(0)  # 성능 이슈 있을 수 있음

for i in range(len(cities)):
    print(f'{cities[i].string}의 날씨는 {wfs[i*13].string}입니다.')

print(len(cities), len(wfs))