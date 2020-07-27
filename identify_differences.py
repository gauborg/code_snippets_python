import os
import cv2

image1 = cv2.imread("./test_image.jpg")
image2 = cv2.imread("./test_image2.jpg")

diff = cv2.subtract(image1, image2)
cv2.imshow('diff', diff)
cv2.waitKey(0)

# color the mask red
Conv_hsv_Gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(Conv_hsv_Gray, 0, 255,cv2.THRESH_BINARY_INV |cv2.THRESH_OTSU)
diff[mask != 255] = [0, 0, 255]

# add the red mask to the images to make the differences obvious
image1[mask != 255] = [0, 0, 255]
image2[mask != 255] = [0, 0, 255]

# store images
cv2.imwrite('diffOverImage1.png', image1)
cv2.imwrite('diffOverImage2.png', image1)
cv2.imwrite('diff.png', diff)


