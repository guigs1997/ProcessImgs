import cv2

img = cv2.imread('data/lena.jpg', cv2.IMREAD_GRAYSCALE) #abrindo em grayscale, passo um filtro

cv2.imshow('Img',img)

cv2.imwrite('newfile.jpg', img) #gravo uma nova img 

print('Gray Image Save')

cv2.waitKey()


cv2.destroyAllWindows()

