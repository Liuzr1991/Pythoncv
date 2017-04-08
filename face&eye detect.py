# -*- coding: UTF-8 -*-

import numpy as np
import cv2
# ģʽ����
dir_path = "D:\opencv\sources\data\haarcascades" # ����OpenCV·��
filename = "haarcascade_frontalface_default.xml" # ʶ��ģʽ�ļ�
model_path = dir_path + "/" + filename
#����ʶ��
def gface(image):
	# ���� classifier
	clf = cv2.CascadeClassifier(model_path)
	eye_cascade = cv2.CascadeClassifier(dir_path+r'/haarcascade_eye_tree_eyeglasses.xml')
	# �趨�Ҷ�
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	# ʶ���沿
	faces = clf.detectMultiScale(
		gray,
		scaleFactor=1.1,
		minNeighbors=5,
		minSize=(30, 30),
		flags=cv2.CASCADE_SCALE_IMAGE
	)
	#print("Found {0} faces!".format(len(faces)))
	# ������
	for (x, y, w, h) in faces:
		cv2.rectangle(image, (x, y), (x+w, y+h), (60, 230, 100), 2)
		roi_gray = gray[y:y+h, x:x+w]
		roi_color = image[y:y+h, x:x+w]
		eyes = eye_cascade.detectMultiScale(roi_gray)
		for (ex,ey,ew,eh) in eyes:
			cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(40,50,255),1)
	return image
cap = cv2.VideoCapture(0) # ������ͷ��ȡ����Ƶ
# ��ȡ��Ƶ���Ž��泤��
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH) + 0.5)
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT) + 0.5)
# ��������� ���� VideoWriter ����
#fourcc = cv2.VideoWriter_fourcc(*'mp4v') # Be sure to use the lower case
#out = cv2.VideoWriter('output.mp4', fourcc, 20.0, (width, height))
while(cap.isOpened()):
	#��ȡ֡����ͷ
	ret, frame = cap.read()
	if ret == True:
		#�����ǰ֡
		frame=gface(frame)
	#	out.write(frame)
		cv2.imshow('My Camera',frame)
		#���̰� Q �˳�
		if (cv2.waitKey(1) & 0xFF) == ord('q'):
			break
	else:
		break
# �ͷ���Դ
#out.release()
cap.release()
cv2.destroyAllWindows()
