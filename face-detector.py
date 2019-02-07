import numpy as np 
import cv2
faceDetect=cv2.CascadeClassifier('haarcascade_frontalface_default.xml');
cam = cv2.VideoCapture(0);
recognizer = cv2.face.LBPHFaceRecognizer_create(); #create a recognizer, LBPH is a face recognition algorithm.Local Binary Patterns Histograms 
recognizer.read("recognizer\\trainingData.yml")
id=0 #id variable
font = cv2.FONT_HERSHEY_SIMPLEX #5=font size
fontscale = 1
fontcolor = (255,255,255)
stroke = 2

			
while(True):
	ret, frame = cam.read();
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) 
	faces=faceDetect.detectMultiScale(gray,1.3,5);
	for(x,y,w,h) in faces:
		#cv2.rectangle(gray,(x,y),(x+w,y+h),(0,0,255),2)
		cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2) #2 is thickness of the text and (0,0,255) is color of the text which is red
		id, conf = recognizer.predict(gray[y:y+h,x:x+w]) #h-heights, w-width. this command predict the id,face of the user for this 1st create id variable which is in the command id=0
		if(conf<50):
			if(id==1):
				id="Munmun"
			elif(id==2):
				id="Mysha"

		else:
			id="Unknown"
		cv2.putText(frame, str(id), (x,y), font, fontscale, fontcolor, stroke,)#print the number or value of the prediction, str(id) means the text we want to print, (x,y+h) is for the text to be in the face and (x,y) is for the text on the upper of the rectangle
		
	cv2.imshow('frame', frame);
	if cv2.waitKey(10) & 0xFF==ord('q'):
		break;
cam.release()#when everything done release the camera or release the capture
cv2.destroyAllWindows() #close the camera and the windows