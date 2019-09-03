# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 14:40:53 2019

@author: sxw17
"""

from bs4 import BeautifulSoup
from selenium import webdriver

import os 

os.getcwd()
os.chdir('C:\\Users\\sxw17\\Desktop\\scrapy\\Project\\IMDB')


driver = webdriver.Chrome()

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
    

td_1=table.find_all('td',class_='titleColumn')[1]
td_1_text = td_1.text
rank = td_1_text.split('\n')[1].strip()[:-1]

title = td_1.text.split('\n')[2].strip()

year= td_1.text.split('\n')[3].strip()[1:-1]

td_1.find('a')['href']

import pandas as pd 
df= pd.DataFrame(movies, columns=['rank', 'name', 'year', 'link'])

url = df.link[0]

driver.get(url)

soup = BeautifulSoup(driver.page_source,'lxml')

poster_info = soup.find_all('div', class_='poster')[0]

poster_img = poster_info.find('img')
poster_name = poster_img['alt']    # ok 
poster_link = poster_img['src']
    
#------------------------

url = df.link[1]

driver.get(url)

soup = BeautifulSoup(driver.page_source,'lxml')

poster_information = soup.find_all('div', class_='poster')[0]

pre_link= poster_information.find('a')['href']
link = "https://www.imdb.com"+pre_link

driver.get(link)
soup_1=BeautifulSoup(driver.page_source, 'lxml')

div_all = soup_1.find_all('div', class_='pswp__zoom-wrap')

img=div_all[1].find('img', class_='pswp__img pswp__img--placeholder')
src=img['src']
file_name = soup_1.title.text

if len(div_all)==2:
    div=div_all[1]
    img = div.find('img', class_='pswp__img pswp__img--placeholder')
    src= img['src']
    
elif len(div_all)==3:
    div = div_all[0]
    img = div.find('img', class_='pswp__img pswp__img--placeholder')
    src= img['src']



#########################################

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
    
import pandas as pd 
df= pd.DataFrame(movies, columns=['rank', 'name', 'year', 'link'])


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
        
get_small_posters(df)


##############################################################
# get larger poster 

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






























