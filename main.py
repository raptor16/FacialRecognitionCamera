import cv2
import numpy as np 

if __name__ == "__main__":
	frameCount = vid2photo("someSampleVideo.mp4")

	#initialing list
	centroidPerFrame = [0] * frameCount

	for i in range (0, frameCount):

		centroidPerFrame[i] = face_detect("frame"+str(i))

	# use the valueo of centroidPerFrame and parse it (need some parser fuction)
	# then use the parsed value rearrange it prettily and feed it to the arduino (need funciton)
	
