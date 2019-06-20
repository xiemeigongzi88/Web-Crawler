demo='http://python123.io/ws/demo.html'

from bs4 import BeautifulSoup

soup=BeautifulSoup(demo,'html.parser')
soup.prettify()

print(soup.prettify())


from bs4 import BeautifulSoup
soup=BeautifulSoup(demo,"html.parser") # html 解析器 parser 
print(soup.prettify())

print(soup.a.prettify())


soup1=BeautifulSoup('<p>中文</p>','html.parser')
soup1.p.string

print(soup1.p.prettify())