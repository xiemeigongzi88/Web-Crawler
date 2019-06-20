import requests

r=requests.get('http://python123.io/ws/demo.html')
print(r.text)

demo=r.text

# 测试 bs
from bs4 import BeautifulSoup
soup=BeautifulSoup(demo,"html.parser") # html 解析器 parser 
print(soup.prettify())