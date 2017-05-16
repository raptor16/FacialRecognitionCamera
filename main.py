import cv2
import numpy as np 

from vid2photos import vid2photos
from face_detection import face_detect

#from pixel2degree import pixel2degree

if __name__ == "__main__":
	frameCount = vid2photos()
	#initialing list for the centroids
	centroidPerFrame = [0] * (frameCount-1)

	for i in range (1, frameCount-1):
		centroidPerFrame[i] = face_detect("image" + str(i) + ".jpg")
	newlist = centroidPerFrame.remove(0)
	print newlist
	cleanList = [x for x in centroidPerFrame if x != [[], []]]
	print cleanList

	#degree = pixel2degree (cleanList, "image1.jpg")
	#print degree

	# use the valueo of centroidPerFrame and parse it (need some parser fuction)
	# then use the parsed value rearrange it prettily and convert it it to some 
		# angle given the distance (CONST) (need a function for this too)
	# then 