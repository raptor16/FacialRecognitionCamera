import cv2
import numpy as np

def vid2photo(vidFilePath):
	print "Hello world from vid2photo"
	counter = 0

	video = cv2.VideoCapture (vidFilePath)

	while (video.isOpened()):
		counter += 1  

		ret, frame = video.read()

		cv2.imwrite ("frame%s" (counter))

		if cv2.waitKey(1) & 0xFF == ord('q'):
        	break

 	video.release()
 	cv2.destroyAllWindows()

 	return counter

if __name__ == "__main__":
	frameCount = vid2photo ("someSampleVideo.mpg")
	
