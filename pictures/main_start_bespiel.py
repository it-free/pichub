#Library immer zuerst
import numpy as np
import cv2
import os

#dann code
print('start')

img = cv2.imread('dasBild.jpg', 1)
cv2.imshow('title', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

print('end')