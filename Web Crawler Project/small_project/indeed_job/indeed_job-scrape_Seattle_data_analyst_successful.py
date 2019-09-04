# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 10:17:36 2019

@author: sxw17
"""

## seattle wa , data analyst 

import time 
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd 

# basic url ='https://www.indeed.com/jobs?q=data+analyst&l=Seattle,+WA&start='


def get_pages():
    # the number of page you can change 
    num =50 
    links=[]
    for i in range(num+1):
        url='https://www.indeed.com/jobs?q=data+analyst&l=Seattle,+WA&start='
        link = url+str(10*i)
        links.append(link)
        
    for i, link in enumerate(links):
        print(i,link)
        
    return links


def get_jobs(links):
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
            
    return job_list


pages_links=get_pages()
driver=webdriver.Chrome()
record = get_jobs(pages_links)

df = pd.DataFrame(record)
df.columns=['title', 'company', 'ratings', 'sponsor', 'summary', 'reviews_number', 'review_link', 'location', 'description_link']
df.drop(['summary'],axis=1,inplace=True)

df.to_csv('Seattle_Data_analyst_jobs_without_summary.csv')
