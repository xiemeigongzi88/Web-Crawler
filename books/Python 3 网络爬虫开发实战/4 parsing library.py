# -*- coding: utf-8 -*-
"""
Created on Thu Jan 17 00:00:00 2019

@author: sxw17
"""

4 parsing library 

page 158 (169) 

'''
https://zhuanlan.zhihu.com/p/29436838
'''



4.1 使用 XPath 
XPath 做响应的信息抽取 

4. 实例引入 
from lxml import etree 

text='''
<div>
<url>
<li class="item-0"><a href="link1.html">first item</a></li>
<li class="item-1"><a href="link2.html">second item</a></li>
<li class="item-inactive"><a href="link1.html">third item</a></li>
<li class="item-1"><a href="link4.html">fourth item</a></li>
<li class="item-0"><a href="link5.html">fifth item</a>
# 没有 </li>闭合 但是 etree module 可以自动修正 
</url>
</div>
'''

html=etree.HTML(text)
# HTML 类 可以对 text 文本初始化 构造一个 XPath 解析对象 
result=etree.tostring(html)
# tostring() 可以输出修正后的 HTML 代码 
print(result.decode('utf-8'))


也可以直接读取文本文件进行解析 


from lxml import etree
 
html = etree.parse('./test.html', etree.HTMLParser())
result = etree.tostring(html)
print(result.decode('utf-8'))



text='''
<div>
<url>
<li class="item-0"><a href="link1.html">first item</a></li>
<li class="item-1"><a href="link2.html">second item</a></li>
<li class="item-inactive"><a href="link1.html">third item</a></li>
<li class="item-1"><a href="link4.html">fourth item</a></li>
<li class="item-0"><a href="link5.html">fifth item</a>
</url>
</div>
'''


from lxml import etree 
html=etree.parse(text,etree.HTMLParser())
result=etree.tostring(html)
print(result.decode('utf-8'))




################################################
# correct 这个版本为  正确的  能出来结果 
from lxml import etree
file= "C:\\Users\\sxw17\\Desktop\\scrapy\\Note\\python_3 Web crawler development\\test.html"
html = etree.parse(file, etree.HTMLParser())
result = etree.tostring(html)
print(result.decode('utf8'))



5. 所有节点 
from lxml import etree
file= "C:\\Users\\sxw17\\Desktop\\scrapy\\Note\\python_3 Web crawler development\\test.html"
html = etree.parse(file, etree.HTMLParser())
result=html.xpath('//*')
print(result) # 返回的是 列表  


想获得所有 li  节点 
from lxml import etree 

file= "C:\\Users\\sxw17\\Desktop\\scrapy\\Note\\python_3 Web crawler development\\test.html"
html=etree.parse(file,etree.HTMLParser())
result=html.xpath('//li')
print(result)
print(result[0])


6. 子节点 
file= "C:\\Users\\sxw17\\Desktop\\scrapy\\Note\\python_3 Web crawler development\\test.html"
html=etree.parse(file,etree.HTMLParser())
result=html.xpath('//li/a')
print(result)


7. 父节点 
// 从当前节点选区子孙节点
/ 从当前节点选区直接子节点
@ 选取属性
。  选取当前节点
。。 选取当前节点的父节点  

<html><body><div>
<url>
<li class="item-0"><a href="link1.html">first item</a></li>
<li class="item-1"><a href="link2.html">second item</a></li>
<li class="item-inactive"><a href="link1.html">third item</a></li>
<li class="item-1"><a href="link4.html">fourth item</a></li>
<li class="item-0"><a href="link5.html">fifth item</a>
# &#27809;&#26377; </li>&#38381;&#21512; &#20294;&#26159; etree module &#21487;&#20197;&#33258;&#21160;&#20462;&#27491; 
</url>
</div>
</body></html>

    
file= "C:\\Users\\sxw17\\Desktop\\scrapy\\Note\\python_3 Web crawler development\\test.html"
html=etree.parse(file,etree.HTMLParser())
print(html.xpath('//*'))

result=html.xpath('//a[@href="link4.html"]/../@class')
print(result)




8. 属性匹配

<html><body><div>
<url>
<li class="item-0"><a href="link1.html">first item</a></li>
<li class="item-1"><a href="link2.html">second item</a></li>
<li class="item-inactive"><a href="link1.html">third item</a></li>
<li class="item-1"><a href="link4.html">fourth item</a></li>
<li class="item-0"><a href="link5.html">fifth item</a>
# &#27809;&#26377; </li>&#38381;&#21512; &#20294;&#26159; etree module &#21487;&#20197;&#33258;&#21160;&#20462;&#27491; 
</url>
</div>
</body></html>


from lxml import etree 

file= "C:\\Users\\sxw17\\Desktop\\scrapy\\Note\\python_3 Web crawler development\\test.html"
html=etree.parse(file,etree.HTMLParser())
result=html.xpath('//li[@class="item-0"]')
print(result)


9. 文本获取 
from lxml import etree 

file= "C:\\Users\\sxw17\\Desktop\\scrapy\\Note\\python_3 Web crawler development\\test.html"
html=etree.parse(file,etree.HTMLParser())
result=html.xpath('//li[@class="item-0"]/text()')
print(result)






4.2 Beautiful Soup 
page 168(179)
如果使用 lxml 初始化 bs 可以把第二个参数 改为 lxml


3. 解析器
from bs4 import BeautifulSoup 
soup=BeautifulSoup('<p>Hello</p>','lxml')
print(soup.p.string) 



4. 基本用法 

html = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""

from bs4 import BeautifulSoup
soup=BeautifulSoup(html,'lxml')
print(soup.prettify())
# 格式化代码 自动补全代码 
print(soup.title.string)


选择元素
html = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""

from bs4 import BeautifulSoup 
soup=BeautifulSoup(html,'lxml')
print(soup.title)
print(type(soup.title))
print(soup.title.string)
print(soup.head)
print(soup.p)


html = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""

提取信息 
（1） 获取节点名称 
print(soup.title.name)

（2） 获取属性 

print(soup.p.attrs)
print(soup.p.attrs['name'])

print(soup.p['name'])
print(soup.p['class'])


(3) 获取内容 
print(soup.p.string)


嵌套选择
html = """
<html><head><title>The Dormouse's story</title></head>
<body>
"""
from bs4 import BeautifulSoup
soup=BeautifulSoup(html,'lxml')
print(soup.head.title)
print(type(soup.head.title))
print(soup.head.title.string)


关联选择
（1） 子节点和子孙节点 
html = """
<html>
    <head>
        <title>The Dormouse's story</title>
    </head>
    <body>
        <p class="story">
            Once upon a time there were three little sisters; and their names were
            <a href="http://example.com/elsie" class="sister" id="link1">
                <span>Elsie</span>
            </a>
            <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> 
            and
            <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>
            and they lived at the bottom of a well.
        </p>
        <p class="story">...</p>
"""

from bs4 import BeautifulSoup
soup=BeautifulSoup(html,'lxml')
print(soup.p.contents)


soup=BeautifulSoup(html,'lxml')
print(soup.p.children)

for i, child in enumerate(soup.p.children):
    print(i,child)












