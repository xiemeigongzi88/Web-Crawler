# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 18:37:37 2019

@author: sxw17
"""
# example online 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
from bs4 import BeautifulSoup as bs

import re 
import pandas as pd 
import os 


driver=webdriver.Chrome()

url='http://kanview.ks.gov/PayRates/PayRates_Agency.aspx'
driver.implicitly_wait(10)
# open the browser 

#driver= webdriver.PhantomJS()  collapse of PhantimJS of selenium
driver.get(url)

button=driver.find_element_by_id('MainContent_uxLevel1_Agencies_uxAgencyBtn_33')
button.click()

soup_leve1 = bs(driver.page_source,'lxml')

data_list=list()

cnt=0 

# all_a = soup.find_all('a', id=re.compile('^MainContent_uxLevel2_JobTitles_uxJobTitleBtn_'))

for link in soup_level1.find_all('a', id=re.compile("^MainContent_uxLevel2_JobTitles_uxJobTitleBtn_")):
    # MainContent_uxLevel2_JobTitles_uxJobTitleBtn_0
    button=driver.find_element_by_id('MainContent_uxLevel2_JobTitles_uxJobTitleBtn_'+str(cnt))
    button.click()
    
    soup_level2=bs(driver.page_source, 'lxml')
    
    table = soup_level2.find_all('table')[0]
    
    df = pd.read_html(str(table), header=0)
    
    data_list.append(df[0])

    driver.execute_script("window.history.go(-1)") 
    cnt+=1 
    
driver.quit()


for data in data_list[:10]:
    print(data)

record = pd.concat([pd.DataFrame(data_list[i])  for i in range(len(data_list))], ignore_index=True)

os.getcwd()
os.chdir('C:\\Users\\sxw17\\Desktop\\scrapy\\Project')

record.to_csv('KanView Search – Employee Compensation by Agency.csv')
    
    