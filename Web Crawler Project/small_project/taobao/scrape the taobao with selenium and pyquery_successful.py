# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 20:09:39 2019

@author: sxw17
"""
# scrape the taobao with selenium and pyquery
from time import sleep
from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#from config import *
import pymongo

MOBGO_URL = 'localhost'
MONGO_DB= 'taobao'
MONGO_TABLE='product'

client=pymongo.MongoClient(host='localhost', port=27017)
db= client[MONGO_DB]


driver = webdriver.Chrome()
driver.implicitly_wait(5)
wait=WebDriverWait(driver,3)

url= 'https://login.taobao.com/member/login.jhtml'

def scan_login(url):
    driver.get(url)
    # wait for the scan QR code finishing 
    sleep(15)
    # enter the taobao

scan_login(url)



def search():
    try:
        url='https://world.taobao.com/'
        driver.get(url)
        # css #mq
        input_ = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#mq"))
        )
        # #J_PopSearch > div.sb-search > div > form > input[type=submit]:nth-child(2)
        # css #J_PopSearch > div.sb-search > div > form > input[type=submit]:nth-child(2)
        submit_ = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"#J_PopSearch > div.sb-search > div > form > input[type=submit]:nth-child(2)")))
        
        input_.send_keys('iphone')
        submit_.click()
        
        total = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#mainsrp-pager > div > div > div > div.total")))
        return total.text
    except TimeoutException:
        return search()
                                                       
                                                       
import re 

def next_page(page_number):
    # input css: #mainsrp-pager > div > div > div > div.form > input
    # submit css: #mainsrp-pager > div > div > div > div.form > span.btn.J_Submit
    
    try:
        input_=wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'#mainsrp-pager > div > div > div > div.form > input')))
        submit_=wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#mainsrp-pager > div > div > div > div.form > span.btn.J_Submit')))
    
        # confirmation css: 
        input_.clear()
        input_.send_keys(page_number)
        submit_.click()
        # checking number 
        
        wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, '#mainsrp-pager > div > div > div > ul > li.item.active > span'), str(page_number)))
                                                     
        record= get_baby()  
        return record                                           
    except TimeoutException:
        next_page(page_number)
           

from pyquery import PyQuery as pq 
                                        
def get_baby():
    # id              #mainsrp-itemlist
    # itemlists css : #mainsrp-itemlist
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#mainsrp-itemlist .items .item')))
    html=driver.page_source
    doc = pq(html)
    items=doc('#mainsrp-itemlist .items .item').items()
    
    baby_list=[]    
    for item in items:
        # pic: #mainsrp-itemlist > div > div > div:nth-child(1) > div:nth-child(1) > div.pic-box.J_MouseEneterLeave.J_PicBox > div > div.pic
        # Note: shoule be checked again 
        product = {
                'image': item.find('.pic .img').attr('src'),
                'price': item.find('.price').text(),
                'deal': item.find('.deal-cnt').text(),
                'title':item.find('.title').text(),
                'shop': item.find('.shop').text(),
                'location': item.find('.location').text()
                
                }
        print(product)
        save_to_mongo(product)
    

def save_to_mongo(result):
    try:
        if db[MONGO_TABLE].insert(result):
            print("save successfully", result)
    except Exception:
        print("save fail", result)
        
                                      
def main():
    total = search()
    total= int(re.compile('(\d+)').search(total).group(1))
    print(total)
 
    for i in range(2, 5):
        record=next_page(i)
   
if __name__=='__main__':
    main()
