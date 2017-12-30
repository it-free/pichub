#Library immer zuerst
import numpy as np
import cv2
import os, sys

#variablen
path = '/pictures'
dirs = os.listdir( path )

#dann programmabschnitte
for file in dirs:
   print file

def load_images_from_folder(folder):
    images = []
    for filename in os.listdir(folder):
        img = cv2.imread(os.path.join(folder,filename))
        if img is not None:
            images.append(img)
    return images

#dann code
print('start')

img = cv2.imread('dasBild.jpg', 1)
cv2.imshow('title', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

print('end')