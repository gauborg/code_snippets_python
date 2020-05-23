import os
import numpy as np
import cv2
import matplotlib.pyplot as plt
import matplotlib.image as mpimg


def mag_sobel(img, sobel_kernel=3, thresh = (190,255)):

    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    cv2.imwrite('gray_test.jpg', gray)
    
    ret,thresh1 = cv2.threshold(img,200,255,cv2.THRESH_BINARY)

    b, g, r = cv2.split(img)
    
    plt.figure(1)
    plt.imshow(thresh1)
    plt.show()
    
    plt.figure(2)
    plt.imshow(b)
    plt.show()
    
    plt.figure(3)
    plt.imshow(g)
    plt.show()
    

    # 1. Applying the Sobel (taking the derivative)
    sobelx = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize = sobel_kernel)
    sobely = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize = sobel_kernel)

    # 2. Magnitude of Sobel
    mag_sobel = np.sqrt(sobelx**2 + sobely**2)

    # 3. Scaling to 8-bit and converting to np.uint8
    scaled_sobel = np.uint8(255*mag_sobel/np.max(mag_sobel))
    plt.imshow(scaled_sobel)
    plt.show()

    # 4. Create mask of '1's where the scaled gradient magnitude is > thresh_min and < thresh_max
    sobel_mag_image = np.zeros_like(scaled_sobel)
    sobel_mag_image[(scaled_sobel > thresh[0]) & (scaled_sobel <= thresh[1])] = 1
    
    return sobel_mag_image

img = cv2.imread('my_test.jpg')

result = mag_sobel(img, sobel_kernel=5, thresh = (100,255))

'''
plt.imshow(result)
plt.show()

'''
