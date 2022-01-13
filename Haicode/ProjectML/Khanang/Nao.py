import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
from time import sleep
from sklearn.cluster import KMeans
from sklearn.preprocessing import MinMaxScaler
# import requests


url = 'https://shopee.com'
driver = webdriver.Chrome(ChromeDriverManager().install())
sp = 'nước%20rửa%20bát'
name= []
price = []
local = []
sold = []
thinglist = []
id = 0
for i in range(0,10):
    driver.get(f'https://shopee.vn/search?keyword={sp}&page={i}')
    # driver.request(f'https://shopee.vn/search?keyword={sp}&page={i}')
    sleep(2)
    for x in range(0,3800,300):
        driver.execute_script(f"window.scrollTo(0, {x})") 
    sleep(1)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    lists = soup.find_all('div', {'class':'col-xs-2-4 shopee-search-item-result__item'})
    for item in lists:
        id = id + 1
        rates = 0
        links = []
        links = item.find('a', href = True)
        if links is not None:
            links = links['href']
        else:
            links = np.nan        
    ##################################
        price = item.find('span', {'class':'_24JoLh'})
        if price is not None:
            intprice = np.int32(price.text.strip().replace('.',''))
        else:
            intprice = 1000
    ##################################
        name = item.find('div', {'class':'yQmmFK _1POlWt _36CEnF'})
        if name is not None:
            name = name.text.strip()
        else:
            name = np.nan
    #################################
        local = item.find('div',{'class':'_2CWevj'})
        if local is not None:
            local = local.text.strip()
        else:
            local = np.nan
    ################################
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
    ############################### 
        for rate in item.find_all('div', {'class':'shopee-rating-stars__star-wrapper'}):
            rates = rates + 1
        things = {
            'id' : id,
            'name' : name,
            'price' : intprice,
            'local' : local,
            'link' : links,
            'rate' : rates,
            'sold' : intsold
        }
        thinglist.append(things)
    print(f'Loangding...{(i+1)*len(range(0,10))}%' )   
driver.close()
sr = pd.DataFrame(thinglist)
mapper = { 'An Giang': 3,'Bà rịa – Vũng tàu':3, 'Bắc Giang':3,'Bắc Kạn':3,'Bạc Liêu':3,'Bắc Ninh':3,'Bến Tre':3,'Bình Định':3,'Bình Dương':3, 'Bình Phước':3, 	'Bình Thuận':3, 	'Cà Mau':3, 	'Cần Thơ':3,	'Cao Bằng':3, 	'Đà Nẵng':3,'Đắk Lắk':3,	'Đắk Nông':3, 	'Điện Biên':3, 	'Đồng Nai':3, 	'Đồng Tháp':3,	'Gia Lai':3, 	'Hà Giang':3, 	'Hà Nam':3, 	'Hà Nội': 1, 'Hà Tĩnh':3, 	'Hải Dương':3, 	'Hải Phòng':3, 	'Hậu Giang':3, 	'Hòa Bình':3,	'Hưng Yên':3, 	'Khánh Hòa':3,	'Kiên Giang':3, 	'Kon Tum':3, 	'Lai Châu':3, 	'Lâm Đồng':3, 	'Lạng Sơn':3, 	'Lào Cai':3,	'Long An':3, 	'Nam Định':3,	'Nghệ An':3,	'Ninh Bình':3, 	'Ninh Thuận':3, 	'Phú Thọ':3, 	'Phú Yên':3, 'Quảng Bình':3,'Quảng Nam':3, 'Quảng Ngãi':3, 'Quảng Ninh':3, 'Quảng Trị':3, 'Sóc Trăng':3, 'Sơn La':3,'Tây Ninh':3, 'Thái Bình':3,'Thái Nguyên':3,'Thanh Hóa':3,'Thừa Thiên Huế':3, 'Tiền Giang':3, 	'TP. Hồ Chí Minh' : 2, 'Trà Vinh':3,'Tuyên Quang':3,'Vĩnh Long':3, 'Vĩnh Phúc':3 ,'Yên Bái':3, 'Nước ngoài':3, 'NaN' : 0}
sr['local'] = sr['local'].map(mapper)
# df = sr[['price', 'local', 'sold']]
df = sr[['price', 'sold']]
df_np = df.to_numpy()
df_np = np.nan_to_num(df_np)

scaler = MinMaxScaler()
df_np = scaler.fit_transform(df_np)


sum_distances = []
K = range(1,15)
for k in K:
  k_mean = KMeans(n_clusters=k)
  k_mean.fit(df_np)
  sum_distances.append(k_mean.inertia_) #bình phuong khoang cach đến tâm cụm của tất cả các điểm
plt.plot(K, sum_distances, 'bx-')
plt.show()



def Nao(a, c):
#build model
    k_mean_4 = KMeans(n_clusters=4)
    model = k_mean_4.fit(df_np)
    result = k_mean_4.labels_
    plt.scatter(df_np[:,0], df_np[:,1])

    plt.scatter(
        df_np[result == 0, 0], df_np[result == 0, 1],
        c='lightgreen',
        marker='s', edgecolor='black',
        label='cluster 1'
    )
    plt.scatter(
        df_np[result == 1, 0], df_np[result == 1, 1],
        c='orange',
        marker='o', edgecolor='black',
        label='cluster 2'
    )
    plt.scatter(
        df_np[result == 2, 0], df_np[result == 2, 1],
        c='lightblue',
        marker='v', edgecolor='black',
        label='cluster 3'
    )
    plt.scatter(
        df_np[result == 3, 0], df_np[result == 3, 1],
        c='black',
        marker='v', edgecolor='black',
        label='cluster 4'
    )
    plt.scatter(
        model.cluster_centers_[:, 0], model.cluster_centers_[:, 1],
        s=250, marker='*',
        c='red', edgecolor='black',
        label='centroids'
    )
    plt.legend(scatterpoints=1)
    plt.grid()
    plt.show()

    df1 = sr[['id', 'price', 'rate', 'local', 'sold']]
    df2 = sr[['id', 'name', 'link']]
    searchs = df1.merge(df2, on= 'id', how= 'right')
    searchs['cluster'] = result
    arr = np.array([[a, c]])
    # arr = np.array([[a, b, c]])
    pred = model.predict(arr)
    print(searchs[searchs['cluster'] == pred[0]].sample(20))





Nao(0.1,0.8)

