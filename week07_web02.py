from bs4 import BeautifulSoup

html = """
<html>
<head>
<title>스크레이핑 실습</title>
</head>
<body>
<a href="http://www.daelim.ac.kr">대림대학교</a><br>
<a href="http://www.harvard.edu">하버드대학교</a>
</body>
</html>
"""
soup = BeautifulSoup(html, 'html.parser')
urls = soup.find_all("a")
print(urls)
for url in urls:
    print(f'{url.string}의 url주소는 {url.attrs["href"]}입니다.')
    # univ = url.string
    # link = url.attrs['href']
    # print(univ)
    # print(link)