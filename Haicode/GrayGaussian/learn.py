from matplotlib import pyplot as mp
import cv2
import numpy as np
from PIL import Image


baseImage = r'C:\Users\chiha\Desktop\2021\Haicode\GrayGaussian\Screenshot 2021-11-03 151655.png' ## de hinh va file code chung 1 folder roi dan path vao day

img = cv2.imread(baseImage, cv2.IMREAD_COLOR)  

imgPIL = Image.open(baseImage) ##doc hinh 

convertImage = Image.new(imgPIL.mode, imgPIL.size)

widthImage = convertImage.size[0]
heightImage = convertImage.size[1]

#get gray index for each pixel$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
grayArray = []
grayindexArray = []

for x in range(widthImage):
    for y in range(heightImage):
        R, G, B, L = imgPIL.getpixel((x, y)) #get thong so R G B theo toa do pixel
        grayIndex = np.uint8((R + G + B) / 3) #lay muc xam cua tung pixel
        grayindexArray.append(grayIndex) #append gray index to array
        grayArray.append([x, y, grayIndex]) ## append gray index theo toa do

#gray index caculation$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$44$$$$$$$$$$$$$$$$$$$$$$$$$4
def Average(lst): ## ham tinh trung binh
    return sum(lst) / len(lst)

T = 100 #T ban dau

obj = []
bgd = []

for y in range(5): ### lap 50 lan
    for x in grayindexArray:
        bgd.append(x) if x < T else obj.append(x) ## moi lan lap la phan loai theo T
    T = (Average(obj) + Average(bgd)) / 2 ### update T (ky thuat 1)

#gray to binary image$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$4
for x in range(len(grayArray)):
    if (grayArray[x][2] < T ):  ## phan loai theo T cuoi cung 
        convertImage.putpixel((grayArray[x][0],grayArray[x][1]), (0, 0, 0, 1)) ## to mau den cho background
    else: 
        convertImage.putpixel((grayArray[x][0],grayArray[x][1]), (255, 255, 255, 1))  ##to mau trang cho object


###### uoc luong gia tri trung binh obj$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

def Variance(lst, mu): ## tinh phuong sai
    sum = 0 
    for x in lst:
        sum = sum + np.power((x - mu), 2)
    return sum/len(lst)

def gaussian(x, mu, sig): #tinh gia tri ham phan phoi chuan
    return (1./(np.sqrt(2.*np.pi)*sig))*np.exp(-np.power((x - mu)/sig, 2.)/2)

def epsilon(Z, siq, n):
    return Z * siq / np.sqrt(n)

sigObj = np.sqrt(Variance(obj, Average(obj))) ##do lech chuan object
sigBgd = np.sqrt(Variance(bgd, Average(bgd))) ## do lech chuan background

Z =  1.96 #reliability = 95%

eslObj = epsilon(Z, sigObj, len(obj))
xObj = (Average(obj) - eslObj ,Average(obj) + eslObj)

eslBgd = epsilon(Z, sigBgd, len(bgd))
xBgd = (Average(bgd) - eslBgd ,Average(bgd) + eslBgd)


x_values = np.linspace(0, 255, 511) ## do chia 
mp.plot(x_values, gaussian(x_values, Average(obj), sigObj), label="Object") ## ve do thi guass cua object
mp.plot(x_values, gaussian(x_values, Average(bgd), sigBgd), label="Background") ## ve do thi guass cua background


#60%$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$4
cpeMushroom1 = []
for x in x_values: #tinh sai so cho tung cap gia tri
    if (x < T):
        cpeMushroom1.append(abs(1.5*gaussian(x, Average(obj), sigObj) - gaussian(x, Average(bgd), sigBgd)))     
closetArray = np.array(cpeMushroom1)
x_closet = closetArray.argmin() / 2 #chon sai so nho nhat
mp.plot([x_closet, x_closet], [gaussian(x_closet, Average(obj), sigObj), gaussian(x_closet, Average(bgd), sigBgd)], 'go-') #ve


#show T
print(f"Muc xam theo Ky thuat 1: {T}")
print(f"Khoang uoc luong gia tri muc xam trung binh vung Object: {xObj}")
print(f"Khoang uoc luong gia tri muc xam trung binh vung Background: {xBgd}")
print(f"Muc xam theo Bayes: {x_closet}")

#show image
resultImage = np.array(convertImage)
cv2.imshow('hahaha', resultImage)
cv2.waitKey(0)
cv2.destroyAllWindows()
mp.show()   
