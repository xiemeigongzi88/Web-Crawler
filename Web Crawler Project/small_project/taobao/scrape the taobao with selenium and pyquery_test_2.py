# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 14:24:28 2019

@author: sxw17
"""

from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


browser = webdriver.Chrome()
wait=WebDriverWait(browser,3)
#url='https://world.taobao.com/'

url='https://world.taobao.com/'
browser.get(url)

'''
# login css selector  
#J_7607074463 > div > div > div > div > div.user-info.oversea-head.user-info-unlogin > p > a:nth-child(1)
input_1= browser.find_element_by_css_selector('#J_7607074463 > div > div > div > div > div.user-info.oversea-head.user-info-unlogin > p > a:nth-child(1)').click()
input_1.send_keys('邪美公子88')
# #J_Form > div.field.username-field > span
input_2=browser.find_element_by_css_selector('#J_Form > div.field.username-field > span').click()
input_2.
# #TPL_password_1
browser.find_element_by_css_selector('#TPL_password_1').click()                                
                                     
'''
                                     
# login taobao 
# #J_7607074463 > div > div > div > div > div.user-info.oversea-head.user-info-unlogin > p > a:nth-child(1)

# click the login 
button = browser.find_element_by_css_selector('#J_7607074463 > div > div > div > div > div.user-info.oversea-head.user-info-unlogin > p > a:nth-child(1)')
button.click()                                              

# input name 
#  #J_Form > div.field.username-field > span
input_1 =wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,"#J_Form > div.field.username-field > span"))).click()
input_1.send_keys("邪美公子88")                                                    
                                                    
submit_1=wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"#J_Form > div.field.username-field > span")))   
                                                 
'''
CSS_Selector: #mq
'''

input_ = wait.until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "#mq")))

# submit #J_PopSearch > div.sb-search > div > form > input[type=submit]:nth-child(2)
submit_= wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"#J_PopSearch > div.sb-search > div > form > input[type=submit]:nth-child(2)")))
input_.send_keys('iphone')
submit_.click()



########################################################################


import time
import datetime
import sys
import os
import random

import logging

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
#rom selenium import webdriver
option = webdriver.ChromeOptions()
option = webdriver.ChromeOptions()
option.add_experimental_option('excludeSwitches',['enable-automation'])

browser = webdriver.Chrome(options=option)



def common_click(driver,element_id,sleeptime=3):
  actions = ActionChains(driver)
  actions.move_to_element(element_id)
  actions.click(element_id)
  actions.perform()
  time.sleep(sleeptime) 


def login_in(user,pwd):
  #open login page
  browser.get('https://login.taobao.com/member/login.jhtml')
  time.sleep(3)
  '''
  sb=driver.find_element_by_class_name("login-switch")
  commonclick(driver,sb)
  '''
  # #J_Form > div.field.username-field > span
  # id TPL_username_1
  userbox=browser.find_element_by_id('TPL_username_1')
  pwdbox=browser.find_element_by_id("TPL_password_1")
  userbox.clear()
  userbox.send_keys(user)
  common_click(browser,pwdbox) 
  pwdbox.send_keys(pwd)
  loadmore=browser.find_element_by_id("J_SubmitStatic")
  common_click(browser,loadmore)
  time.sleep(20)

browser = webdriver.Chrome()

webdriver = window.navigator.webdriver
if(webdriver){
	console.log('你这个傻逼你以为使用Selenium模拟浏览器就可以了？')
} else {
	console.log('正常浏览器')
}


login_in('邪美公子88','WS@abel1989')





# login page 
# https://world.taobao.com/markets/all/login 
  
# <span class="ph-label" data-spm-anchor-id="a2107.1.0.i1.1241PGTbPGTbEc">会员名/邮箱</span>
# css   #J_Form > div.field.username-field > span
  
#  css  #TPL_password_1

def common_click(driver,element_id,sleeptime=3):
  actions = ActionChains(driver)
  actions.move_to_element(element_id)
  actions.click(element_id)
  actions.perform()
  time.sleep(sleeptime) 


def login_in(user,pwd):
  #open login page
  browser.get('https://login.taobao.com/member/login.jhtml')
  time.sleep(3)
  # #J_Form > div.field.username-field > span
  sb=browser.find_element_by_css_selector("#J_Form > div.field.username-field > span")
  commonclick(browser,sb)
  
  userbox=driver.find_element_by_id("TPL_username_1")
  pwdbox=driver.find_element_by_id("TPL_password_1")
  userbox.clear()
  userbox.send_keys(user)
  commonclick(driver,pwdbox) 
  pwdbox.send_keys(pwd)
  loadmore=driver.find_element_by_id("J_SubmitStatic")
  commonclick(driver,loadmore)
  time.sleep(20)


####################################################################
  
from time import sleep
from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import *
import pymongo

MOBGO_URL = 'localhost'
MONGO_DB= 'taobao'
MONGO_TABLE='product'

client=pymongo.MongoClient(host='localhost', port=27017)
db= client[MONGO_DB]


driver = webdriver.Chrome()
driver.implicitly_wait(5)
def scan_login(url):
    driver.get(url)
    # 等待扫码登录
    sleep(15)
    # 进入之后开始其他操作

url= 'https://login.taobao.com/member/login.jhtml'

scan_login(url)

wait=WebDriverWait(driver,3)

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
           

from bs4 import BeautifulSoup as bs 
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





