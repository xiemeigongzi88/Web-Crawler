# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 19:12:09 2019

@author: sxw17
"""

#url='https://www.cia.gov/library/publications/the-world-factbook/'

from selenium import webdriver
from bs4 import BeautifulSoup

#driver = webdriver.Chrome()
#driver.get(url)
url ='https://www.indeed.com/jobs?q=data+analyst&l=Dallas%2C+TX'
 


def get_soup(url):
    driver=webdriver.Chrome()
    driver.get(url)
    soup = BeautifulSoup(driver.page_source, 'lxml')
    driver.close()
    return soup 

page one:
'https://www.indeed.com/jobs?q=data+analyst&l=Dallas,+TX&start=0'

page two:
'https://www.indeed.com/jobs?q=data+analyst&l=Dallas%2C+TX&start=10'

url_basic='https://www.indeed.com/jobs?q=data+analyst&l=Dallas%2C+TX&start='

num=10

links=[]

for i in range(num+1):
    url='https://www.indeed.com/jobs?q=data+analyst&l=Dallas%2C+TX&start='
    link = url+str(10*i)
    links.append(link)
    
for i, link in enumerate(links):
    print(i,link)
    
# td id='resultsCol'
    
# import requests

link = links[0]

#response = requests.get(link)
    
#soup = BeautifulSoup(response.text, 'lxml')

#td=soup.find('td', attrs={'id':'resultsCol'})

# div class = 'jobsearch-SerpJobCard unifiedRow row result clickcard'

#div_all=td.find_all('div', class_='jobsearch-SerpJobCard unifiedRow row result clickcard')


##########################################
driver = webdriver.Chrome()
driver.get(link)

soup = BeautifulSoup(driver.page_source, 'lxml')
td=soup.find('td', attrs={'id':'resultsCol'})

div_all=td.find_all('div', class_='jobsearch-SerpJobCard unifiedRow row result clickcard')

div=div_all[0]

# div class= 'title'
title= div.find('div', class_='title').text.replace('\n','')
print(title)

description_info =div.find('div', class_='title')

# a target blank
description = description_info.find('a', attrs={'target':'_blank'})
description_link = 'https://www.indeed.com'+description['href']
print(description_link)

'''
https://www.indeed.com/pagead/clk?mo=r&ad=-6NYlbfkN0DdVgMPPqVTZ3Zw7YleYjiHVuuqNtn4z__DRsBmcGhhf4Bl4Fr7VSVqmycQ5cv9mOACatk_MAPO_iWPp3AXN6aXvDFfwy8za48FZbjrKSV1o61LHDKMF1hwgkey2zniZ4oIlcvUF3AYg4yu7IVOjLdTO399Lk-mjH1yT48tubM4BF0WUfAUOeXokHLh-9FTWVup9ljbzKltnryAj1VKOwnMg2siE0YlaXqQGZf3qJY_OYtBU9hFtTa9CTsqYK4t3MYTeqEUAnYuAhtev2klRc1xYTYwTPCbUhIq1RRshj11M8UZl5Un3GU0HrAVhTKSGPvoYujcY8QGO4fDxUA3DT1iiFDIxNFN7CQosAYRVtTzpOHzC19R3YM8ERboVr7QJa5WDDtqGPwvC5Kus3QY5UPuo-I9rRfnHJSmZL6pfwjfarwDmFUUOQ8C9bp_wh-oPmE=&p=0&fvj=1&vjs=3&tk=1djsru7sl33hm002&jsa=7989&sal=0&sal=0&sal=0&sal=0&oc=1&sal=0
'''

# dic class 'sjcl'

detail= div.find('div', class_='sjcl')
company = detail.find('span', class_='company').text.replace('\n','').strip()
print(company)

# span class='ratings'
ratings = detail.find('span', class_='ratings')['aria-label']
print(ratings)


# span class='slNoUnderline'
reviews_num = detail.find('span', class_='slNoUnderline').text
print(reviews_num)


# data-tn-variant : cmplinktst2 
reviews_link_info = str(detail.find('a', attrs={'data-tn-variant':'cmplinktst2'}))

reviews_link_list=reviews_link_info.split("href")

'''
https://www.indeed.com/cmp/Mv-Transportation/reviews?campaignid=cmplinktst2&from=SERP&jt=Data+Visualization+Analyst&fromjk=8eca2024a7678b52&jcid=664e666343e1f3d9
?campaignid=cmplinktst2&amp;from=SERP&amp;jt=Data+Visualization+Analyst&amp;
   fromjk=8eca2024a7678b52&amp;jcid=664e666343e1f3d9
'''
link_pre='https://www.indeed.com/'

link_mid= reviews_link_list[1][2:].split(' ')[0][:-1]

link_post = reviews_link_list[3].split(')')[0][3:-1]
    
job_link= link_pre+ link_mid + link_post
print(job_link)


# location 
# div class location accessible-contrast-color-location
location = detail.find('div', class_='location').text
print(location)

# summary 
# jobsearch-SerpJobCard unifiedRow row result clickcard
# div class summary 

summary = div.find('div', class_='summary')
print(summary)


# https://www.indeed.com/viewjob?
#cmp=MV-Transportation&t=Data+Visualization+Analyst&jk=8eca2024a7678b52&sjdu=QwrRXKrqZ3CNX5W-O9jEvQQqVrRMME8teBhMeanXvVh3svEDEhvDGJbN_JFBaZbFoqu_gU8nCdXWaPWhbO5pb1KEzPoMsvd9UKwxweExl_o&tk=1djsru7sl33hm002&adid=205457239&pub=4a1b367933fd867b19b072952f68dceb&vjs=3
    

# div class jobsearch-SerpJobCard-footer
# span class  sponsoredGray 
sponsor='NO'
sponsor_check = div.find('div', class_='result-link-bar').find('span').text

if sponsor_check:
    sponsor=sponsor_check

print(sponsor)


#####################################################################
link = links[0]



#################################################################################
#driver = webdriver.Chrome()
link=links[1]

driver.get(link)

soup = BeautifulSoup(driver.page_source, 'lxml')
td=soup.find('td', attrs={'id':'resultsCol'})

div_all=td.find_all('div', class_='jobsearch-SerpJobCard unifiedRow row result clickcard')

div=div_all[0]

title= div.find('div', class_='title').text.replace('\n','')
print(title)

description_info =div.find('div', class_='title')

description = description_info.find('a', attrs={'target':'_blank'})
description_link = 'https://www.indeed.com'+description['href']
print(description_link)

'''
https://www.indeed.com/pagead/clk?mo=r&ad=-6NYlbfkN0DdVgMPPqVTZ3Zw7YleYjiHVuuqNtn4z__DRsBmcGhhf4Bl4Fr7VSVqmycQ5cv9mOACatk_MAPO_iWPp3AXN6aXvDFfwy8za48FZbjrKSV1o61LHDKMF1hwgkey2zniZ4oIlcvUF3AYg4yu7IVOjLdTO399Lk-mjH1yT48tubM4BF0WUfAUOeXokHLh-9FTWVup9ljbzKltnryAj1VKOwnMg2siE0YlaXqQGZf3qJY_OYtBU9hFtTa9CTsqYK4t3MYTeqEUAnYuAhtev2klRc1xYTYwTPCbUhIq1RRshj11M8UZl5Un3GU0HrAVhTKSGPvoYujcY8QGO4fDxUA3DT1iiFDIxNFN7CQosAYRVtTzpOHzC19R3YM8ERboVr7QJa5WDDtqGPwvC5Kus3QY5UPuo-I9rRfnHJSmZL6pfwjfarwDmFUUOQ8C9bp_wh-oPmE=&p=0&fvj=1&vjs=3&tk=1djsru7sl33hm002&jsa=7989&sal=0&sal=0&sal=0&sal=0&oc=1&sal=0
'''


detail= div.find('div', class_='sjcl')
company = detail.find('span', class_='company').text.replace('\n','').strip()
print(company)


ratings = detail.find('span', class_='ratings')['aria-label']
print(ratings)


reviews_num = detail.find('span', class_='slNoUnderline').text
print(reviews_num)


reviews_link_info = str(detail.find('a', attrs={'data-tn-variant':'cmplinktst2'}))

reviews_link_list=reviews_link_info.split("href")


link_pre='https://www.indeed.com/'

link_mid= reviews_link_list[1][2:].split(' ')[0][:-1]

link_post = reviews_link_list[3].split(')')[0][3:-1]
    
job_link= link_pre+ link_mid + link_post
print(job_link)


location = detail.find('div', class_='location').text
print(location)

summary = div.find('div', class_='summary').text
print(summary)


sponsor='NO'
sponsor_check = div.find('div', class_='result-link-bar').find('span').text

if sponsor_check:
    sponsor=sponsor_check

print(sponsor)


###########################################

for i in links:
    print(i)


################################################################################

import time 

job_list=[]


for link in links:
    driver.get(link)
    
    soup = BeautifulSoup(driver.page_source, 'lxml')
    td=soup.find('td', attrs={'id':'resultsCol'})
    
    div_all=td.find_all('div', class_='jobsearch-SerpJobCard unifiedRow row result clickcard')
    
    for div in div_all:
    
        title= div.find('div', class_='title').text.replace('\n','')
        print(title)
        
        description_info =div.find('div', class_='title')
        
        description = description_info.find('a', attrs={'target':'_blank'})
        description_link = 'https://www.indeed.com'+description['href']
        print(description_link)
        
        '''
        https://www.indeed.com/pagead/clk?mo=r&ad=-6NYlbfkN0DdVgMPPqVTZ3Zw7YleYjiHVuuqNtn4z__DRsBmcGhhf4Bl4Fr7VSVqmycQ5cv9mOACatk_MAPO_iWPp3AXN6aXvDFfwy8za48FZbjrKSV1o61LHDKMF1hwgkey2zniZ4oIlcvUF3AYg4yu7IVOjLdTO399Lk-mjH1yT48tubM4BF0WUfAUOeXokHLh-9FTWVup9ljbzKltnryAj1VKOwnMg2siE0YlaXqQGZf3qJY_OYtBU9hFtTa9CTsqYK4t3MYTeqEUAnYuAhtev2klRc1xYTYwTPCbUhIq1RRshj11M8UZl5Un3GU0HrAVhTKSGPvoYujcY8QGO4fDxUA3DT1iiFDIxNFN7CQosAYRVtTzpOHzC19R3YM8ERboVr7QJa5WDDtqGPwvC5Kus3QY5UPuo-I9rRfnHJSmZL6pfwjfarwDmFUUOQ8C9bp_wh-oPmE=&p=0&fvj=1&vjs=3&tk=1djsru7sl33hm002&jsa=7989&sal=0&sal=0&sal=0&sal=0&oc=1&sal=0
        '''
        
        
        detail= div.find('div', class_='sjcl')
        company = detail.find('span', class_='company').text.replace('\n','').strip()
        print(company)
        
        
        try:
            ratings = detail.find('span', class_='ratings')['aria-label']
        except Exception:
            ratings="NULL"
            
        print(ratings)
        
        
        try:
            reviews_num = detail.find('span', class_='slNoUnderline').text
        except Exception:
            reviews_num='NULL'
    
        print(reviews_num)
        
        
        review_link=''
        try:
            reviews_link_info = str(detail.find('a', attrs={'data-tn-variant':'cmplinktst2'}))
            
            reviews_link_list=reviews_link_info.split("href")
            
            
            link_pre='https://www.indeed.com/'
            
            link_mid= reviews_link_list[1][2:].split(' ')[0][:-1]
            
            link_post = reviews_link_list[3].split(')')[0][3:-1]
                
            review_link= link_pre+ link_mid + link_post
            
            print(review_link)
        except Exception:
            review_link='NULL'
            print(company+' review link wait ...')
            
        location=''
        try:
            location = detail.find('div', class_='location').text
        except Exception:
            location='NULL'
        print(location)
        
        summary = div.find('div', class_='summary').text
        print(summary)
        
        
        sponsor='NO'
        sponsor_check = div.find('div', class_='result-link-bar').find('span').text
        
        if sponsor_check:
            sponsor=sponsor_check
        
        print(sponsor)
        
        job_list.append((title, company, ratings, sponsor, summary, reviews_num, review_link, location, description_link))
    
        time.sleep(5)


import pandas as pd 
df = pd.DataFrame(job_list)



########################################################################















    
    