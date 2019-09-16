# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 23:28:46 2019

@author: sxw17
"""
# 
links = ['https://www.amazon.com/s?k=sexy+panties+for+women&crid=26GKVG63H487M&qid=1568504711&sprefix=sexy+pan%2Caps%2C162&ref=sr_pg_1',
 'https://www.amazon.com/s?k=sexy+panties+for+women&page=2&crid=26GKVG63H487M&qid=1568507071&sprefix=sexy+pan%2Caps%2C162&ref=sr_pg_2',
 'https://www.amazon.com/s?k=sexy+panties+for+women&page=3&crid=26GKVG63H487M&qid=1568507071&sprefix=sexy+pan%2Caps%2C162&ref=sr_pg_3',
 'https://www.amazon.com/s?k=sexy+panties+for+women&page=4&crid=26GKVG63H487M&qid=1568507071&sprefix=sexy+pan%2Caps%2C162&ref=sr_pg_4',
 'https://www.amazon.com/s?k=sexy+panties+for+women&page=5&crid=26GKVG63H487M&qid=1568507071&sprefix=sexy+pan%2Caps%2C162&ref=sr_pg_5',
 'https://www.amazon.com/s?k=sexy+panties+for+women&page=6&crid=26GKVG63H487M&qid=1568507071&sprefix=sexy+pan%2Caps%2C162&ref=sr_pg_6',
 'https://www.amazon.com/s?k=sexy+panties+for+women&page=7&crid=26GKVG63H487M&qid=1568507071&sprefix=sexy+pan%2Caps%2C162&ref=sr_pg_7']


def get_items_detail(links):
    
    detail_info=[]
    for link in links:
        driver.get(link)

        soup= BeautifulSoup(driver.page_source, 'lxml')
        
        div_items = soup.find_all('div', class_='a-section a-spacing-medium')
        
        for div in div_items:
            name = div.find('h5', class_="s-line-clamp-1").text.strip() # ok 

            # text span class class="a-size-base-plus a-color-base a-text-normal"
    
            # a class a-link-normal a-text-normal
            post_link = div.find('a', class_='a-link-normal a-text-normal')['href']
            pre_link = 'https://www.amazon.com'
            
            item_link = pre_link+ post_link
            img_src = div.find('div', class_='a-section aok-relative s-image-tall-aspect').find('img')['src']
            
            '''
            try:
                # span class   a-icon-alt
                total_rank = div.find('span', class_='a-icon-alt').text
                #pure_rank = total_rank.split(' ')[0]
            except Exception as e:
                print(str(e)+ ' rank_pbl '+ name + '\n'+ item_link)
                total_rank= None
                #pure_rank= None 
                '''
            try:
                text = div.find('span', class_='a-size-base-plus a-color-base a-text-normal').text.strip()  # ok 
            except Exception as e:
                print(str(e)+ ' description '+ name + '\n'+ item_link)
                text=None 
            # div class a-section aok-relative s-image-tall-aspect
            
            
            detail_info.append((name, text, item_link, img_src))
            
            time.sleep(5)

    return detail_info

detail_info=get_items_detail(links)

import pandas as pd 

df= pd.DataFrame(detail_info)
df.columns=['item_name','description', 'item_link', 'img_src']

df.to_csv('detail_item_info.csv')
