import cv2
import numpy as np
def vid2photos():
	counter = 0

	cap = cv2.VideoCapture(0)
	cap.set(cv2.cv.CV_CAP_PROP_FPS, 1)

	while (cap.isOpened()):
		ret, frame = cap.read()
		cv2.imwrite("image"+str(counter)+".jpg", frame)
		gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

		cv2.imshow('frame', gray)
		counter+=1
		if cv2.waitKey(1) & 0xFF == ord('q'):
			break

	cap.release()
	cv2.destroyAllWindows()

	return counter

	
