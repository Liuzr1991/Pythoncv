# -*- coding: utf-8 -*- 

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('aero3.jpg',0)
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
cl1 = clahe.apply(img)
plt.imshow(cl1,'gray')
plt.show()