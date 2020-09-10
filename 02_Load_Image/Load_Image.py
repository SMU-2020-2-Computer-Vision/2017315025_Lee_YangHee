import cv2
import os
# Get the path to the current file
cwd = os.path.dirname(os.path.abspath(__file__))

#Change the working directory
os.chdir(cwd)

# Load an image
img = cv2.imread('Blender_Suzanne1.jpg')

#Display the image in a window
cv2.imshow('image', img)

#Wait for a key to be pressed
cv2.waitkey(0)

#Destroy all windows
cv2.destroyAllWindows()
