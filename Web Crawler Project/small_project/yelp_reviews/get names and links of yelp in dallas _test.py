# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 19:30:18 2019

@author: sxw17
"""

# get names and links of yelp in dallas 
import os 
os.getcwd()
#os.chdir('C:\\Users\\sxw17\\Desktop\\python learning\\Web-Crawler\\Web Crawler Project\\Web Scraping Yelp, Text Mining and Sentiment Analysis for Restaurant Reviews')

import re 
import requests
from bs4 import BeautifulSoup as bs


links=[]
page= 'https://www.yelp.com/search?cflt=restaurants&find_loc=Dallas%2C%20TX&start=0'

html= get_one_page(page)
parser=bs(html,'lxml')
mul_link=parser.find_all(href= re.compile('biz'))

# href="/biz/ellens-dallas-4" 

for i , content in enumerate(mul_link[3:]):
    print(i, content)
    
find_link=str(mul_link[3]).split()[3]
each_link= find_link.split('?')[0].split('="')[1]
    

for i, content in enumerate(mul_link[3:]):
    try:
        find_link=str(content).split()[3]
        each_link= find_link.split('?')[0].split('="')[1]
        paste='https://www.yelp.com'
        links.append(paste + each_link.split('\"')[0])
    except:
        print(str(i)+" no exist useful data")
        
###########################################################
'''
lemon--div__373c0__1mboc mapColumnTransition__373c0__10KHB arrange-unit__373c0__1piwO arrange-unit-fill__373c0__17z0h border-color--default__373c0__2oFDT
'''
# parse_one_page 

links=[]
#https://m.yelp.com/search?cflt=restaurants&find_loc=Dallas%2C+TX&start=0
# https://m.yelp.com/search?cflt=restaurants&find_loc=Dallas%2C+TX&start=0
page= 'https://m.yelp.com/search?cflt=restaurants&find_loc=Dallas%2C+TX&start=0' 

import requests

html=requests.get(page)

soup =bs(html.text, 'lxml')

import re

total=soup.find_all('div', class_=re.compile("^lemon--div__373c0__1mboc mapColumnTransition"))

'''
# lemon--img__373c0__3GQUb photo-box-img__373c0__O0tbt
# lemon--div__373c0__1mboc arrange-unit__373c0__1piwO arrange-unit-fill__373c0__17z0h border-color--default__373c0__2oFDT
li_bt = total[0].find_all('li', class_='lemon--img__373c0__3GQUb photo-box-img__373c0__O0tbt')

#lemon--li__373c0__1r9wz border-color--default__373c0__2oFDT
# start 10 Hattie’s Restaurant
li_FDT=total[0].find_all('li',class_='lemon--li__373c0__1r9wz border-color--default__373c0__2oFDT' )


# div class = lemon--div__373c0__1mboc arrange__373c0__UHqhV border-color--default__373c0__2oFDT
div_FDT=total[0].find_all('div', class_='lemon--div__373c0__1mboc arrange__373c0__UHqhV border-color--default__373c0__2oFDT')

print(len(div_FDT))

# li class = 'lemon--li__373c0__1r9wz border-color--default__373c0__2oFDT'
li_FDT = total[0].find_all('li', class_='lemon--li__373c0__1r9wz border-color--default__373c0__2oFDT')
print(len(li_FDT))
# start from #11 Hattie’s Restaurant

# Smokey John’s Bar-B-Que
'''
# li class  page-link full-width js-fast active-background interactive-list-item new-type biz-listing

li_class= total[0].find_all('li', class_='page-link full-width js-fast active-background interactive-list-item new-type biz-listing')

# a class = lemon--a__373c0__IEZFH link__373c0__29943 link-color--blue-dark__373c0__1mhJo link-size--inherit__373c0__2JXk5
a_class= total[0].find_all('a', class_='lemon--a__373c0__IEZFH link__373c0__29943 link-color--blue-dark__373c0__1mhJo link-size--inherit__373c0__2JXk5')

print(a_class)

print(len(a_class))


for i in range(2, len(a_class),2):
    name = a_class[i].text
    print(i//2, name)
    
    link = a_class[i]['href']
    link_pre='https://m.yelp.com/'
    link=link_pre+a_class[i]['href']
    print(link)
    

################################################3

page= 'https://m.yelp.com/search?cflt=restaurants&find_loc=Dallas%2C+TX&start=0' 
import requests

html=requests.get(page)

soup =bs(html.text, 'lxml')

import re

total=soup.find_all('div', class_=re.compile("^lemon--div__373c0__1mboc mapColumnTransition"))

data_list=list()

a_class= total[0].find_all('a', class_='lemon--a__373c0__IEZFH link__373c0__29943 link-color--blue-dark__373c0__1mhJo link-size--inherit__373c0__2JXk5')

for i in range(2, len(a_class),2):
    name = a_class[i].text
    print(i//2, name)
    
    link = a_class[i]['href']
    link_pre='https://m.yelp.com/'
    link=link_pre+a_class[i]['href']
    print(link)
    
    data_list.append((name, link))
    
data_list

import pandas as pd 
record= pd.DataFrame(data_list, columns=['Name','Link'])

################################################################
# page 1 
https://www.yelp.com/search?cflt=restaurants&find_loc=Dallas%2C%20TX
   # or 
https://www.yelp.com/search?cflt=restaurants&find_loc=Dallas%2C%20TX&start=0
# page 2 
https://www.yelp.com/search?cflt=restaurants&find_loc=Dallas%2C%20TX&start=30

# https://www.yelp.com/search?cflt=restaurants&find_loc=Dallas%2C+TX&start=30&mapsize=1684%2C-2988



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











     