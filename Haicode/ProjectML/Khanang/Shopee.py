#thu vien ho tro tinh toan, xu li du lieu
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#thu vien ho tro scrapping
from selenium import webdriver #(pip install selenium)
from webdriver_manager.chrome import ChromeDriverManager #pip install webdriver_manager
from bs4 import BeautifulSoup #pip install bs4
from time import sleep
#thu vien xu ly thuat toan k-means
from sklearn.cluster import KMeans #pip install pip install -U scikit-learn
from sklearn.preprocessing import MinMaxScaler 


url = 'https://shopee.com' #base url
sp = 'nuoc rua bat'
driver = webdriver.Chrome(ChromeDriverManager().install()) #khoi tao cua so scrapping tu chrome
#cac thong so scrapping tu shopee
name= []
price = []
local = []
sold = []
thinglist = []
id = 0
for i in range(0,10):
    driver.get(f'https://shopee.vn/search?keyword={sp}&page={i}') #load du lieu tu trinh duyet chrome, so tring i
    sleep(2) #delay de load trang web 
    for x in range(0,3800,300):
        driver.execute_script(f"window.scrollTo(0, {x})") #lan con tro de load het du lieu tu shopee
    sleep(1)
    soup = BeautifulSoup(driver.page_source, 'html.parser') #khoi tao thu vien bs4 lay du lieu html tu pagesource
    lists = soup.find_all('div', {'class':'col-xs-2-4 shopee-search-item-result__item'})
    #scrapping data tu shopee
    for item in lists:
        id = id + 1 #danh so thu tu san pham
        rates = 0   #khoi tao thong so 'rate'
        links = []
        links = item.find('a', href = True)
        if links is not None:
            links = links['href'] #crapping link tu shopee
        else:
            links = np.nan  
        #scrapping gia tu shopee
        price = item.find('span', {'class':'_24JoLh'})
        if price is not None:
            intprice = np.int32(price.text.strip().replace('.',''))
        else:
            intprice = 1000
        #scrapping ten san pham tu shopee
        name = item.find('div', {'class':'yQmmFK _1POlWt _36CEnF'})
        if name is not None:
            name = name.text.strip()
        else:
            name = np.nan
        #scrapping dia diem ban tu shopee
        local = item.find('div',{'class':'_2CWevj'})
        if local is not None:
            local = local.text.strip()
        else:
            local = np.nan
        #gia ban
        sold = item.find('div',{'class':'go5yPW'})
        if sold is not None:
            sold = sold.text.strip()
            intsold = sold.replace('Đã bán ','')
            
            if 'k' in intsold: 
                intsold = int(intsold.replace('k', '').replace(',', ''))
            else:
                if intsold == '' : 
                    intsold = 0
                else:
                    intsold = int(intsold)
        else:
            sold = np.nan
        #rate
        for rate in item.find_all('div', {'class':'shopee-rating-stars__star-wrapper'}):
            rates = rates + 1