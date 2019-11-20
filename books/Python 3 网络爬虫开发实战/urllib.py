# -*- coding: utf-8 -*-
"""
Created on Sat Dec 22 17:23:15 2018

@author: sxw17
"""
'''
8 Urllib 库 基本使用 

Urllib :
    
urllib.request  请求模块
urllib.error 异常处理模块
urllib.parse url 解析模块
urllib.robotpaser robot。txt 解析模块 

函数：
urlopen

urllib.request.urlopen(url, data=None, 
[timeout, ]*, cafile=None, capath=None,
 cadefault=False, context=None)

'''

import urllib.request

response=urllib.request.urlopen('http://www.baidu.com')
print(response.read().decode('utf-8'))


###########################################

import urllib.parse
import urllib.request

data=bytes(urllib.parse.urlencode({'word':'hello'}),encoding='utf8')

response=urllib.request.urlopen('http://httpbin.org/post',data=data)

print(response.read())


###########################################3

import urllib.request
response=urllib.request.urlopen('http://httpbin.org/get',timeout=1)
print(response.read())


#######################################

import urllib.request
import socket
import urllib.error

try:
    response=urllib.request.urlopen('http://httpbin.org/get',timeout=0.1)
except urllib.error.URLError as e:
    if isinstance(e.reason,socket.timeout):
        print('Time out.')


#########################################
'''
响应类型
'''
import urllib.request

response=urllib.request.urlopen('http://www.python.org')
print(type(response))


############################################
'''
状态码， 响应头
'''
import urllib.request

response=urllib.request.urlopen('http://www.python.org')
print(response.status)
print(response.getheaders())
print(response.getheader('Server'))


####################################################
'''
Request
'''

import urllib.request

request=urllib.request.Request('http://python.org')
response=urllib.request.urlopen(request)
print(response.read().decode('utf-8'))

##########################################

from urllib import request, parse

url='http://httpbin.org/post'

headers={
        'User-Agent':'Mozillia/4.0'
        }




































