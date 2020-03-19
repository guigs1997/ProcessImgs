from cv2 import cv2 
import numpy as np

img = cv2.imread('data/lena.jpg')
ok = True

while ok:
    cv2.imshow('Img',img)
        
    if cv2.waitKey(1)  == 113:
        ok = False
    if cv2.waitKey(1) & 0xFF == ord('Q'):
        ok = False
#cv2.waitKey()

cv2.destroyAllWindows()