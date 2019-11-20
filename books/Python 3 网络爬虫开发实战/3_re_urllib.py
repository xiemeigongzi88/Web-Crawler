# -*- coding: utf-8 -*-
"""
Created on Mon Jan 14 12:29:40 2019

@author: sxw17
"""

'''
# 3 基本库的使用 
page 102- 113 

3.1 使用 urllib 

request 
error 
parse
robotparser 

'''

'''
3.1.1 发送请求
'''

1. urlopen()

import urllib.request

response=urllib.request.urlopen('http://www.python.org')
print(response.read().decode('utf-8'))


利用 type() 方法输出响应的类型：

import urllib.request

response=urllib.request.urlopen('https://www.python.org')
print(type(response))



调用 read() 方法可以得到返回的网页内容 
调用 status 属性 可以得到返回结果的 状态码 

import urllib.request

response=urllib.request.urlopen('https://www.python.org')

print(response.status)
print(response.getheaders())
print(response.getheader('Server')) 


如何给 链接传递一些参数？？？
urlopen() API 

urllib.request.urlopen(url, data=None, [timeout, ]*, cafile=None, capath=None, cadefault=False, context=None)¶

data 参数 
如果传递了这个参数 则请求方式不是 get 而是 post  
以表单提交的方式 以 post 方式传输数据  

import urllib.parse
import urllib.request

data=bytes(urllib.parse.urlencode({'word':'hello'}),encoding='utf-8')
#把字典转成 字符串 用 urllib.parse.
#将字典转为 字符串 urlencode  
# encoding 指定编码格式 
response=urllib.request.urlopen('http://httpbin.org/post',data=data)
print(response.read())


timeout 参数 
请求超出时间  没有得到响应 就会抛出异常 

import urllib.request

response=urllib.request.urlopen('http://httpbin.org/get',timeout=0.001)
print(response.read())

如果长时间未响应， 就跳过抓取 

import socket 
import urllib.request
import urllib.error

try:
    response=urllib.request.urlopen('http://httpbin.org/get',timeout=0.01)
except urllib.error.URLError as e:
    if isinstance(e.reason, socket.timeout):
        print('Time OUT!')


其他参数 



###################################################
2. Request 
urlopen() 可以完成基本的请求 
但是要加入 Headers 等信息 需要更加强大的 Request 

import urllib.request

request=urllib.request.Request('https://python.org')
response=urllib.request.urlopen(request)
#用对象来发送请求  
print(response.read().decode('utf-8'))


Request 参数 
class urllib.request.Request(url, data=None, headers={}, origin_req_host=None, unverifiable=False, method=None):
    

from urllib import request,parse 

url='http://httpbin.org/post'

headers={
        'User-Agent':'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)',
        'Host':'httpbin.org'
        }

dict_1={'name':'Germey'}

data=bytes(parse.urlencode(dict_1),encoding='utf-8')

req=request.Request(url=url,data=data,headers=headers,method='POST')

response=request.urlopen(req)
print(response.read().decode('utf-8'))


3. 高级用法 
Cookies 代理。。。 ： Handler  

urllib.request.BaseHandler 类  

引入 Opener 可以实现更高级的功能 
Opener 可以使用 open() 方法 利用 Handler 来构建 Opener

验证  HTTPBasicAuthHandler 

from urllib.request import HTTPPasswordMgrWithDefaultRealm, HTTPBasicAuthHandler, build_opener 
from urllib.error import URLError 

username='username'
password='password'
url='http://localhost:5000/'

p=HTTPPasswordMgrWithDefaultRealm()
p.add_password(None,url,username,password)
#建立一个处理验证的 Handler 
auth_handler=HTTPBasicAuthHandler(p)
opener=build_opener(auth_handler)

try:
    result=opener.open(url)
    html=result.read().decode('utf-8')
    print(html)
except URLError as e:
    print(e.reason)



代理 
from urllib.error import URLError 
from urllib.request import ProxyHandler, build_opener

proxy_handler=ProxyHandler({
        'http':'http://127.0.0.1:9743',
        'https':'https://127.0.0.1:9743'
        })
    
opener=build_opener(proxy_handler)

try:
    response=opener.open('https://www.baidu.com')
    print(response.read().decode('utf-8'))
except URLError as e:
    print(e.reason)



Cookies 

import http.cookiejar, urllib.request 

cookie=http.cookiejar.CookieJar()
handler=urllib.request.HTTPCookieProcessor(cookie)
opener=urllib.request.build_opener(handler)
response=opener.open('http://www.baidu.com')

for item in cookie:
    print(item.name+'='+item.value)


输出文件格式 

filename='cookies.txt'
cookie=http.cookiejar.MozillaCookieJar(filename)
handler=urllib.request.HTTPCookieProcessor(cookie)
opener=urllib.request.build_opener(handler)
response=opener.open('http://www.baidu.com')
cookie.save(ignore_discard=True,ignore_expires=True)

########################################
3.1.2 处理异常 
1. URLError 
reason 属性 返回错误原因 

from urllib import request,error 
try:
    response=request.urlopen('https://cuiqingcai.com/index.htm')
except error.URLError as e:
    print(e.reason)



2. HTTPError  认证请求失败。。。
3 个属性：
    code 
    reason 
    headers 
    
from urllib import request,error 
try:
    response=request.urlopen('http://cuiqingcai.com/index.h,m')
except error.HTTPError as e:
    print(e.reason,e.code,e.headers,sep='\n')
    

from urllib import request, error 
try:
    response=request.urlopen('http://cuiqingcai.com/index.htm')
except error.HTTPError as e:
    print(e.reason, e.code, e.headers, sep='\n')
except error.URLError as e:
    print(e.reason)
else:
    print('quest successfully')
#用 else 处理正常的逻辑 
    
    
    
    
reason 属性返回的不一定是字符串， 可能是一个对象 

import socket 
import urllib.request
import urllib.error

try:
    response=urllib.request.urlopen('https://www.baidu.com',timeout=0.01)
except urllib.error.URLError as e:
    print(type(e.reason))
    
    if isinstance(e.reason, socket.timeout):
        print('Time Out')
        

#################################################3
3.1.3 解析链接 parse 

1. urlparse 识别和分段 

from urllib.parse import urlparse 
result=urlparse('http://www.baidu.com/index.html;user?id=5#comment')
print(type(result))
print(result)
#返回一个 ParseResult 类型的对象 



from urllib.parse import urlparse 
result=urlparse('http://www.baidu.com/index.html;user?id=5#comment',allow_fragments=False)
print(result)

#实际上 返回一个元组 可以用index 索引 
from urllib.parse import urlparse 
result=urlparse('http://www.baidu.com/index.html#comment',allow_fragments=False)
print(result.scheme, result[0],result.netloc,result[1],sep='\n')


2. urlunparse 长度必须是 6  

from urllib.parse import urlunparse 

data=['http','www.baidu.com','index.html','user','a=6','comment']
print(urlunparse(data))


3. urlsplit()  5 

4. urlunsplit()


5. urljoin()


6. urlencode() 

from urllib.parse import urlencode 

params={
        'name':'germey',
        'age':12}

base_url='http://www.baidu.com'
url=base_url+urlencode(params)
print(url)


7. parse_qs()
反序列化

from urllib.parse import parse_qs

query='name=germey&age=22'
print(parse_qs(query))  


8. parse_qsl() 用于将参数转化为元组组成的列表 

from urllib.parse import parse_qsl

query='name=germey&age=22'
print(parse_qsl(query))


9. quote() 

from urllib.parse import quote 
keyboard='壁纸'

url='https://www.baidu.com/s?wd='+quote(keyboard)
print(url)


10. unquote() 
from urllib.parse import unquote 
url=''


###############################################
3.14 Robot 协议  
page 119 

用 robotparser 模块解析 robot.txt 
该模块 提供了  RobotFileParser

from urllib.robotparser import RobotFileParser 

rp=RobotFileParser()
rp.set_url('http://www.jianshu.com/robots.txt')
rp.read()

print(rp.can_fetch('*','http://www.jianshu.com/p/b675540257d'))
print(rp.can_fetch('*','http://www.jianshu.com/search?q=python&page=1&type=collections'))




3. robotparser 模块解析 robots.txt  

from urllib.robotparser import RobotFileParser 

rp=RobotFileParser()
#rp.RobotFileParser()

rp.set_url('http://www.jianshu.com/robots.txt')
rp.read()



###################################################

3.2 使用 requests 
page 122 -133 

3.2.1 基本用法 

import requests 

r=requests.get('http://www.baidu.com/')
print(type(r))
print(r.status_code)
print(type(r.text))
print(r.text)
print(r.cookies)



3. Get 请求 

基本实例

import requests 

r=requests.get('http://httpbin.org/get')
print(r.text)



import requests 
data={
      'name':'germey',
      'age':22
     }

r=requests.get('http://httpbin.org/get',params=data)
print(r.text)


想要解析返回结果， 得到一个字典格式 可以直接带用 json() 方法 

import requests 

r=requests.get('http://httpbin.org/get')
print(type(r.text))
#很特殊 是 str 类型 但是 json 格式的 
print(r.json())
print(type(r.json()))

调用 json() 方法， 就可以将返回结果是 JSON 格式的字符串转化为字典 


抓取网页  ---普通网页 

import requests 
import re 

headers={
        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Max OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'}

r=requests.get('https://www.zhihu.com/explore',headers=headers)
pattern=re.compile('explore-feed.*?question_link.*?>(.*?)</a>',re.S)
titles=re.findall(pattern,r.text)
print(titles)


抓取二进制数据 
二进制码 有特定的保存格式和对应的 解析方式 

import requests 
r=requests.get('http://github.com/favicon.ico')
print(r.text)
print(r.content)

保存图片 上面的 

import requests 
r=requests.get('http://github.com/favicon.ico')
with open('favicon.ico','wb') as f:
    f.write(r.content)


添加 headers 

4. POST 请求 
import requests 

data={'name':'germey','age':'22'}
r=requests.post('http://httpbin.org/post',data=data)
print(r.text)

5. 响应 

import requests 
r=requests.get('http://wwww.jianshu.com')
print(type(r.status_code), r.status_code)
print(type(r.headers), r.headers)
print(type(r.cookies),r.cookies)
print(type(r.url),r.url)
print(type(r.history),r.history)


###############################################
3.2.2 高级用法 
1. 上传文件 

import requests 
files={'file':open('favicon.ico','rb')}
r=requests.post('http://httpbin.org/post',files=files)
print(r.text)

2. Cookies 
import requests 
r=requests.get('https://www.baidu.com')
print(r.cookies)

for key, value in r.cookies.items():
    print(key+'='+value)

也可以直接 使用 Cookie 来维持登陆状态 
可以替换自己的 cookie 但是我 找不到 cookie 
page 131-142 


3. 维持会话
Session 对象 

import requests 

requests.get('http://httpbin.org/cookies/set/number/123456789')
r=requests.get('http://httpbin.org/cookies')
print(r.text)
# 灭有 结果 

import requests 
s=requests.Session()
s.get('http://httpbin.org/cookies/set/number/123456789')
r=s.get('http://httpbin.org/cookies')
print(r.text)

Session 可以做到模拟同一个会话不用担心 Cookies 的问题 


4. SSL 证书验证 
 
import requests 

response=requests.get('https://www.12306.cn',verify=False)
print(response.status_code)



这会有个警告 通过设置忽略警告的方式来屏蔽警告 

import requests 
from requests.packages import urllib3 

urllib3.disable_warnings()
response=requests.get('https://www.12306.cn',verify=False)
print(response.status_code)


5. 代理设置 
import requests 
proxies={
        "http":"http://10.10.1.10:3128",
        "https":"http://10.10.1.10:1080",}

requests.get("https://www.taobao.com",proxies=proxies)


6. 超时设置 

7. 身份认证 



3.3 正则表达式 
page 139 150 

1. 实例引入 
hello, my phone number is 010-86432100 and email is cqc@cuiqingcai.com, and my website is https://cuiqingcai.com

2. match() 

import re 
content='Hello 123 4567 world_This is a Regex Demo'
print(len(content))

result=re.match('^Hello\s\d\d\d\s\d{4}\s\w{10}',content)
#match() 第一个参数传入 正则表达式 
# 第二个参数传入 要匹配的字符串 
print(result)
print(result.group())
print(result.span())


匹配目标

import re 
content='Hello 1234567 World_This is a Regex Demo'
result=re.match('^Hello\s(\d+)\sWorld',content)
print(result)
print(result.group())
print(result.group(1))
print(result.span())


通用匹配 

import re 
content='Hello 123 4567 World_This is a Regex Demo'
result=re.match('^Hello.*Demo$',content)
# . 可以匹配 任意字符 除了换行符 
# * 可以匹配前面的字符 无限次 
print(result)
print(result.group())
print(result.span())


贪婪与 非贪婪 

import re 
content='Hello 1234567 World_This is a Regex Demo'
result=re.match('^He.*(\d+).*Demo$',content)
print(result)
print(result.group(1))



.*? 匹配尽可能少的字符 

import re 

content='http://weibo.com/comment/kEraCN'
result_1=re.match('http.*?comment/(.*?)',content)
result_2=re.match('http.*?comment/(.*)',content)
print('result_1',result_1.group(1))
print('result_2',result_2.group(1))

.*? 没有匹配到任何结果   .* 尽量匹配多的内容 



修饰符 
'''
这里有问题 我也不知道 出现在哪里   修饰符 
'''

import re 

content='''Hello 1234567 World_This
is a Regex Demo
'''

result=re.match('^He.*?(\d+).*?Demo$',content)
print(result.group(1))



转义匹配 
































