import cv2


cap=cv2.VideoCapture(0)
fourcc = cv2.cv.CV_FOURCC(*'XVID')
out=cv2.VideoWriter('output.avi',fourcc,20.0,(640,480))

while True:
	_,frame=cap.read()

	laplacian=cv2.Laplacian(frame,cv2.CV_64F)
	sobelx=cv2.Sobel(frame,cv2.CV_64F,1,0,ksize=5)
	sobely=cv2.Sobel(frame,cv2.CV_64F,0,1,ksize=5)
	edges=cv2.Canny(frame,200,200)

	cv2.imshow('frame',frame)
	cv2.imshow('laplacian',laplacian)
	cv2.imshow('sobelx',sobelx)
	
	cv2.imshow('edges' ,edges)		
	if cv2.waitKey(1) & 0xFF==ord('q'):
		break;

cap.release()
out.release()
cv2.destroyAllWindows()
