# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 02:49:06 2019

@author: sxw17
"""
# get_reviews_successful
import os 
os.getcwd()
os.chdir('C:\\Users\\sxw17\\Desktop\\scrapy\\Project\\yelp reviews')

import re 
import requests
from bs4 import BeautifulSoup as bs
import pandas as pd 

target = pd.read_csv('yelp_restaurant.csv', encoding='utf-8', index_col=False)

target_copy= target.copy()

def target_copy['Unnamed: 0']:
    
    def get_reviews(target_df):
    reviews_list=list()
    
    names = target_df['Name'].tolist()
    links = target_df['Link'].tolist()
    
    num = len(target_df)
    
    for i in range(num):
        name = names[i]
        link= links[i]
        
        url = link+'?sort_by=date_asc'
        soup =bs(requests.get(url).text,'lxml')
        
        all_reviews=soup.find_all('p', class_='lemon--p__373c0__3Qnnj text__373c0__2pB8f comment__373c0__3EKjH text-color--normal__373c0__K_MKN text-align--left__373c0__2pnx_')
        #print(len(all_reviews))
        
        all_stars=soup.find_all('div', class_='lemon--div__373c0__1mboc arrange__373c0__UHqhV gutter-6__373c0__zqA5A vertical-align-middle__373c0__2TQsQ border-color--default__373c0__2oFDT')
        #print(len(all_stars))
                
        if len(all_reviews)== len(all_stars)-1:
            checked_num = len(all_reviews)
            
            for j in range(checked_num):
                review= all_reviews[j].text
                star = all_start[j+1].find_all('div')[1]['aria-label']
                
                reviews_list.append((name, link, review, star))
                print(name, star)
                
    return reviews_list


result = get_reviews(target_copy)
    
record=pd.DataFrame(result, columns=['Name','Link','Review','Star'])

record.to_csv('yelp_reviews.csv')

