import numpy as np
import cv2
import math

def pixel2degree (centroid, img):

	# modify this constant 
	#z_distance = input("Type your distance from the camera in meters: ")# in meters
	#FOV_x = input ("Enter the field of view of your camera in degrees in the x-axis: ")
	#FOV_y = input ("Enter the field of view of your camera in degrees in the y-axis: ")
	
	z_distance = 0.2
	FOV_x = 130
	FOV_y = 45

	image = cv2.imread(img)

	h, w = image.shape[0:2]
	#get the bottom right pixel
	bottom_right = image[h-1, w-1]

	parseList = [0] * len(centroid)
	# normalizing pixel coordinates
	for i in range (0, len(centroid)):
		parseList[i] = centroid[i]
	print parseList
	for i in range (0, len(centroid)):
		x_norm = (parseList[i])[i]/bottom_right[0]
		y_norm = parseList[1]/bottom_right[1]

	# tan(FOV/2) = x / distance
	radx = math.radians(FOV_x/2)
	rady = math.radians(FOV_y/2)
	x = z_distance * math.tan (radx)
	y = z_distance * math.tan (rady)

	degree = [0] * 2
	degree[0] = math.atan(x/z_distance)
	degree[1] = math.atan(y/z_distance)

	
	return degree

if __name__ = "__main__":
	centroid = [0, [[183], [197]], [[757], [474]], [[1052, 749], [646, 459]], [[786], [429]], [[719], [464]], [[718], [475]], [[667, 697], [309, 471]], [[673], [448]], [[656], [423]], [[665], [323]], [[688], [251]], [[721], [289]], [[737], [299]], [[757], [336]], [[752], [330]], [[775], [375]], [[774], [417]], [[730], [365]], [[671], [364]], [[634], [379]], [[611], [395]], [[580], [392]], [[551], [384]], [[488], [376]], [[431], [343]], [[360], [368]], [[332], [384]], [[324], [354]], [[307], [356]], [[289], [361]], [[301], [359]], [[330], [394]], [[386], [388]], [[451], [371]], [[517], [374]], [[610], [362]], [[688], [369]], [[794], [362]], [[862], [350]], [[888], [578]], [[672], [355]], [[611], [441]]]
	degree = pixel2degree(centroid,"image1.jpg")
