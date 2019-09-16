# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 11:08:02 2019

@author: sxw17
"""

import pandas as pd
import os 
import time 
os.chdir('C:\\Users\\sxw17\\Desktop\\DATA\\Project\\Data Analysis\\sexy panties')

df = pd.read_csv('detail_item_info.csv')

item_links = df['item_link']

def get_product_info(item_links):
    
    specific_item_info=[]
    
    for i, link in enumerate(item_links):
        print(i, link)
        driver = webdriver.Chrome()

        driver.get(link)
        
        soup = BeautifulSoup(driver.page_source,'lxml')
        shop_info = soup.find('div', attrs={'id':'titleBlock'})
        
        try:
            # div class a-section a-spacing-none 
            shop_info = soup.find('div', attrs={'id':'titleBlock'})
            shop_name = shop_info.find('div', class_='a-section a-spacing-none').text.strip() # ok 1-1
            
            pre_link = 'https://www.amazon.com'
            post_link = shop_info.find('a', class_='a-link-normal')['href']
            shop_link = pre_link+post_link  # pretend to be true  # 7. ok 
            
            # span id productTitle
            product_title = shop_info.find('span', attrs={'id':'productTitle'}).text.strip()  # 2. ok
            
            # span id  acrCustomerReviewText
            review_num= shop_info.find('span', attrs={'id':'acrCustomerReviewText'}).text.split(' ')[0] # 5. ok 
            
            star = soup.find('span', class_='a-icon-alt').text  # 3. ok 
            
            try:
                # span class a-size-medium a-color-price priceBlockSalePriceString
                price=soup.find('span', class_='a-size-medium a-color-price priceBlockSalePriceString').text.strip()
                #price = soup.find('spn', class_='a-size-medium a-color-price priceBlockSalePriceString').text.strip()
            except Exception as e:
                print(str(e)+' price wrong type1')
                price_id = soup.find('tr', attrs={'id':'priceblock_ourprice_row'})
                price = price_id.find('span', attrs ={'id':'priceblock_ourprice'}).text # 4. ok 
            except Exception as e:
                # priceblock_saleprice
                price=soup.find('span', attrs={'id':'priceblock_saleprice'}).text
                print(str(e)+' price wrong type 2')
            except Exception as e:
                # priceblock_saleprice
                price=soup.find('span', attrs={'id':'price_inside_buybox'}).text.strip()
                print(str(e)+' price wrong type 3 ')
            except Exception as e:
                price=soup.find('span', attrs={'id':'priceblock_ourprice'}).text.strip()
                print(str(e)+' price wrong type 4 ')
            except Exception as e:
                #price=soup.find('span', class_='a-size-medium a-color-price priceBlockSalePriceString').text.strip()
                price = soup.find('span', class_='a-size-medium a-color-price priceBlockSalePriceString').text.strip()
                print(str(e)+' price wrong type 5')
            except Exception as e:
                price = soup.find('span', class_='a-size-medium a-color-price priceBlockSalePriceString').text.strip()
                print(str(e)+' price wrong type 6')
            
        except Exception as e:
            # span id productTitle
            shop_info = soup.find('div', attrs={'id':'titleSection'})
            product_title = shop_info.find('span', attrs={'id':'productTitle'}).text.strip() # ok1-2
  
            
            # div class a-section a-spacing-none
            # a id  bylineInfo 
            shop_name = soup.find('a', attrs={'id':'bylineInfo'}).text
            
            pre_link = 'https://www.amazon.com'
            post_link = soup.find('a', attrs={'id':'bylineInfo'})['href']
            shop_link = pre_link+post_link  # pretend to be true  # 7. ok 
            
            # span id productTitle
            # product_title = shop_info.find('span', attrs={'id':'productTitle'}).text.strip()  # 2. ok
            
            # span id  acrCustomerReviewText
            # acrCustomerReviewText
            try:
                review_num= soup.find('span', attrs={'id':'acrCustomerReviewText'}).text.split(' ')[0]
                
            except Exception as e:
                review_num=None
                print('review_num wrong ! '+str(e))
                
            try:
                star = soup.find('span', class_='a-icon-alt').text  # 3. ok 
            except Exception as e:
                star=None
                print('star wrong! '+str(e))
                
            price_id = soup.find('tr', attrs={'id':'priceblock_ourprice_row'})
            price = price_id.find('span', attrs ={'id':'priceblock_ourprice'}).text # 4. ok 
            
        
        try:
            div_tag = soup.find('div', class_='cr-lighthouse-terms')
            div_span = div_tag.find_all('span', class_='a-declarative')
            reviews_mention = []  # 6. ok 
            
            for span in div_span:
                reviews_mention.append(span.text.strip())
        except Exception as e:
            print('Review mention wrong! '+str(e))
            reviews_mention=None
            
        
        try:
            reviews_info = soup.find('div', attrs={'id':'cm-cr-dp-review-list'})
            review_list=reviews_info.find_all('div', class_='a-section review aok-relative')  
            
            for review in review_list:
                profile_name = review.find('span', class_='a-profile-name').text  # 8. ok
                profile_star = review.find('span', class_='a-icon-alt').text  # 9.  ok 
                
                # a data-hook = review-title
                review_title = review.find('a', attrs={'data-hook':'review-title'}).text.strip()  # 10. ok 
                
                # a data-hook review-date
                review_date = review.find('span', attrs={'data-hook':'review-date'}).text  # 11. ok 
                
                # span data-hook format-strip-linkless
                try:
                    size= review.find('span', attrs={'data-hook':'format-strip-linkless'}).text.split('Color')[0]  # 12. ok 
                    #color ='Color'+review.find('span', attrs={'data-hook':'format-strip-linkless'}).text.split('Color')[1]  # 13. ok 
                except Exception as e:
                    size=None 
                    print('size  error! '+str(e))
                
                try:
                    color ='Color'+review.find('span', attrs={'data-hook':'format-strip-linkless'}).text.split('Color')[1]  # 13. ok 
                except Exception as e:
                    color =None
                    print('color error! '+str(e))
                    
                # div data-hook review-collapsed
                review_text = review.find('div', attrs={'data-hook':'review-collapsed'}).find('span').text  # 14. ok 
                specific_item_info.append((shop_name, product_title, star, price, review_num, 
                                       reviews_mention, shop_link, profile_name,profile_star, 
                                       review_title, review_date,size, color, review_text))
                
                time.sleep(3)
                
        except Exception as e:
            print(str(e))
                
    return specific_item_info

df_1 = get_product_info(item_links[:30])

df_2 = get_product_info(item_links[30:60])

df_3_1 =get_product_info(item_links[60:63])  # unsuccessful
df_3_2 = get_product_info(item_links[65:90])

df_4= get_product_info(item_links[90:120])

df_5= get_product_info(item_links[120:140])

df_6 =get_product_info(item_links[140:142])  

df_7 = get_product_info(item_links[143:156])

df_8 = get_product_info(item_links[157:180])

df_9 = get_product_info(item_links[180:183])

df_10 = get_product_info(item_links[187:200])

df_11 = get_product_info(item_links[200:220])

df_12 = get_product_info(item_links[220:240])

df_13 = get_product_info(item_links[240:260])

df_14 = get_product_info(item_links[260:280])

df_15 = get_product_info(item_links[280:298])

df_16 = get_product_info(item_links[299:320])

df_17 = get_product_info(item_links[320:340])

df_18 = get_product_info(item_links[340:360])

df_19 = get_product_info(item_links[360:390])


df_1_record = pd.DataFrame(df_1)
df_2_record = pd.DataFrame(df_2)

df_3_1_record = pd.DataFrame(df_3_1)
df_3_2_record = pd.DataFrame(df_3_2)
df_4_record = pd.DataFrame(df_4)
df_5_record = pd.DataFrame(df_5)
df_6_record = pd.DataFrame(df_6)
df_7_record = pd.DataFrame(df_7)
df_8_record = pd.DataFrame(df_8)
df_9_record = pd.DataFrame(df_9)
df_10_record = pd.DataFrame(df_10)
df_11_record = pd.DataFrame(df_11)
df_12_record = pd.DataFrame(df_12)
df_13_record = pd.DataFrame(df_13)
df_14_record = pd.DataFrame(df_14)
df_15_record = pd.DataFrame(df_15)
df_16_record = pd.DataFrame(df_16)
df_17_record = pd.DataFrame(df_17)
df_18_record = pd.DataFrame(df_18)
df_19_record = pd.DataFrame(df_19)

frames=[df_1_record,df_2_record,df_3_1_record,df_3_2_record,df_4_record,df_5_record,df_6_record,df_7_record,
         df_8_record,df_9_record,df_10_record,df_11_record,df_12_record,df_13_record,df_14_record,df_15_record,df_16_record,df_17_record,df_18_record,df_19_record]

df_records= pd.concat(frames)

result = df_records.copy()

result.columns=['shop_name', 'product_title', 'star', 'price', 'review_num', 
                                       'reviews_mention', 'shop_link', 'profile_name',
                                       'profile_star', 
                                       'review_title', 'review_date','size', 'color', 'review_text']
    
result.to_csv('each_description_review.csv')