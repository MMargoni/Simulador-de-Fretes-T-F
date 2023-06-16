# -*- coding: utf-8 -*-
"""
Created on Fri Jun 16 00:23:58 2023

@author: mmarg
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException

import time
import pandas as pd

ceps = pd.read_excel(r'D:\DADOS (1).xlsx', sheet_name='DADOS1')
ceps = ceps['CEPS'].tolist()

chrome_options = Options()
chrome_options.add_argument('--headless')  
chrome_options.add_argument('--disable-gpu')  

driver = webdriver.Chrome(options=chrome_options)    
driver.get('https://www.tf.com.br/top-basico-brilho--uva/p')
time.sleep(7)  

def tie(locator):
    try:
        driver.find_element(*locator)
        return True
    except NoSuchElementException:
        return False

locator = (By.CLASS_NAME,'trackfield-store-components-0-x-cookies-disclaimer__button')

if tie(locator):
    accept_button = driver.find_element(By.CLASS_NAME, 'trackfield-store-components-0-x-cookies-disclaimer__button')
    accept_button.click()
    time.sleep(2) 
else:
    time.sleep(2) 

frete = driver.find_element(By.CLASS_NAME, 'trackfield-shipping-simulator-0-x-shipping-simulator__input')  
calcularb = driver.find_element(By.CLASS_NAME, 'trackfield-shipping-simulator-0-x-shipping-simulator__button')
frete.send_keys(1)
frete.clear()
val = []

c = 0 
for cep in ceps:
    frete.send_keys(cep)
    calcularb.click()
    locator = (By.CLASS_NAME, 'trackfield-shipping-simulator-0-x-error')
    if tie(locator):
        val.extend("E")
    else:
        time.sleep(1)
        n = driver.find_element(By.CLASS_NAME, 'trackfield-shipping-simulator-0-x-shipping-list__price')
        nt = n.text
        if nt == 'Grátis':
         val.extend("0")
        else:
         val.extend(n.text)
    frete.clear()
    c += 1
    if c % 100 == 0:
        print(c)



