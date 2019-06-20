import requests
'''
requests.request()
    构造一个请求， 支撑一下各方法的基础方法

requests.get()
    #获取HTML网页的主要方法
requests.head()
    #获取 HTML 网页头信息的方法
requests.post()
    # 向 HTML 网页提交 POST 请求方法
requests.put()
    # 向 HTML 网页提交 PUT 方法
requests.patch()
    # 向 HTML 网页提交局部修改请求
requests.delete()
    # 向 HTML网页提交删除请求 
'''

'''
requests.request(method,url,**kwargs)
    params: 字典或者字节序列， 作为参数增加到url 中
'''
kv={'key1':'value1','key2':'value2'}
r=requests.request('GET','http://python123.io/ws',params=kv)
print(r.url)


'''
    proxies: 字典类型， 设定访问代理服务器，可以增加登陆认证
'''

pxs={'http':'http://user:pass@10.10.10.1:1234',
     'https':'https://10.10.10.1:4321'}

r=requests.request('GET','http://www.baidu.com',proxies=pxs)



















