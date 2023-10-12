import urllib.request

url = 'https://www.daelim.ac.kr/type/KOR_A/img/intro/logo.png'
urllib.request.urlretrieve(url, 'daelim.png')
print('저장완료')