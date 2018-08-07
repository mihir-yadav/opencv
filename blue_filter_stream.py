import cv2
import numpy as np
#img =cv2.imread('4balls.jpg')

cap=cv2.VideoCapture(0)
fourcc = cv2.cv.CV_FOURCC(*'XVID')

while True:
	_,img=cap.read()


	hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)




	lower_red=np.array([110,50,50])
	upper_red=np.array([115,250,250])

	mask=cv2.inRange(hsv,lower_red,upper_red)
	res=cv2.bitwise_and(img,img,mask=mask)
	median=cv2.medianBlur(res,15)
	kernel=np.ones((5,5),np.uint8)
	opening=cv2.morphologyEx(res,cv2.MORPH_OPEN,kernel)
	
	cv2.imshow('img',img)
#	cv2.imshow('mask',mask)
	cv2.imshow('res',res)
#	cv2.imshow('median',median)
#	cv2.imshow('opening',opening)
	if cv2.waitKey(1) & 0xFF==ord('q'):

		break


cv2.destroyAllWindows()
cap.release()
