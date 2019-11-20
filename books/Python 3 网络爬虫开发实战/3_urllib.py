# -*- coding: utf-8 -*-
"""
Created on Wed Jan  2 16:48:32 2019

@author: sxw17
"""

'''
3 library 


'''

#page 103 
# 3.1.1 发送请求
import urllib.request

response=urllib.request.urlopen('https://www.python.org')
print(response.read().decode('utf-8')) 


#######################################
import urllib.request

response=urllib.request.urlopen('https://www.python.org')
print(type(response))
#print(response.read().decode('utf-8')) 

###############################
import urllib.request

response=urllib.request.urlopen('https://www.python.org')
print(response.status)
print(response.getheaders())
print(response.getheader('Server'))


#######################################

import urllib.parse
import urllib.request

data=bytes(urllib.parse.urlencode({'word':'hello'}),encoding='utf-8')
response=urllib.request.urlopen('http://httpbin.org/post',data=data)
print(response.read())


####################################
import urllib.request

response=urllib.request.urlopen('http://httpbin.org/get',timeout=0.1)
print(response.read())



import socket 
import urllib.request
import urllib.error

try:
    response=urllib.request.urlopen('http://httpbin.org/get',timeout=0.001)
except urllib.error.URLError as e:
    if isinstance(e.reason,socket.timeout):
        print('TIME OUT')
        

##########################################
#2.Request
        
import urllib.request

request=urllib.request.Request('http://python.org')
response=urllib.request.urlopen(request)
print(response.read().decode('utf-8'))
#print(response.read())

#################################

from urllib import request,parse

url='http://httpbin.org/post'

headers={
        'User-Agent':'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)',
        'Host':'httpbin.org'
        }

dict_1={
      'name':'Germey'}

data=bytes(parse.urlencode(dict_1),encoding='utf-8')
req=request.Request(url=url,data=data,headers=headers,method='POST')
response=request.urlopen(req)
print(response.read().decode('utf-8'))


#####################################33
from urllib.request import HTTPPasswordMgrWithDefaultRealm, HTTPBasicAuthHandler, build_opener
from urllib.error import URLError

username='username'
password='password'
url='http://localhost:5000/'

p=HTTPPasswordMgrWithDefaultRealm()
p.add_password(None,url,username,password)
auth_handler=HTTPBasicAuthHandler(p)
opener=build_opener(auth_handler)

try:
    result=opener.open(url)
    html=result.read().decode('utf-8')
    print(html)
except URLError as e:
    print(e.reason)


############################################
import http.cookiejar, urllib.request

cookie=http.cookiejar.CookieJar()
handler=urllib.request.HTTPCookieProcessor(cookie)
opener=urllib.request.build_opener(handler)

response=opener.open('http://www.baidu.com')

for i in cookie:
    print(i.name+' '+i.value)

######################################
filename='cookie.txt'
cookie=http.cookiejar.MozillaCookieJar(filename)
handler=urllib.request.HTTPCookieProcessor(cookie)
opener=urllib.request.build_opener(handler)
response=opener.open('http://baidu.com')
cookie.save(ignore_discard=True, ignore_expires=True)


##########################################

from urllib import request, error 
try:
    response=request.urlopen('https://cuiqingcai.com')
except error.HTTPError as e:
    print(e.reason, e.code, e.headers,seq='\n')


##############################
from urllib.parse  import urlparse

result=urlparse('http://www.baidu . com/index .htr比 u ser?id=S#comment')
print(type(result),result)









