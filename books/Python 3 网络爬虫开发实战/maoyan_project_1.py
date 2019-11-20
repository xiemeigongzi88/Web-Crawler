# -*- coding: utf-8 -*-
"""
Created on Tue Jan 15 20:49:12 2019

@author: sxw17
"""
#url='https://maoyan.com/board/4'
'''
后面 开始引入进程池  我还没有学习 
到时候再说 
'''



import requests 
import re
import json
#from requests.exception imoport RequestException 

def get_one_page(url):
    try:
        headers={
        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Max OS X 10_13_3) AppleWebKit/537.36 (KHTML, liek Gecko) Chrome/65.0.3325.162 Safari/537.36'}
    
        response=requests.get(url, headers=headers)
    
        if response.status_code==200:
            return response.text
    except requests.RequestException:
        return None 

#def parse_one_page(html):
    
def parse_one_page(html):
    pattern=re.compile('<dd>.*?board-index.*?>(\d+)</i>.*?data-src="(.*?)".*?name"><a'
                       +'.*?>(.*?)</a>.*?star">(.*?)</p>.*?releasetime">(.*?)</p>'
                       +'.*?integer">(.*?)</i>.*?fraction">(.*?)</i>.*?</dd>',re.S)

    items=re.findall(pattern,html) #list 
    print(items)
    
    for item in items:
        # 生成器 
        yield{
            'index':item[0],
            'iamge':item[1],
            'title':item[2],
            'actors':item[3].strip()[3:],
            'time':item[4].strip()[5:],
            'score':item[5]+item[6],
            }
    
def write_to_file(content):
    with open('result.txt','a', encoding='utf-8') as f:
        f.write(json.dumps(content,ensure_ascii=False) + "\n")
        f.close()

def main(offset):
    url='https://maoyan.com/board/4?offset='+str(offset)
    
    html=get_one_page(url)
    #parse_one_page(html)
    
    for item in parse_one_page(html):
        print(item)
        write_to_file(item)
    
    
    
if __name__=='__main__':
    
    for i in range(10):
        main(i*10)

