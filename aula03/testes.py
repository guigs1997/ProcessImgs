from cv2 import cv2 
import numpy as np

i=0.0
j=1.0
n = []

img = cv2.imread('data/lena.jpg')
img2 = cv2.imread("data/macaco.jpg")

while True:
    if (i<=0):
        for contador in range(11):           
            i+=0.10
            j-=0.10
            n = cv2.addWeighted(img,i,img2,j,1)
            cv2.imshow('Img',n)
            cv2.waitKey(100)
        i=1    
    elif (i>=1.0):
        for contador2 in range(10):
            j+=0.10
            i-=0.10
            n = cv2.addWeighted(img,i,img2,j,1)
            cv2.imshow('Img',n)
            cv2.waitKey(100)
        i=0
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break     
cv2.waitKey()