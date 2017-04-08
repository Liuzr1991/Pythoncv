# -*- coding: utf-8 -*- 

import cv2
import numpy as np
from matplotlib import pyplot as plt

def nothing(x):
	pass

img = cv2.imread('messi5.jpg',0)
cv2.namedWindow('image')
cv2.createTrackbar('L','image',0,255,nothing)
cv2.createTrackbar('H','image',0,255,nothing)

while(1):
	l=cv2.getTrackbarPos('L','image')
	h=cv2.getTrackbarPos('H','image')

	edges = cv2.Canny(img,l,h)
	cv2.imshow('image',edges)
	
	k=cv2.waitKey(1)&0xFF
	if k==27:
		break
cv2.destroyAllWindows()