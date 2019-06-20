# 网络图片链接的格式：
# http://www.example.com/picture.jpg

import requests
import os 
path="C:\\Users\\sxw17\\Desktop\\python learning\\Web-Crawler\\Beginner\\course\\1 week"

#url='https://news.nationalgeographic.com/news/2013/11/131113-lunar-property-rights-bigelow-nasa/#/73406.jpg'
'''
sessions = requests.session()
sessions.headers['User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.131 Safari/537.36'
'''


#url='https://baike.baidu.com/pic/%E6%9D%8E%E6%9E%96%E5%8E%9F/16968724/21151077/8c1001e93901213f63cee2b85de736d12e2e95d1?fr=lemma&ct=cover#aid=21151077&pic=b8014a90f603738dcd98a046ba1bb051f919ec80'
url='https://media1.fdncms.com/orlando/imager/u/original/24166329/screen_shot_2019-02-18_at_12.12.00_pm.png'
r=requests.get(url)
print(r.status_code)

with open(path,'wb') as f:
    f.write(r.content)

f.close()
