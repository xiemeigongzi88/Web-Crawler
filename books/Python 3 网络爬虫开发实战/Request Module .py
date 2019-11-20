# -*- coding: utf-8 -*-
"""
Created on Fri Jan 18 21:00:03 2019

@author: sxw17
"""

Request Module 
'''
对request 库 进行补充
http://docs.python-requests.org/zh_CN/latest/user/quickstart.html

https://cuiqingcai.com/2556.html

'''





import requests 
r=requests.get('http://cuiqingcai.com')
print(type(r))
print(r.status_code)
print()

# 获取 某个网页 
import requests

r=requests.get('https://api.github.com/events')

r=requests.post('http://httpbin.org/post',data={'key':'value'})

# 传递 URL 参数 
payload={'key1':'value1','key2':'value2'}
r=requests.get('http://httpbin.org/get',params=payload)
print(r.url)


payload={'key1':'value1','key2':['value2','value3']}
r=requests.get('http://httpbin.org/get',params=payload)
print(r.url)


#响应内容 
import requests 
r=requests.get('https://api.github.com/events')
print(r.text)

print(r.encoding)
r.encoding='ISO-8859-1'
print(r.text)

print(r.content)


# 以二进制数据创建一张图片 
from PIL import Image 
from io import BytesIO

i=Image.open(BytesIO(r.content))
# 这个有问题 

#JSON 响应内容 
import requests
r=requests.get('https://api.github.com/events')
print(r.json())# 有结果 并不意味响应成功 
# 如果想 检查是否响应成功 用 下面的 
print(r.raise_for_status)
print(r.status_code)


#原始响应内容 
#想获得来自服务器的原始套结字响应 
#需要再初始请求中 设置 stram=True 
r=requests.get('https://api.github.com/events',stream=True)
print(r.raw)
print(r.raw.read(10))

#将文本保存到文件中 

with open(filename,'wb') as fd:
    for chunk in r.iter_content(chunk_size):
        fd.write(chunk)
        
#定制请求头 
url='https://api.github.com/some/endpoint'
headers={'user-agent':'my-app/0.0.1'}
r=requests.get(url,headers=headers)

#POST 请求 


响应状态码
r=requests.get('http://httpbin.org/get')
print(r.status_code)

print(r.status_code==requests.codes.ok)

bad_r=requests.get('http://httpbin.org/status/404')
print(bad_r.status_code)
print(bad_r.raise_for_status())


响应头 

print(r.headers) # 字典的格式 
print(r.headers['Content-Type'])


cookie 
# 这里有问题 没有结果出来 
url='http://example.com/some/cookie/setting/url'
r=requests.get(url)
print(r.cookies)

重新定向与请求历史
使用  allow_redirects 参数禁用重定处理

r=requests.get('http://github.com',allow_redirects=False)
print(r.status_code)
print(r.history)



'''
official document of Request 
http://docs.python-requests.org/en/master/
'''
import requests
r=requests.get('https://api.github.com/user',auth=('user','pass'))
print(r.status_code)

print(r.headers['content-type'])

print(r.encoding)

print(r.text) #dict outcome 

print(r.json())




































































