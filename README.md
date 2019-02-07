# Face-detection-and-identification-in-real-time-by-using-user-input-id

Detect and Identify human faces in real time by asking user input id (implementing opencv with python):

Face Detection: Face detection means to detect human faces from an input image, video or detect human faces in real time.

Face Identification: Face identification is identify human faces in a video or image including the person's name. A human is recognized by his/her name.

Opencv has some built-in features. To do this project here used: numpy==1.15.4, opencv==3.4.3.18, pillow=5.3.0, virualenv==16.1.0, python=3.6.7

✔ Step 1: Copy haarcascade_frontalface_default.xml from cv2

✔ Step 2: Than start with a new file which is named as datasetcreator.py file: Here need to do is whenever the program captures a face write that in a folder before capturing the face need to tell whose face it is. 
For that need a identifier. So, id=input('Enter user id : ') This ask user to input id and after putting an id number, the id number saves with a face because later it will identify whose face it is.
Create a directory in the project folder where datasetcreator.py file is and than named the directory dataSet. In this directory the persons face picture will be saved after running datasetcreator.py file
Now running datasetcreator.py file and it ask the user Enter user id :  So, as user I entered user id 1. Now, the webcam will open and it will take my pictures and will save it in the dataSet directory.

✔ Step 3: Create another new file named as face-trainner.py file: Here the pictures that have been taken in the dataSet directory will be trained. So that it could identify the person.
To train the opencv recognizer, LBPH is used. There are many facial recognizer. But here used LBPH face recognizer which is Local Binary Patterns Histogram. OpenCV provides three methods of face recognition: Eigenfaces, Fisherfaces, Local Binary Patterns Histograms (LBPH).
LBPH(Local Binary Patterns Histograms) : In LBPH each images is analyzed independently, while the eigenfaces method looks at the dataset as a whole. The LBPH method is somewhat simpler, in the sense that we characterize each image in the dataset locally and when a new unknown image is provided, we perform the same analysis on it and compare the result to each of the images in the dataset. The way which we analyze the images is by characterizing the local patterns in each location in the image. Using LBPH method for face recognition, it will probably work better in different environments and light conditions. However, it will depend on our training and testing data sets. 
Create another directory in the project folder where datasetcreator.py and face-trainner.py file is and named the directory recognizer.
After running face-trainner.py file it will show the id number of the person that has been declared in datasetcreator.py file. As I have declared my id 1, so after ruunning face-trainner.py file in the result it will show 1 and automatically a new file has been saved in the recognizer directory wich is named as trainingData.yml

✔ Step 4: Now, Create another new file named as face-detector.py file: Here the LBPH recognizer need to be create again and have to load the trainning data.
It will detect and identify the person because in the previous file the id has been declare with the images and than the images has been trained with id. So, now with id the person will be recognized. With id the person name has been declared in this file.
So, after running face-detector.py file the webcam will open and will see a red rectangle will detect a face, also the name of the person will be seen in the webcam.
It can also detect a unknown face whose id has not been declared and whose face has not been captured or trained.
