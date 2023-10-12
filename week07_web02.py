from bs4 import BeautifulSoup

html = """
<html>
<head>
<title>스크레이핑 실습</title>
</head>
<body>
<h1>대림대학교</h1>
<p>웹 스크레이핑</p>
<p>파이썬 기본 문법, 넘파이, 판다스, 맷플롯립, 사이킷런, GUI ... </p>
</body>
</html>
"""
soup = BeautifulSoup(html, 'html.parser')
t = soup.html.head.title
h1 = soup.html.body.h1.string
p1 = soup.html.body.p
p2 = p1.next_sibling.next_sibling
print(t, h1, p1, p2)