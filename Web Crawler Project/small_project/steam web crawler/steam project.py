# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 21:07:31 2019

@author: sxw17
"""
# steam project
# get the pages of top selling of Steam 
#---- url = 'https://store.steampowered.com/search/?filter=topsellers&page=1'
# url = 'https://store.steampowered.com/search/?filter=topsellers'


# test for steam project 
from selenium import webdriver
from bs4 import BeautifulSoup as bs


import pandas as pd 

def get_url(url):
    url_list=[]
    # you can change the number as you like 
    for i in range(1,3):
        url_add=url+'&page='+str(i)
        url_list.append(url_add)
        
    return url_list
    

def top_seller(url_list):
    
    record=[]
    
    for url in url_list:
        driver = webdriver.Chrome()
        driver.get(url)
        
        soup = bs(driver.page_source, 'lxml')
        
        # div id= search_result_container
        
        div = soup.find('div', {'id':'search_result_container'})
        record=[]
        # class="search_result_row ds_collapse_flag "
        for a in div.find_all('a', class_='search_result_row'):
            title= a.find('span').text
            price=a.find('div', class_='col search_price responsive_secondrow').text[1:].strip()
            link = a['href']
            try:

                driver.get(link)
                soup=bs(driver.page_source,'lxml')
                
               
                detail = soup.find('div', {'id':'game_area_description'})
                
                if detail is not None:
                    detail=detail.text
                else:
                    detail='checking...'
                    
                
            except:
                print(title)
                print('\n')
           
            record.append((title , price, link, detail))
    
    return record
    


url ='https://store.steampowered.com/search/?filter=topsellers'
url_list=get_url(url)


record= top_seller(url_list)
df=pd.DataFrame(record, columns=['title', 'price','link','description'])

df.to_csv('steam_project.csv', encoding='utf-8')
