import cv2 
import numpy as np
def face_detect (imFilePath): # add counter in argument for multiple image files (i.e. in a video)
	# face dete
	face_cascade = cv2.CascadeClassifier ('haarcascade_frontalface_default.xml')
	eye_cascade = cv2.CascadeClassifier ('haarcascade_eye.xml')


	img = cv2.imread (imFilePath)
	gray = cv2.cvtColor (img, cv2.COLOR_BGR2GRAY)

	#finding faces in the image
	faces = face_cascade.detectMultiScale (gray, 1.2, 5)

	# faces is a tuple and the ouput are of the form (x, y, w, h) 
	# the x,y coordinates of the upper left hand corner and
	#  the w, h which is the width adn height of the face respectively

	# initializing the lists
	centroid_x = [0] * len(faces) # where len(faces) is the number of faces detected
	centroid_y = [0] * len(faces)

	index = 0
	for (x,y,w,h) in faces:
		# drawing the rectangles on the faces
	    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
	    roi_gray = gray[y:y+h, x:x+w]
	    roi_color = img[y:y+h, x:x+w]

	    centroid_x[index] = x+ (w/2)
	    centroid_y[index] = y+ (h/2)

	    cv2.imwrite("image"+str(index)+".jpg", img)

	    index +=1
	#cv2.imshow('img',img)
	#cv2.waitKey(0)
	cv2.destroyAllWindows()

	centroid = [centroid_x, centroid_y]
	return centroid
	# parse the result of this as such list of lists
	# [ [list of all the x-centroids] , [list of all the y-centroids]]

