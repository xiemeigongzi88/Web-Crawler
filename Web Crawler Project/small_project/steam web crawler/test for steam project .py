# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 20:02:22 2019

@author: sxw17
"""

# test for steam project 
from selenium import webdriver
from bs4 import BeautifulSoup as bs

driver = webdriver.Chrome()

def login(username, password):
    url='https://help.steampowered.com/en/wizard/Login'
    driver.get(url)
    


def top_seller():
    url='https://store.steampowered.com/search/?filter=topsellers'
    
    
    driver.get(url)
    
    soup = bs4(driver.page_source, 'lxml')
    
    # div id= search_result_container
    
    div = soup.find('div', {'id':'search_result_container'})
    record=[]
    # class="search_result_row ds_collapse_flag "
    for a in div.find_all('a', class_='search_result_row'):
        span= a.find('span')
        price=a.find('div', class_='col search_price responsive_secondrow')
        print(span.text)
        print(a['href'])
        print('\n')
        record.append((span, a['href']))
    
    return record
    
    
record= top_seller()


# https://help.steampowered.com/en/wizard/Login

# <div id="game_area_description" class="game_area_description">

def detail(url):
    driver.get(url)
    soup=bs4(driver.page_source,'lxml')
    
    detail = soup.find('div', {'id':'game_area_description'})
    
    if detail is not None:
        print(detail.text)
    
    
    
    
##############################################
    
print(div)

div.find('a')

print(type(div.find('a')))

print(len(div.find('a').contents))

a_list=div.find('a').contents

for i,tag in enumerate(a_list):
    print(i, tag)

a_list[3].split('title')



#--------------------------------
div.find('a', class_='search_result_row').find('span').text

class="col search_price  responsive_secondrow"

div.find('a', class_='search_result_row').find('div', class_='col search_price')



# -------------------------------

url='https://store.steampowered.com/app/617290/Remnant_From_the_Ashes/'
driver.get(url)
soup= bs4(driver.page_source,'lxml')
detail = soup.find('div', {'id':'game_area_description'})
print(detail.text)





https://store.steampowered.com/search/?filter=topsellers

https://store.steampowered.com/search/?filter=topsellers&page=1
https://store.steampowered.com/search/?filter=topsellers&page=2
https://store.steampowered.com/search/?filter=topsellers&page=3



# -------------------------------------
url='https://store.steampowered.com/search/?filter=topsellers'


driver.get(url)

soup = bs(driver.page_source, 'lxml')

# div id= search_result_container

div = soup.find('div', {'id':'search_result_container'})

first_a=div.find('a', class_='search_result_row' )
price=first_a.find('div', class_='col search_price responsive_secondrow')


record=[]
# class="search_result_row ds_collapse_flag "
for a in div.find_all('a', class_='search_result_row'):
    span= a.find('span')
    print(span.text)
    print(a['href'])
    print('\n')
    record.append((span, a['href']))

return record


#_____________________________
from selenium import webdriver
from bs4 import BeautifulSoup as bs


import pandas as pd 

def get_url(url):
    url_list=[]
    
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
            span= a.find('span')
            price=a.find('div', class_='col search_price responsive_secondrow').text[1:].strip()
            specifc_url = a['href']
            #driver.close()
            driver.get(specifc_url)
            soup=bs(driver.page_source,'lxml')
    
            detail = soup.find('div', {'id':'game_area_description'})
            #print(span.text)
            #print(a['href'])
            #print('\n')
            record.append((span.text , price, specifc_url, detail))
    
    return record
    


url ='https://store.steampowered.com/search/?filter=topsellers'
url_list=get_url(url)
record= top_seller(url_list)


#############
a= div.find_all('a', class_='search_result_row')[0]


specifc_url = a['href']
#driver.close()
driver.get(specifc_url)
soup=bs(driver.page_source,'lxml')

detail = soup.find('div', {'id':'game_area_description'})


#################################################

div = soup.find('div', {'id':'search_result_container'})
a=div.find
span= a.find('span')
price=a.find('div', class_='col search_price responsive_secondrow').text[1:].strip()
specifc_url = a['href']
#driver.close()
driver.get(specifc_url)
soup=bs(driver.page_source,'lxml')

detail = soup.find('div', {'id':'game_area_description'})
#print(span.text)
#print(a['href'])
#print('\n')
record.append((span.text , price, specifc_url, detail))


a= div.find_all('a', class_='search_result_row')[0]





########################################3
url='https://store.steampowered.com/search/?filter=topsellers'


driver.get(url)

soup = bs(driver.page_source, 'lxml')

# div id= search_result_container

div = soup.find('div', {'id':'search_result_container'})
record=[]
# class="search_result_row ds_collapse_flag "
#for a in div.find_all('a', class_='search_result_row'):

a=div.find_all('a', class_='search_result_row')[0]

title= a.find('span').text
price=a.find('div', class_='col search_price responsive_secondrow').text[1:].strip()
link=a['href']

driver.get(link)
soup = bs(driver.page_source,'lxml')
detail = soup.find('div', {'id':'game_area_description'})
print(detail.text)


print(span.text)
print(a['href'])
print('\n')
record.append((span, a['href']))


record=[]
for a in div.find_all('a', class_='search_result_row'):
    
    print(a)
    print(type(a))
    
    title = a.find('span').text
    price=a.find('div', class_='col search_price responsive_secondrow').text[1:].strip()
    link = a['href']
    print(title.text)
    print(a['href'])
    print(price)
    print('\n')
    record.append((title, price, link))


all_a= div.find_all('a',  class_='search_result_row')

a=all_a[0]

a.find('span').text
price=a.find('div', class_='col search_price responsive_secondrow').text[1:].strip()
link = a['href']

# col search_price  responsive_secondrow
#################
all_a= div.find_all('a',  class_='search_result_row')
num=len(all_a)

for i in range(num):
    a=all_a[i]
    title = a.find('span').text
    price_tmp=a.find('div', class_='col search_price_discount_combined responsive_secondrow').find_all('div')[1]
    price= price_tmp.text[1:].strip()
    link = a['href']
    
    print(title)
    
    print(link)
    print(price)


price_test = a.find('div', class_='col search_price_discount_combined responsive_secondrow')


a=[1,2,3,4,5]
b=[1,2,3,4,5]
c=[1,2,3,4,5]

dic={'a':a, 'b':b}
print(dic)

df=pd.DataFrame(dic)
d=pd.Series(c)

df[d]=d

df.d = pd.Series(c)




