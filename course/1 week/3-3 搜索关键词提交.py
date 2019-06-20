# 百度的关键词接口：
# http://www.baidu.com/s?wd=keyword

import requests
kv={'wd':'python'}
r=requests.get('http://www.baidu.com/s',params=kv)
print(r.status_code)

print(r.request.url)
print(len(r.text))

# complete code

import requests
keyword="python"

try:
    kv={"wd":keyword}
    r=requests.get('http://www.google.com/search',params=kv)
    r.raise_for_status()
    r.encoding=r.apparent_encoding
    print(r.text)
except:
    print('error!')