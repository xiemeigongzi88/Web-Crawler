# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 23:49:51 2019

@author: sxw17
"""
# steam test_2
from selenium import webdriver
from bs4 import BeautifulSoup as bs
import pandas as pd 

driver = webdriver.Chrome()

def get_url(url):
    url_list=[]
    # you can change the number as you like 
    for i in range(1,3):
        url_add=url+'&page='+str(i)
        url_list.append(url_add)
        
    return url_list


def top_seller(url_list):
    
    for url in url_list:
        
        
        driver.get(url)
        
        soup = bs(driver.page_source, 'lxml')
        
        # div id= search_result_container
        
        div = soup.find('div', {'id':'search_result_container'})
        all_a = div.find_all('a', class_='search_result_row')
        num = len(all_a)
        record=[]
        # class="search_result_row ds_collapse_flag "
        for i in range(num):

            a=all_a[i]
            title = a.find('span').text
            price_tmp=a.find('div', class_='col search_price_discount_combined responsive_secondrow').find_all('div')[1]
            price= price_tmp.text[1:].strip()
            link = a['href']
            record.append((title, price, link))
    
    return record
    
def get_detail(links):
    description=[]
    
    for link in links:
        driver.get(link)
        soup = bs(driver.page_source, 'lxml')
        detail  = soup.find('div', {'id':'game_area_description'})
                        
        if detail is not None:
            detail=detail.text
        else:
            detail='checking...'
    
        description.append(detail)
        
    return description
    
url ='https://store.steampowered.com/search/?filter=topsellers'
url_list=get_url(url)


record= top_seller(url_list)
df=pd.DataFrame(record, columns=['title', 'price','link'])

description= get_detail(df.link)
df[detail]= pd.Series(description,  name='detail')

    

#######################################
links=df['link']
link=links[0]
driver.get(link)
soup = bs(driver.page_source, 'lxml')
detail  = soup.find('div', {'id':'game_area_description'})
                
if detail is not None:
    detail=detail.text
else:
    detail='checking...'



























df.to_csv('steam_project.csv')

