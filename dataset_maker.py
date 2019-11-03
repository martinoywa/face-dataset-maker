import os

import cv2
from random import randint

if 'images' in os.listdir():
	pass
else:
	os.mkdir("images")	# main images directory

def make_directory():
	# Ensures that correct dataset is made.
		#Returns new directory

	person_directory = input("name directory(name of a person): ")
	
	os.chdir("images") 
	if person_directory in os.listdir():
		pass
	else:
		os.mkdir(person_directory)

	# change back to the parent directory
	os.chdir(os.pardir)

	directory_name = "images/"+person_directory

	return directory_name

def generate_dataset(directory_name):
	""" Generated a dataset containing images of person.
	    Once green box displays, images is saved.
	"""

	# face cascade
	cascade = cv2.CascadeClassifier('haarcascade/haarcascade_frontalface_alt2.xml')
	cap = cv2.VideoCapture(0)	# initialize realtime video capture

	while True:
		ret, frame = cap.read()	# intialize frame
		gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)	# necessary for detection
		face = cascade.detectMultiScale(gray) # detected face

		for (x, y, w, h) in face:
			# get region of interest
			roi = frame[y:y+h, x:x+w]
			# saving image gotten from the roi
			image = directory_name+"/image"+str(randint(1, 10000000))+".png"
			cv2.imwrite(image, roi)

			# generating the bounding box.
			# This is necessary as it's an indicator that an image has been
			# saved.
			color = (0, 255, 0)	# setting the color to green. (BGR)
			stroke = 2	# box thickness
			end_cord_x = x + w
			end_cord_y = y + h
			cv2.rectangle(frame, (x, y), (end_cord_x, end_cord_y), color, stroke)

		cv2.imshow('realtime frame', frame)	# show the video capture
		if cv2.waitKey(20) & 0xFF == ord('q'):  # press 'Q' to quit
			break

	# clear memory
	cap.release()
	cv2.destroyAllWindows()


if __name__ == '__main__':
	directory_name =  make_directory()
	generate_dataset(directory_name)