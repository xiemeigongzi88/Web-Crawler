# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 21:51:20 2019

@author: sxw17
"""

from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd 
import requests

# baobaosmallmaomao@gmail.com
driver=webdriver.Chrome()

def get_info_pages():
    basic_url='https://www.indeed.com/jobs?q=data+analyst&l=Seattle,+WA&start='
    page=10
    
    links=[]
    
    for i in range(page+1):
        url= basic_url+str(i*10)
        links.append(url)
        
    return links 

links = get_info_pages()

def get_jobs(links):
    
    job_list=[]
    
    cnt_page =0 
    for link in links:
        
        cnt_jobs =1
        driver.get(link)
        soup = BeautifulSoup(driver.page_source,'lxml')
        td= soup.find('td',attrs={'id':'resultsCol'})
        
        div_all=td.find_all('div', class_='jobsearch-SerpJobCard unifiedRow row result clickcard')

        try:
            for div in div_all:
                
                # 1. title 
                title= div.find('div', class_='title').text.replace('\n','')
                description_info =div.find('div', class_='title')
                
                # 9. job description
                description = description_info.find('a', attrs={'target':'_blank'})
                description_link = 'https://www.indeed.com'+description['href']
                
                detail= div.find('div', class_='sjcl')
                
                # 2. company name 
                company = detail.find('span', class_='company').text.replace('\n','').strip()
                
                # 3. ratings 
                ratings = detail.find('span', class_='ratings')['aria-label']
    
                # 6. review nums
                reviews_num = detail.find('span', class_='slNoUnderline').text
    
                reviews_link_info = str(detail.find('a', attrs={'data-tn-variant':'cmplinktst2'}))
    
                reviews_link_list=reviews_link_info.split("href")
    
                link_pre='https://www.indeed.com/'
    
                link_mid= reviews_link_list[1][2:].split(' ')[0][:-1]
    
                link_post = reviews_link_list[3].split(')')[0][3:-1]
                
                # 7. review_link
                job_link= link_pre+ link_mid + link_post
                
                # 8. location 
                location = detail.find('div', class_='location accessible-contrast-color-location').text
                
                # 5. simple summary
                summary = div.find('div', class_='summary').replace('<b>','')
                
                # 4. sponsor or not 
                
                sponsor = div.find('div', class_='result-link-bar').find('span').text
                
                if sponsor:
                    sponsor=sponsor
                else:
                    sponsor='Not'
                
                job_list.append((title, company, ratings, sponsor, summary, reviews_num, job_link, location, description_link))
                
                cnt_jobs+=1
        except Exception:
            print(str(cnt_page)+' - '+str(cnt_jobs))
        
        cnt_page +=1 
    return job_list

record = get_jobs(links)


            
            




    
    