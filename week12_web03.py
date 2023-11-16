from bs4 import BeautifulSoup

html = """
<html>
<head>
<title>스크레이핑 실습</title>
</head>
<body>
<h1 id="univ">대림대학교</h1>
<p>웹스크레이핑</p>
<p id="contents">파이썬, 판다스, 넘파이, 맷플롯립, GUI...</p>
</body>
</html>
"""
soup = BeautifulSoup(html, 'html.parser')
university = soup.find(id='univ')
contents = soup.find(id='contents')

print(university)
print(contents.string)
print(contents)
