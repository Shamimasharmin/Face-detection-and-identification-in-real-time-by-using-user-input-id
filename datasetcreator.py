import numpy as np 
import cv2
faceDetect=cv2.CascadeClassifier('haarcascade_frontalface_default.xml');
cam = cv2.VideoCapture(0);
id=input('Enter user id : ')
sampleNum=0;
while(True):
	ret, frame = cam.read();
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	faces=faceDetect.detectMultiScale(gray,1.3,5);
	for(x,y,w,h) in faces:
		sampleNum=sampleNum+1;
		#cv2.imwrite("dataSet/User."+str(id)+"."+str(sampleNum)+".jpg",gray[y:y+h,x:x+w])
		cv2.imwrite("dataSet/User1."+str(id)+"."+str(sampleNum)+".jpg",frame[y:y+h,x:x+w])
		#cv2.rectangle(gray,(x,y),(x+w,y+h),(0,0,255),2)
		cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)
		cv2.waitKey(1);
	cv2.imshow("frame",frame);
	#if(sampleNum>20):
	#	break
	if cv2.waitKey(20) & 0xFF == ord('q'):
	    break; 
cam.release()
cv2.destroyAllWindows()