# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 13:54:09 2019

@author: sxw17
"""

from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


browser = webdriver.Chrome()
wait=WebDriverWait(browser,10)
url='https://world.taobao.com/'

def search():
    url='https://world.taobao.com/'
    browser.get(url)
    
    '''
    CSS_Selector: #mq
    '''
    
    input_ = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#mq")))
    
    # submit #J_PopSearch > div.sb-search > div > form > input[type=submit]:nth-child(2)
    submit_= wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"#J_PopSearch > div.sb-search > div > form > input[type=submit]:nth-child(2)")))
    input_.send_keys('iphone')
    submit_.click()
    
def main():
    search()
    
if __name__=='__main__':
    main()
    
    
                                                    
                                                    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        