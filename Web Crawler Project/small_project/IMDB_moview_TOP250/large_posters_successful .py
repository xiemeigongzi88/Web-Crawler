# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 17:53:42 2019

@author: sxw17
"""
# large_posters_successful 
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

driver=webdriver.Chrome()

def get_larger_posters_links(links):
    tmp =links 
    
    for url in tmp:
        driver.get(url)
        soup = BeautifulSoup(driver.page_source,'lxml')
        
        poster_information = soup.find_all('div', class_='poster')[0]
        
        pre_link= poster_information.find('a')['href']
        link = "https://www.imdb.com"+pre_link
        
        driver.get(link)
        soup_1=BeautifulSoup(driver.page_source, 'lxml')
        name = soup_1.title.text
        
        try:
            
            div_all = soup_1.find_all('div', class_='pswp__zoom-wrap')
        
            #img=div_all[1].find('img', class_='pswp__img pswp__img--placeholder')['src']
            
            src=''
            if len(div_all)==2:
                div=div_all[0]
                img = div.find('img', class_='pswp__img pswp__img--placeholder')
                src= img['src']
            elif len(div_all)==3:
                div = div_all[1]
                img = div.find('img', class_='pswp__img pswp__img--placeholder')
                src= img['src']
            
            
            file_name= name +'.jpg'
            f= open(file_name,'wb')
            f.write(requests.get(src).content)
            f.close()
        except Exception:
            print(name)
            

get_larger_posters_links(df.link)         
