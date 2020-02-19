import numpy as np
import cv2

imdad = cv2.imread('imdad_pic.jpg', cv2.IMREAD_GRAYSCALE)
height = imdad.shape[0]
width = imdad.shape[1]

max_intensity = int(input("Enter the max intensity of the image: "))
#max_intensity = 255
for i in np.arange(height):
    for j in np.arange(width):
        a = imdad.item(i,j)
        b = max_intensity - a
        imdad.itemset((i,j), b)
cv2.imwrite("inverted_Image.jpg", imdad)

cv2.imshow("image",imdad)
cv2.waitKey(0)
cv2.destroyAllWindows()
