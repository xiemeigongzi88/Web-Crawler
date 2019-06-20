import requests

# 3.2.1  example 
import requests
url='http://www.cuiqingcai.com'
response= requests.get(url)
print(response.status_code)

print(response.encoding)

print(response.text)
print(response.cookies)


# GET 请求
url='http://httpbin.org/get'
# 该网站会判断 客户端发起的是 GET 请求 返回相应的请求信息

response=requests.get(url)
print(response.text)


# GET 中 添加参数
data={
    'name':'germey',
    'age':22
}
r=requests.get(url, params=data)
print(r.text)


# 返回类型是 str 类型， JSON 格式  
# 直接解析返回结果， 得到字典格式 可以调用 json() method 

import requests
r=requests.get(url)
print(type(r.text))
# 调用 json（） 方法 得到字典格式  
print(r.json())

print(type(r.json()))

# 抓取网页 
import requests
import re 

'''
查找方式： 
network:

User-Agent: Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Mobile Safari/537.36

'''

headers={'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Mobile Safari/537.36'}

url='https://www.zhihu.com/explore'
response=requests.get(url, headers=headers)
response.encoding=response.apparent_coding 

'''
<a class="question_link" href="/question/284668287/answer/703196498" target="_blank" data-id="25536714" data-za-element-name="Title">
当朱一龙的粉丝是怎么样的一种体验？
</a>
'''

'''

'''
pattern=re.compile('explore-feed.*?question_link.*?>(.*?)</a>',re.S)
title=re.findall(pattern,response.text)
print(title)

# 抓取二进制数据
import requests
url="https://github.com/favicon.ico"
r=requests.get(url)
print(r.text)
print(r.content)

# 保存图片 
import requests 
r=requests.get(url)
with open('favicon.ico','wb') as f:
	f.write(r.content)
	
	
# 添加 headers 
# 针对知乎来说 不传递 headers 不能在正常请求 

import requests 
url='https://www.zhihu.com/explore'
r=requests.get(url)
print(r.text)


# POST 请求 
data={
    'name':'germey',
    'age':22
}
r=requests.get(url, params=data)
print(r.text)

r1=requests.post(url,data=data)
print(r1.text)


# 响应 response 
url='http://wwww.jianshu.com'
r=requests.get(url)

print(type(r.status_code), r.status_code)
print(type(r.headers), r.headers)
print(type(r.cookies), r.cookies)

print(type(r.url), r.url)
print(type(r.history), r.history)


# 3.2.2 高级用法 
# such as : 文件上传 cookies 设置， 代理设置 

# 1. 文件上传 没兴趣 

# 2. cookies 
import requests 
url="https://www.baidu.com"
r=requests.get(url)
print(r.cookies)

for key, value in r.cookies.items():
	print(key+' '+value)
	
	
# cookies 维持登陆状态 
'''
cookie: d_c0="AHDCRHDhrAyPTkm6zC0bIgIKL43EPPV09k0=|1510540252"; _zap=6e52a037-14a2-4701-ac32-ba717b8dd741; _xsrf=YLvllP7KpbQ9JP5eKAoSLNS36lPreoNL; tst=r; __gads=ID=6c40fa8853f8f38a:T=1540170196:S=ALNI_MZNJ_ksvH2OPEf1GoSHQ2x4zKvuGw; z_c0="2|1:0|10:1547918473|4:z_c0|92:Mi4xUGxFNEFBQUFBQUFBY01KRWNPR3NEQ1lBQUFCZ0FsVk5pYW93WFFCcjVMX18wUTVpcmlIeFFJQjhJbmRaZVd1QlZn|5a26be08263acb5bc25ca979aef1ef2257543e90a3d3d84d2da9b785cc64899f"; __utma=155987696.927077142.1556518157.1556518157.1556518157.1; __utmz=155987696.1556518157.1.1.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); q_c1=e800cca0e552432a9ad1019a505d9c99|1558752946000|1510540251000; tgw_l7_route=f2979fdd289e2265b2f12e4f4a478330
'''
headers={'cookie': 'd_c0="AHDCRHDhrAyPTkm6zC0bIgIKL43EPPV09k0=|1510540252"; _zap=6e52a037-14a2-4701-ac32-ba717b8dd741; _xsrf=YLvllP7KpbQ9JP5eKAoSLNS36lPreoNL; tst=r; __gads=ID=6c40fa8853f8f38a:T=1540170196:S=ALNI_MZNJ_ksvH2OPEf1GoSHQ2x4zKvuGw; z_c0="2|1:0|10:1547918473|4:z_c0|92:Mi4xUGxFNEFBQUFBQUFBY01KRWNPR3NEQ1lBQUFCZ0FsVk5pYW93WFFCcjVMX18wUTVpcmlIeFFJQjhJbmRaZVd1QlZn|5a26be08263acb5bc25ca979aef1ef2257543e90a3d3d84d2da9b785cc64899f"; __utma=155987696.927077142.1556518157.1556518157.1556518157.1; __utmz=155987696.1556518157.1.1.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); q_c1=e800cca0e552432a9ad1019a505d9c99|1558752946000|1510540251000; tgw_l7_route=f2979fdd289e2265b2f12e4f4a478330'}

url="https://www.zhihu.com"
r=requests.get(url, headers=headers)
print(r.text)
print(r.status_code) # 400 服务器不理解请求的语法





























