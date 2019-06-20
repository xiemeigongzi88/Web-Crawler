
#
import requests

url='https://www.amazon.cn/dp/B01M8L5Z3Y/ref=sr_1_1?__mk_zh_CN=%E4%BA%9A%E9%A9%AC%E9%80%8A%E7%BD%91%E7%AB%99&keywords=%E6%9E%81%E7%AE%80&qid=1559526036&s=gateway&sr=8-1'
r= requests.get(url)

print(r.status_code)

print(r.request.headers)
# 忠实地告诉 Amazon 这次访问 是由 python 的 request 库访问造成的

# 程序模拟浏览器访问
# 重新定义 user-agent 的信息内容  request 库 是可以改变头信息的
kv={'user-agent':'Mozilla/5.0'}  # 身份标识字段： Mozilla

url='https://www.amazon.cn/dp/B01M8L5Z3Y/ref=sr_1_1?__mk_zh_CN=%E4%BA%9A%E9%A9%AC%E9%80%8A%E7%BD%91%E7%AB%99&keywords=%E6%9E%81%E7%AE%80&qid=1559526036&s=gateway&sr=8-1'

r.request.get(url,headers=kv)
print(r.status_code)
print(r.request.headers)
print(r.text[:1000])


# complete code

import requests
url="https://www.amazon.cn/dp/B01M8L5Z3Y/ref=sr_1_1?__mk_zh_CN=%E4%BA%9A%E9%A9%AC%E9%80%8A%E7%BD%91%E7%AB%99&keywords=%E6%9E%81%E7%AE%80&qid=1559526036&s=gateway&sr=8-1"

try:
    kv={'user-agent':'Mozilla/5.0'}
    r=requests.get(url,headers=kv)
    r.raise_for_status()
    r.encoding=r.apparent_encoding
    print(r.text[:500])
except:
    print("error")


