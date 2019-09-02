# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 23:40:59 2019

@author: sxw17
"""

# get names and links of yelp in dallas 
import os 
os.getcwd()
os.chdir('C:\\Users\\sxw17\\Desktop\\scrapy\\Project\\yelp reviews')

import re 
import requests
from bs4 import BeautifulSoup as bs
import pandas as pd 


def get_pages():
    url='https://www.yelp.com/search?cflt=restaurants&find_loc=Dallas%2C%20TX&start='
    
    url_list=[]
    
    # the pages you can change as you like
    for i in range(21):
        url_list.append(url+str(30*i))
        
    return url_list

def get_basic_info(url_list):
    data_list=list()
    
    for page in url_list:
        
        html=requests.get(page)

        soup =bs(html.text, 'lxml')
        
        total=soup.find_all('div', class_=re.compile("^lemon--div__373c0__1mboc mapColumnTransition"))
            
        a_class= total[0].find_all('a', class_='lemon--a__373c0__IEZFH link__373c0__29943 link-color--blue-dark__373c0__1mhJo link-size--inherit__373c0__2JXk5')
        
        for i in range(2, len(a_class),2):
            name = a_class[i].text
            print(i//2, name)
            
            link = a_class[i]['href']
            link_pre='https://m.yelp.com/'
            link=link_pre+a_class[i]['href']
            print(link)
            
            data_list.append((name, link))
    
    return data_list


url_list= get_pages()
data_list=get_basic_info(url_list)

record= pd.DataFrame(data_list, columns=['Name','Link'])

record.to_csv('yelp_restaurant.csv', encoding='utf-8')