#

import requests

r= requests.get('https://item.jd.com/12333540.html')
print(r.status_code)
print(r.encoding)

print(r.text[:1000])

# total code

import requests

url="https://item.jd.com/12333540.html"

try:
    r=requests.get(url)
    r.raise_for_status()
    r.encoding=r.apparent_encoding
    print(r.text[:1000])
except:
    print("fail")