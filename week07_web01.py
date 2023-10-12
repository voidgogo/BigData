import urllib.request
import urllib.parse

api = 'https://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp'

station_id = input('지역코드 : ')  # 전국 108, 수도권 109, 강원 105, 제주 184 ....
values = {'stnId': station_id}
parameters = urllib.parse.urlencode(values)
url = api + '?' + parameters  # api string + ? + stnId=station_id
# print(url)

urls = urllib.request.urlopen(url).read()
texts = urls.decode('utf-8')
print(texts)
