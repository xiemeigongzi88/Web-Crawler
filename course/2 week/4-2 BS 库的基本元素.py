
from bs4 import BeautifulSoup
soup=BeautifulSoup(demo,'html.parser')
soup.title

tag=soup.a  # 只返回第一个标签 
tag

# 获得标签的名字
soup.a.name
print(soup.a.name)
# a 父标签的名字
soup.a.parent.name

soup.a.parent.parent.name

tag=soup.a
tag.attrs

tag.attrs['class']

# 链接属性
tag.attrs['href']

# 标签属性的类型 
type(tag.attrs)

# 标签类型
type(tag)

# 查看字符串信息 
soup.a

soup.a.string 

soup.p

soup.p.string 

# comment 

newsoup=BeautifulSoup('<b><!--This is a comment--></b><p>This is not a comment</p>','html.parser')
newsoup.b.string 
print(type(newsoup.b.string))

newsoup.p.string 
print(type(newsoup.p.string))


