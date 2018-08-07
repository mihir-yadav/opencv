import cv2
import numpy as np
img =cv2.imread('4balls.jpg')

hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)




lower_red=np.array([140,0,0])
upper_red=np.array([180,250,250])

mask=cv2.inRange(hsv,lower_red,upper_red)
res=cv2.bitwise_and(img,img,mask=mask)
median =cv2.medianBlur(res,15)

kernel=np.ones((5,5),np.uint8)
opening =cv2.morphologyEx(res,cv2.MORPH_OPEN,kernel)

cv2.imshow('img',img)
cv2.imshow('mask',mask)
cv2.imshow('res',res)
cv2.imshow('median',median)
cv2.imshow('opening',opening)
cv2.waitKey(0)
cv2.destroyAllWindows()
