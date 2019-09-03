# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 17:53:42 2019

@author: sxw17
"""

# small_posters_successful 
from bs4 import BeautifulSoup
from selenium import webdriver
import pandas as pd 

import os 

os.getcwd()
os.chdir('C:\\Users\\sxw17\\Desktop\\scrapy\\Project\\IMDB')


def get_movies():

    url = 'https://www.imdb.com/chart/top?ref_=nv_mv_250'
    
    # table class = chart full-width 
    
    driver.get(url)
    
    soup = BeautifulSoup(driver.page_source, 'lxml')
    
    table = soup.find('table', class_='chart full-width')
    
    movies =[]
    
    #  td class = 'titleColumn'   # 250 sure  
    for td in table.find_all('td', class_='titleColumn'):
        rank = td.text.split('\n')[1].strip()[:-1]
        title = td.text.split('\n')[2].strip()
        year= td.text.split('\n')[3].strip()[1:-1]
        
        prefix='https://www.imdb.com'
        link = prefix + td.find('a')['href']
        movies.append((rank, title, year, link))
        print(link)
        
        #print(td.text)
        print(rank)
        print(title)
        print(year)
        print('-------------')
    
    return movies
    
movies = get_movies()
df= pd.DataFrame(movies, columns=['rank', 'name', 'year', 'link'])

df.to_csv('IMDB_TOP250.csv')


def get_small_posters(df):
    links = df.link.tolist()
    
    for url in links:
        
        driver.get(url)
    
        soup = BeautifulSoup(driver.page_source,'lxml')
        
        try:
            poster_info = soup.find_all('div', class_='poster')[0]
            
            poster_img = poster_info.find('img')
            poster_name = poster_img['alt']    # ok 
            poster_link = poster_img['src']
            
            file_name = poster_name+'.jpg'
            
            f= open(file_name,'wb')
            f.write(requests.get(poster_link).content)
            f.close()
        except Exception:
            print(soup.title)
  
driver=webdriver.Chrome()
     
get_small_posters(df)
