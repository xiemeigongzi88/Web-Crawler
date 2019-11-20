# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 13:15:47 2019

@author: sxw17
"""

# http://kanview.ks.gov/PayRates/PayRates_Agency.aspx

# get the public available data 

from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
from bs4 import BeautifulSoup as bs

import re 
import pandas as pd 
import os 


from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
driver = webdriver.Chrome(chrome_options=chrome_options)


url='http://kanview.ks.gov/PayRates/PayRates_Agency.aspx'

driver=webdriver.Chrome()

# open the browser 

#driver= webdriver.PhantomJS()
driver.get(url)

'''
 <a id="MainContent_uxLevel1_Agencies_uxAgencyBtn_33" 
 href="javascript:__doPostBack(&#39;ctl00$MainContent$uxLevel1_Agencies$ctl35$uxAgencyBtn&#39;
 ,&#39;&#39;)">Fort Hays State University</a>
'''

button=driver.find_element_by_id('MainContent_uxLevel1_Agencies_uxAgencyBtn_33')
button.click()

soup = bs(driver.page_source,'lxml')

data_list=[]

cnt=0 

'''
<table class="dataView" cellspacing="0" rules="all" border="1" 
    id="MainContent_uxLevel2_JobTitles" style="border-collapse:collapse;">
'''

table= soup.find_all('table', attrs={'id':'MainContent_uxLevel2_JobTitles'})
print(table[:100])

'''
<table class="dataView" cellspacing="0" rules="all" border="1" 
id="MainContent_uxLevel2_JobTitles" style="border-collapse:collapse;">
'''

table_1=soup.find('table', class_='dataView')

table_a=table_1.find_all('a')
num =len(table_a)

test_a=table_a[1]
job_name = test_a.text # ok 
print(job_name)
link = test_a['href']
print(link)




id_click=id="MainContent_uxLevel2_JobTitles_uxJobTitleBtn_"+'0'


button=driver.find_element_by_id(id_click)
button.click()

# <form method="post" action="./PayRates_Agency.aspx" id="form1">

soup = bs(driver.page_source,'lxml')
link_test= soup.find('form', attrs={'id':'form1'})
b= str(link_test).split('div')

link= b[0].split('action')[1].split('=')[1][2:].split(' ')[0][:-1]







driver.get(link)
soup_job=bs(driver, 'lxml')



df= pd.read_html(link)


detail = table.find_all('a')


##################################################################
table_1=soup.find('table', class_='dataView')
table_a=table_1.find_all('a')
num =len(table_a)


a=table_a[1]
job = a.text # ok 
print(job)

python_button = driver.find_element_by_id('MainContent_uxLevel2_JobTitles_uxJobTitleBtn_' + str(0))
python_button.click() #click link



id_click="MainContent_uxLevel2_JobTitles_uxJobTitleBtn_"+ str(0)
button=driver.find_element_by_id(id_click)
button.click()    

soup_job = bs(driver.page_source,'lxml')
link_test= soup_job.find('form', attrs={'id':'form1'})
b= str(link_test).split('div')

link= b[0].split('action')[1].split('=')[1][2:].split(' ')[0][:-1]
print(link)
    
    

'''
button=driver.find_element_by_id('MainContent_uxLevel1_Agencies_uxAgencyBtn_33')
button.click()

soup = bs(driver.page_source,'lxml')
'''



for i in range(1, num+1):
    a= table_a[i]
    job = a.text # ok 
    print(job)
    id_click="MainContent_uxLevel2_JobTitles_uxJobTitleBtn_"+ str(i-1)
    button=driver.find_element_by_id(id_click)
    button.click()    
    
    soup_job = bs(driver.page_source,'lxml')
    link_test= soup_job.find('form', attrs={'id':'form1'})
    b= str(link_test).split('div')
    
    link= b[0].split('action')[1].split('=')[1][2:].split(' ')[0][:-1]
    print(link)
    
    data_list.append((job, link))







###############################################################

from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
from bs4 import BeautifulSoup as bs

import re 
import pandas as pd 
import os 

url='http://kanview.ks.gov/PayRates/PayRates_Agency.aspx'

driver=webdriver.Chrome()

# open the browser 

#driver= webdriver.PhantomJS()
driver.get(url)

button=driver.find_element_by_id('MainContent_uxLevel1_Agencies_uxAgencyBtn_33')
button.click()

soup = bs(driver.page_source,'lxml')

data_list=[]

cnt=0 

table_1=soup.find_all('table', class_='dataView')

table_a=table_1.find_all('a')
num =len(table_a)



#  for 
test_a=table_a[1]
job_name = test_a.text # ok 
print(job_name)


python_button = driver.find_element_by_id('MainContent_uxLevel2_JobTitles_uxJobTitleBtn_' + str(0))
python_button.click() #click link


# soup_job= bs(driver.page_source,'lxml')

soup_job = bs(driver.page_source,'lxml')
link_test= soup_job.find('form', attrs={'id':'form1'})
b= str(link_test).split('div')

link= b[0].split('action')[1].split('=')[1][2:].split(' ')[0][:-1]
suffix= 'http://kanview.ks.gov/PayRates/Pay'
link_job=suffix+link
print(link_job)
    







