# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 19:15:36 2019

@author: sxw17
"""

from bs4 import BeautifulSoup
from selenium import webdriver
import requests

import os 
os.getcwd()
os.chdir('C:\\Users\\sxw17\\Desktop\\DATA\\Project\\Data Analysis\\sexy panties')

driver= webdriver.Chrome()

def get_links(basic_url):
    
    links=[]
    
    links.append(basic_url)
    driver.get(basic_url)
    soup = BeautifulSoup(driver.page_source,'lxml')
    
    # class = a-pagination
    ul_result = soup.find('ul', class_='a-pagination')
    li_results= ul_result.find_all('li')
    pre_url='https://www.amazon.com'
    
    part_link = ul_result.find('li', class_='a-normal').find('a')['href']
    
    pre_part = part_link.split('page=')[0]
    mid_part= part_link.split('page=')[1][1:-1]
    
    link_type = pre_url+ ul_result.find('li', class_='a-normal').find('a')['href']
    
    next_num =int(part_link[-1])
    
    page_num =int( ul_result.find_all('li', class_='a-disabled')[1].text)
    https://www.amazon.com/s?k=sexy+panties+for+women&page=3&crid=26GKVG63H487M&qid=1568507071&sprefix=sexy+pan%2Caps%2C162&ref=sr_pg_3
    for i in range(next_num, page_num+1):
        link_model = pre_url+pre_part+'page='+ str(i)+mid_part+str(i)
        links.append(link_model)
        print(link_model)
    
    driver.close()
    return links

url ='https://www.amazon.com/s?k=sexy+panties+for+women&crid=26GKVG63H487M&qid=1568504711&sprefix=sexy+pan%2Caps%2C162&ref=sr_pg_1'

links = get_links(url)
    