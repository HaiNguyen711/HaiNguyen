import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn import metrics
import warnings
warnings.filterwarnings("ignore")
from Khanang.Nghe import Nghe
from Khanang.Noi import Noi
from Khanang.Nao import Nao
import wikipedia
import webbrowser as wb
import datetime 

def time():
    Time=datetime.datetime.now().strftime("%I:%M:%p") 
    Noi("Bây giờ là")
    Noi(Time)

def chao():
        #Chao hoi
        hour=datetime.datetime.now().hour
        if hour >= 6 and hour<12:
            Noi("Chào buổi sáng!")
        elif hour>=12 and hour<18:
            Noi("Chào buổi trưa!")
        elif hour>=18 and hour<24:
            Noi("Buổi tối tốt lành")
        Noi("Tôi có thể giúp gì cho bạn") 

def Search_GG():
    Noi("Bạn cần tìm kiếm gì ?")
    search=Nghe()
    url = f"https://google.com/search?q={search}"
    wb.get().open(url)
    wikipedia.set_lang("vi")
    wiki = wikipedia.summary(search, sentences= 1)
    Noi(wiki)

def Search_YT():
    Noi("Bạn cần tìm kiếm gì ?")
    search=Nghe()    
    url = f"https://youtube.com/search?q={search}"
    wb.get().open(url)

if __name__  =="__main__":
    while True:
        Khoi_dong=Nghe().lower()
        if Khoi_dong.count('chào'or 'hey') > 0:
            Noi('Hari đây! Bạn cần gì')
            Lenh = Nghe().lower()
            Noi('Đợi tôi một chút')
            if "mấy giờ" in Lenh:
                print(Lenh)
                time()
            elif "google" in Lenh:
                print(Lenh)
                Search_GG()
            elif "youtube" in Lenh:
                print(Lenh)
                Search_YT()
            elif "mua" in Lenh:
                print(Lenh)
                Noi('Bạn muốn mua gì')
                sp = Nghe()
                Noi('Hãy nhập thông số')
                print(Nao(input('gia'),input('danh gia'),input('vi tri'),input('so sp da ban'),sp))
            elif "bye" or "tạm biệt" in Lenh:
                print(Lenh)
                Noi("Tạm biệt")
                quit()


