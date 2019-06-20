import requests


r=requests.head('https://www.baidu.com')
r.headers
print(r.headers)

r.text
print(r.text)  # Output: empty 

# post 提交新增数据
payload={'key1':'value1','key2':'value2'}
r=requests.post('http://httpbin.org/post',data=payload)
print(r.text)
# 向 URL POST 一个字典 自动编码为 form （表单）

r=requests.post('http://httpbin.org/post', data='ABC')
print(r.text)
# data="ABC" 被存放在 data 字段下


# PUT 覆盖原有的数据
payload={'key1':'value1','key2':'value2'}
r=requests.put('http://httpbin.org/put',data=payload)
print(r.text)
