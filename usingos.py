import os

face_dir = input("Enter name of folder **usually name of person to be in the images**: ")

""" done automatically. """
if 'images' in os.getcwd():
	os.chdir('images')
	print(os.getcwd())
	os.mkdir(face_dir)
else:
	os.mkdir(face_dir)


# doesn't seem to be working. I have no idea why...