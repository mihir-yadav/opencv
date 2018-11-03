# opencv
using the opencv framework in python to do some interesting stuff


The blue_filter_stream.py and red_filter.py basically use the inRange funcion of numpy and the bitwise_and function of cv2. This idea can be used to filter out any given color using their hsv values. Note: pressing 'q' finishes the live streaming by closing the popup window.

Edge detection is mainly implemented using the Laplacian and Sobel functions.

superimpose.py fulfills one of the most crucial purpose faced by many companies in their advertisements i.e. the implacemnt of company logos on the main advertisement poster in such a way that it seems logo has been placed over the image and does not cover the region below it. The main function used was Threshold followed by manipualtion using bitwise_and,add and bitwise_not .
