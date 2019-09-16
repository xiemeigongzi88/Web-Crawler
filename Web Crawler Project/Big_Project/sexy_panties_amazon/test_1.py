# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 15:56:16 2019

@author: sxw17
"""

from bs4 import BeautifulSoup
from selenium import webdriver
import requests

driver= webdriver.Chrome()

https://www.amazon.com/s?k=sexy+panties+for+women&page=2&crid=26GKVG63H487M&qid=1568494032&sprefix=sexy+pan%2Caps%2C162&ref=sr_pg_1



# page one:
https://www.amazon.com/s?k=sexy+panties+for+women&crid=26GKVG63H487M&sprefix=sexy+pan%2Caps%2C162&ref=nb_sb_ss_i_3_8
https://www.amazon.com/s?k=sexy+panties+for+women&page=2&crid=26GKVG63H487M&qid=1568494032&sprefix=sexy+pan%2Caps%2C162&ref=sr_pg_1

# page two 

https://www.amazon.com/s?k=sexy+panties+for+women&page=2&crid=26GKVG63H487M&qid=1568494032&sprefix=sexy+pan%2Caps%2C162&ref=sr_pg_2

https://www.amazon.com/s?k=sexy+panties+for+women&page=2&crid=26GKVG63H487M&qid=1568494032&sprefix=sexy+pan%2Caps%2C162&ref=sr_pg_1

https://www.amazon.com/s?k=sexy+panties+for+women&crid=26GKVG63H487M&qid=1568496457&sprefix=sexy+pan%2Caps%2C162&ref=sr_pg_1

https://www.amazon.com/s?k=sexy+panties+for+women&crid=26GKVG63H487M&qid=1568496457&sprefix=sexy+pan%2Caps%2C162&ref=sr_pg_2
# get_pages()

page one 
https://www.amazon.com/s?k=sexy+panties+for+women&crid=26GKVG63H487M&qid=1568496613&sprefix=sexy+pan%2Caps%2C162&ref=sr_pg_1


page two 
https://www.amazon.com/s?k=sexy+panties+for+women&page=2&crid=26GKVG63H487M&qid=1568496621&sprefix=sexy+pan%2Caps%2C162&ref=sr_pg_2

pre_url='https://www.amazon.com'






<a href="/s?k=sexy+panties+for+women&amp;crid=26GKVG63H487M&amp;qid=1568496891&amp;sprefix=sexy+pan%2Caps%2C162&amp;ref=sr_pg_1">1</a>

#url='https://www.amazon.com/s?k=sexy+panties&crid=2SVTTJV10B4J1&sprefix=sexy+%2Caps%2C168&ref=nb_sb_ss_i_5_5'

#driver.get(url)

import requests
url='https://www.amazon.com/s?k=sexy+panties+for+women&crid=26GKVG63H487M&qid=1568496863&sprefix=sexy+pan%2Caps%2C162&ref=sr_pg_1'
#response = requests.get(url)

driver.get(url)
soup = BeautifulSoup(driver.page_source,'lxml')

li_result = soup.find('li', class_='a-normal')
link= pre_url+li_result.find('a')['href']




get_next_page()


driver.get(url)


url_list=[]


def get_next_page(basic_url):
    
    driver.get(basic_url)
    soup = BeautifulSoup(driver.page_source,'lxml')
    
    li_result = soup.find('li', class_='a-normal')
    link= pre_url+li_result.find('a')['href']
    
    return link

def get_links(basic_url):
    
    links=[]
    #links.append(basic_url)
    next_link = get_next_page(basic_url)
    links.append(next_link)
    
    
    while next_link:
        url = next_link
        next_link=get_next_page(url)
        links.append(next_link)
    
    return links 

links = get_links(url)
    
    
    
############################ 
import requests
url='https://www.amazon.com/s?k=sexy+panties+for+women&crid=26GKVG63H487M&qid=1568496863&sprefix=sexy+pan%2Caps%2C162&ref=sr_pg_1'
#response = requests.get(url)

driver.get(url)
soup = BeautifulSoup(driver.page_source,'lxml')

li_result = soup.find('li', class_='a-normal')
link= pre_url+li_result.find('a')['href']


#page 2 
# 判断页码数

li class a-disabled

page one 
https://www.amazon.com/s?k=sexy+panties+for+women&crid=26GKVG63H487M&qid=1568501247&sprefix=sexy+pan%2Caps%2C162&ref=sr_pg_1

page two 
https://www.amazon.com/s?k=sexy+panties+for+women&page=2&crid=26GKVG63H487M&qid=1568501247&sprefix=sexy+pan%2Caps%2C162&ref=sr_pg_2

page three 

https://www.amazon.com/s?k=sexy+panties+for+women&page=3&crid=26GKVG63H487M&qid=1568501581&sprefix=sexy+pan%2Caps%2C162&ref=sr_pg_3

https://www.amazon.com/s?k=sexy+panties+for+women&page=3&crid=26GKVG63H487M&qid=1568501581&sprefix=sexy+pan%2Caps%2C162&ref=sr_pg_3



url='https://www.amazon.com/s?k=sexy+panties+for+women&crid=26GKVG63H487M&qid=1568496863&sprefix=sexy+pan%2Caps%2C162&ref=sr_pg_1'
#response = requests.get(url)

links =[]
links.append(url)
driver.get(url)
soup = BeautifulSoup(driver.page_source,'lxml')

# class = a-pagination
ul_result = soup.find('ul', class_='a-pagination')
li_results= ul_result.find_all('li')
pre_url='https://www.amazon.com'


next_link = pre_url+ ul_result.find('li', class_='a-normal').find('a')['href']

next_num =int(next_link[-1])

page_num =int( ul_result.find_all('li', class_='a-disabled')[1].text)

for i in range(next_num, page_num+1):
    link= next_link[:-1]+str(i)
    links.append(link)
    

https://www.amazon.com/s?k=sexy+panties+for+women&crid=26GKVG63H487M&qid=1568502908&sprefix=sexy+pan%2Caps%2C162&ref=sr_pg_1
https://www.amazon.com/s?k=sexy+panties+for+women&page=2&crid=26GKVG63H487M&qid=1568502928&sprefix=sexy+pan%2Caps%2C162&ref=sr_pg_2
    
https://www.amazon.com/s?k=sexy+panties+for+women&page=3&crid=26GKVG63H487M&qid=1568502811&sprefix=sexy+pan%2Caps%2C162&ref=sr_pg_3
https://www.amazon.com/s?k=sexy+panties+for+women&page=4&crid=26GKVG63H487M&qid=1568502840&sprefix=sexy+pan%2Caps%2C162&ref=sr_pg_4
https://www.amazon.com/s?k=sexy+panties+for+women&page=5&crid=26GKVG63H487M&qid=1568502862&sprefix=sexy+pan%2Caps%2C162&ref=sr_pg_5
https://www.amazon.com/s?k=sexy+panties+for+women&page=6&crid=26GKVG63H487M&qid=1568502881&sprefix=sexy+pan%2Caps%2C162&ref=sr_pg_6
https://www.amazon.com/s?k=sexy+panties+for+women&page=7&crid=26GKVG63H487M&qid=1568502895&sprefix=sexy+pan%2Caps%2C162&ref=sr_pg_7



    
###########################################################
# page one find next page 
url='https://www.amazon.com/s?k=sexy+panties+for+women&crid=26GKVG63H487M&qid=1568502908&sprefix=sexy+pan%2Caps%2C162&ref=sr_pg_1'
driver.get(url)

soup = BeautifulSoup(driver.page_source,'lxml')

ul_result = soup.find('ul', class_='a-pagination')
pre_url='https://www.amazon.com'

li_
next_link = pre_url+ ul_result.find('li', class_='a-normal').find('a')['href']

https://www.amazon.com/s?k=sexy+panties+for+women&page=2&crid=26GKVG63H487M&qid=1568502928&sprefix=sexy+pan%2Caps%2C162&ref=sr_pg_2
https://www.amazon.com/s?k=sexy+panties+for+women&page=2&crid=26GKVG63H487M&qid=1568503484&sprefix=sexy+pan%2Caps%2C162&ref=sr_pg_2



driver.get(next_link)

soup = BeautifulSoup(driver.page_source,'lxml')

ul_result = soup.find('ul', class_='a-pagination')
pre_url='https://www.amazon.com'

next_link_1 = pre_url+ ul_result.find('li', class_='a-normal').find('a')['href']



############################################
driver= webdriver.Chrome()
link_1 ='https://www.amazon.com/s?k=sexy+panties+for+women&crid=26GKVG63H487M&qid=1568504711&sprefix=sexy+pan%2Caps%2C162&ref=sr_pg_1'
driver.get(url)

soup = BeautifulSoup(driver.page_source,'lxml')

ul_result = soup.find('ul', class_='a-pagination')
pre_url='https://www.amazon.com'

li_results=ul_result.find_all('li')  # length = 7
link_2 = pre_url+ li_results[2].find('a')['href']

driver.close()

####################################
# page 2 
driver= webdriver.Chrome()
#link_1 ='https://www.amazon.com/s?k=sexy+panties+for+women&crid=26GKVG63H487M&qid=1568504711&sprefix=sexy+pan%2Caps%2C162&ref=sr_pg_1'
driver.get(link_2)

soup = BeautifulSoup(driver.page_source,'lxml')

ul_result = soup.find('ul', class_='a-pagination')
pre_url='https://www.amazon.com'

li_results=ul_result.find_all('li')  # length = 7
link_3 = pre_url+ li_results[2].find('a')['href']

driver.close()


https://www.amazon.com/s?k=sexy+panties+for+women&page=2&crid=26GKVG63H487M&qid=1568505053&sprefix=sexy+pan%2Caps%2C162&ref=sr_pg_2
https://www.amazon.com/s?k=sexy+panties+for+women&page=3&crid=26GKVG63H487M&qid=1568505053&sprefix=sexy+pan%2Caps%2C162&ref=sr_pg_3

# get page numbers 

driver= webdriver.Chrome()
url ='https://www.amazon.com/s?k=sexy+panties+for+women&crid=26GKVG63H487M&qid=1568504711&sprefix=sexy+pan%2Caps%2C162&ref=sr_pg_1'

links =[]
links.append(url)
driver.get(url)
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

for i in range(next_num, page_num+1):
    link_model = pre_url+pre_part+'page='+ str(i)+mid_part+str(i)
    links.append(link_model)
    print(link_model)
    
    
















