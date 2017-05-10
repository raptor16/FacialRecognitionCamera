import numpy as np

def pixel2degree ():

	# modify this constant 
	distance = input("Type your distance from the camera in meters: ")# in meters
	FOV = input ("Enter the field of view of your camera")

	# how to find the bottom right corner pixel values???
	# becuase I want to normalize the centroid location to the overall pixel couunt in x and y
	# and then find the percentage given the knwon field of view (FOV) of the camera
	return degree