#Library immer zuerst
import numpy as np
import cv2

#dann code
print('hello world')

img = cv2.imread('dasBild.jpg', 0)
cv2.imshow('title', img)
cv2.waitKey(0)
cv2.destroyAllWindows()