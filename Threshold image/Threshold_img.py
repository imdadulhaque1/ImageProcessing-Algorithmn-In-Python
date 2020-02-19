import numpy as np
import cv2

im = cv2.imread('imdad_pic.jpg', cv2.IMREAD_GRAYSCALE)
height = im.shape[0]
width = im.shape[1]

threshold = int(input("Enter the threshold of the image: "))
#threshold = 150
for i in np.arange(height):
    for j in np.arange(width):
        a= im.item(i,j)
        if a>threshold:
            b=255
        else:
            b=0
        im.itemset((i,j), b)

cv2.imwrite("threshold_image.jpg", im)

cv2.imshow("image",im)
cv2.waitKey(0)
cv2.destroyAllWindows()
