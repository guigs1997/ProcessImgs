import cv2

#cap = cv2.VideoCapture(0)

while True :
    #ret, frame = cap.read()

    #cv2.imshow('Camera', frame)
    
    img = cv2.imread('data/lena.jpg')
    cv2.imshow('Img',img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    else cv2.waitKey(1) & 0xFF == ord('Q'):
            break

#cap.release()
cv2.destroyAllWindows()


