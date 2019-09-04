# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 00:51:42 2019

@author: sxw17
"""
from selenium import webdriver
from bs4 import BeautifulSoup

#driver = webdriver.Chrome()
#driver.get(url)
url ='https://www.indeed.com/jobs?q=data+analyst&l=Dallas%2C+TX'


links=[]
num=30
for i in range(num):
    url='https://www.indeed.com/jobs?q=data+analyst&l=Dallas%2C+TX&start='
    link = url+str(10*i)
    links.append(link)
    
for i, link in enumerate(links):
    print(i,link)
    
import requests

link = links[0]

driver = webdriver.Chrome()
driver.get(link)

import time
time.sleep(5)


soup = BeautifulSoup(driver.page_source, 'lxml')
td=soup.find('td', attrs={'id':'resultsCol'})

div_all=td.find_all('div', class_='jobsearch-SerpJobCard unifiedRow row result clickcard')

#div=div_all[0]
for i, div in enumerate(div_all):
    print(i, div)
    print('----------------------------')

job_list=[]

for div in div_all:
    # div class= 'title'
    # 1. title 
    title= div.find('div', class_='title').text.replace('\n','')
    print(title)
    
    # 9. description_in_detail 
    description_info =div.find('div', class_='title')
    # a target blank
    description = description_info.find('a', attrs={'target':'_blank'})
    description_link = 'https://www.indeed.com'+description['href']
    print(description_link)
    
    # dic class 'sjcl'
    detail= div.find('div', class_='sjcl')
    
    # 2. company
    company = detail.find('span', class_='company').text.replace('\n','').strip()
    print(company)
    
    # 3. ratings 
    # span class='ratings'
    ratings = detail.find('span', class_='ratings')['aria-label']
    print(ratings)
    
    # 6. review_num
    # span class='slNoUnderline'
    reviews_num = detail.find('span', class_='slNoUnderline').text
    print(reviews_num)
    
    # 7. review_links
    # data-tn-variant : cmplinktst2 
    reviews_link_info = str(detail.find('a', attrs={'data-tn-variant':'cmplinktst2'}))
    
    reviews_link_list=reviews_link_info.split("href")

    ink_pre='https://www.indeed.com/'

    link_mid= reviews_link_list[1][2:].split(' ')[0][:-1]
    
    link_post = reviews_link_list[3].split(')')[0][3:-1]
        
    job_link= link_pre+ link_mid + link_post
    print(job_link)
    
    # 8. location 
    # div class location accessible-contrast-color-location
    location = detail.find('div', class_='location').text
    print(location)
    
    # 4.summary
    # div class jobsearch-SerpJobCard-footer
    # span class  sponsoredGray 
    summary = div.find('div', class_='summary').text.replace('\n','').strip()
    print(summary)
    
    # 5. sponsor 
    # div class jobsearch-SerpJobCard-footer
    # span class  sponsoredGray 
    sponsor_check='Not'
    sponsor_check = div.find('div', class_='result-link-bar').find('span').text
    
    if sponsor_check:
        sponsor = sponsor_check
        
    print(sponsor)
    
    \

















































