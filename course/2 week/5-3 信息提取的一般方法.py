from bs4 import BeautifulSoup

from urllib import urlopen

import urllib.request
#resp=urllib.request.urlopen('http://www.baidu.com')

demo='http://python123.io/ws/demo.html'

soup=BeautifulSoup(urllib.request.urlopen(demo),"html.parser")
print(soup.prettify())

# another way to deal with demo
import requests

url="http://www.baidu.com"
demo=requests.get(url)
demo=r.text

from bs4 import BeautifulSoup
soup=BeautifulSoup(demo,'html.parser')

soup.find_all('a')

# 同时查找 a b 标签
soup.find_all(['a','b'])

# 所有标签 和所有便签的名称
for tag in soup.find_all(True):
    print(tag)
    print("###############")
    print(tag.name)

# 只显示 以 b 开头的标签
import re
for tag in soup.find_all(re.compile('b')):
    print(tag.name)

# 查找属性的部分信息
# 查找 p 标签中 包含  course 字符串的信息
soup.find_all('p','course')

# 查找 特定属性 即 对属性做约定 ru id=link 1

soup.find_all(id='link1')

soup.find_all(id='link')

# 查找包含 link 的所有信息
import re
soup.find_all(id=re.compile('link'))


soup.find_all('a')

soup.find_all('a',recursive=False)


# 检索所有 包含 python 的字符串
soup.find_all(string=re.compile('python'))