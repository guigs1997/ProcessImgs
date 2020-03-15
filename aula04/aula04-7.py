import cv2

imgRGB  = cv2.imread('data/lena.jpg')
copy = imgRGB.copy()

#get b-g-r components
b,g,r = cv2.split(imgRGB)

#get blue component
b2 = imgRGB[:,:,0] #todos os pixels da largura, todos da altura, cor azul

#set 0 to red compoment 
copy[:,:,2]=0 #todos os pixels da largura, todos da altura, cor vermelho

cv2.imshow('Blue'       ,b)
cv2.imshow('Green'      ,g)
cv2.imshow('Red'        ,r)
cv2.imshow('Blue2'      ,b2)
cv2.imshow('Copy'       ,copy)


cv2.waitKey()
cv2.destroyAllWindows()

