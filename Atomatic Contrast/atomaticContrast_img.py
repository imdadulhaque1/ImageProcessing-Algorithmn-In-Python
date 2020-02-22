import numpy as np
import cv2
im = cv2.imread('imdad_pic.jpg', cv2.IMREAD_GRAYSCALE)

height = im.shape[0]
width = im.shape[1]

max = int(input("Enter the maximum: "))     #max = 0
min = int(input("Enter the minimum: "))     #min = 255

for i in np.arange(height):
    for j in np.arange(width):
        a = im.item(i,j)
        if a > max:
            max = a
        elif a < min:
            min = a
for i in np.arange(height):
    for j in np.arange(width):
        a = im.item(i,j)
        b = float(a - min) / (max - min) * 255
        im.itemset((i,j),b)
cv2.imwrite("auto_contrast.jpg", im)

cv2.imshow("image",im)
cv2.waitKey(0)
cv2.destroyAllwindows()