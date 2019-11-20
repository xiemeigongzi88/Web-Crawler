# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 17:09:46 2019

@author: sxw17
"""

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

soup = bs(driver.page_source,'lxml')

data_list=[]


table_1=soup.find('table', class_='dataView')
table_a=table_1.find_all('a')
num =len(table_a)

for i in range(1, 10):
    a= table_a[i]
    job = a.text # ok 
    print(job)
    '''
    id_click="MainContent_uxLevel2_JobTitles_uxJobTitleBtn_"+ str(i-1)
    button=driver.find_element_by_id(id_click)
    button.click()    
    
    soup_job = bs(driver.page_source,'lxml')
    link_test= soup_job.find('form', attrs={'id':'form1'})
    b= str(link_test).split('div')
    
    link= b[0].split('action')[1].split('=')[1][2:].split(' ')[0][:-1]
    print(link)
    
    data_list.append((job, link))
    '''
    
    python_button = driver.find_element_by_id('MainContent_uxLevel2_JobTitles_uxJobTitleBtn_' + str(i-1))
    python_button.click() #click link
    
    
    # soup_job= bs(driver.page_source,'lxml')
    
    soup_job = bs(driver.page_source,'lxml')
    link_test= soup_job.find('form', attrs={'id':'form1'})
    b= str(link_test).split('div')
    
    link= b[0].split('action')[1].split('=')[1][2:].split(' ')[0][:-1]
    suffix= 'http://kanview.ks.gov/PayRates/Pay'
    link_job=suffix+link
    print(link_job)
    
    data_list.append((job, link_job))
    
    
    
###############################################
# test -2 

driver=webdriver.Chrome()

url='http://kanview.ks.gov/PayRates/PayRates_Agency.aspx'
driver.implicitly_wait(10)
# open the browser 

#driver= webdriver.PhantomJS()  collapse of PhantimJS of selenium
driver.get(url)

button=driver.find_element_by_id('MainContent_uxLevel1_Agencies_uxAgencyBtn_33')
button.click()

soup_level_1 = bs(driver.page_source,'lxml')

data_list=[]
    
all_a = soup_level_1.find_all('a', id=re.compile("^MainContent_uxLevel2_JobTitles_uxJobTitleBtn_"))


python_button = driver.find_element_by_id('MainContent_uxLevel2_JobTitles_uxJobTitleBtn_' + str(0))
python_button.click() #click link

#Selenium hands of the source of the specific job page to Beautiful Soup
soup_level2=BeautifulSoup(driver.page_source, 'lxml')

#Beautiful Soup grabs the HTML table on the page
table = soup_level2.find_all('table')[0]

#Giving the HTML table to pandas to put in a dataframe object
df = pd.read_html(str(table),header=0)

df

#Store the dataframe in a list
datalist.append(df[0])

#Ask Selenium to click the back button
driver.execute_script("window.history.go(-1)") 








































