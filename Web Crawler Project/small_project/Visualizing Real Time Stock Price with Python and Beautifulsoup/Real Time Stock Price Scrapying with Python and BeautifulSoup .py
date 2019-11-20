# -*- coding: utf-8 -*-
"""
Created on Wed Jul 24 09:51:17 2019

@author: sxw17
"""

# Real Time Stock Price Scrapying with Python and BeautifulSoup 
import os 
os.getcwd()
os.chdir('C:\\Users\\sxw17\\Desktop\\python learning\\Python_Data\\Customizing Matplotlib Graphs and Charts\\Python Charting Stocks Forex for Technical Analysis')



from bs4 import BeautifulSoup
import requests
import time



# get price 
#soup.find_all('div', {'calss':'D(ib) Mend(20px)'})

my_6px= soup.find_all('div',{'class':'My(6px) Pos(r) smartphone_Mt(6px)'})[0]

price = my_6px.find('span').text


# get the current price 
def parsePrice():
    url= 'https://finance.yahoo.com/quote/fb/'
    response= requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    
    my_6px= soup.find_all('div',{'class':'My(6px) Pos(r) smartphone_Mt(6px)'})[0]

    price = my_6px.find('span').text
    
    return price


while True:
    print('the current price：' ,str(parsePrice()))
    
    time.sleep(2)
    
    