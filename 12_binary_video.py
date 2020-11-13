import os
import imageio
import moviepy as mpy
import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from moviepy.editor import VideoFileClip



def bin_video(img):

    # convert to HLS colorspace
    hls = cv2.cvtColor(img, cv2.COLOR_RGB2HLS)
    hls_blurred = cv2.GaussianBlur(hls,(5,5),cv2.BORDER_DEFAULT)
    # convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    gray_blurred = cv2.GaussianBlur(gray,(5,5),cv2.BORDER_DEFAULT)
    img_blurred = cv2.GaussianBlur(img,(5,5),cv2.BORDER_DEFAULT)


    ################ ------ LIGHTNESS IMAGE ------ ################
    # 2. Apply threshold to s channel
    l_channel = hls_blurred[:,:,1]
    # 3. Create empty array to store the binary output and apply threshold
    l_binary = np.zeros_like(l_channel)
    l_binary[(l_channel > 130) & (l_channel <= 255)] = 1


    ############## ------ PIXEL BINARY IMAGE ------ ###############
    # THIS FUNCTION WORKS ONLY ON GRAYSCALE IAMGES!!!
    # 1. apply threshold
    intensity_binary = np.zeros_like(gray_blurred)
    # 2. create a binary image
    intensity_binary[(gray_blurred > 150) & (gray_blurred <= 255)] = 1


    ################## ------ SOBEL OPERATOR ------ ################
    # 1. Applying the Sobel depending on x or y direction and getting the absolute value
    orient = 'x'
    if (orient == 'x'):
        abs_sobel = np.absolute(cv2.Sobel(gray_blurred, cv2.CV_64F, 1, 0, ksize = 5))
    if (orient == 'y'):
        abs_sobel = np.absolute(cv2.Sobel(gray_blurred, cv2.CV_64F, 0, 1, ksize = 5))
    # 2. Scaling to 8-bit and converting to np.uint8
    scaled_sobel = np.uint8(255*abs_sobel/np.max(abs_sobel))
    # 3. Create mask of '1's where the sobel magnitude is > thresh_min and < thresh_max
    sobel_image = np.zeros_like(scaled_sobel)
    sobel_image[(scaled_sobel >= 25) & (scaled_sobel <= 100)] = 1


    
    ############### ------ COMBINED THRESHOLD ------ ################
    # creating an empty binary image
    combined_l_or_intensity = np.zeros_like(gray_blurred)
    combined_l_or_intensity[((intensity_binary == 1) | ((l_binary == 1) | (sobel_image == 1)))] = 1
    # apply region of interest mask
    height, width = combined_l_or_intensity.shape
    mask = np.zeros_like(combined_l_or_intensity)

    
    # define the region as 
    region = np.array([[0, height-1], [int(width/2), int(height/2)], [width-1, height-1]], dtype=np.int32)
    cv2.fillPoly(mask, [region], 1)

    masked_img = cv2.bitwise_and(combined_l_or_intensity, mask)

    # canny edge detection
    canny_img = cv2.Canny(img_blurred, 50, 150)
    canny_img2 = np.zeros_like(img_blurred)
    canny_img2[:,:,0] = canny_img
    canny_img2[:,:,1] = canny_img
    canny_img2[:,:,2] = canny_img

    # copy of final image
    combined_canny_and_threshold = np.zeros_like(canny_img)
    combined_canny_and_threshold[(combined_l_or_intensity == 1) | (canny_img == 1)] = 1

    # resulting final image
    result = np.zeros_like(img_blurred)
    result[:,:,0] = 255*combined_canny_and_threshold
    result[:,:,1] = 255*combined_canny_and_threshold
    result[:,:,2] = 255*combined_canny_and_threshold

    return result


# video pipeline
video_binary_output = 'video-output-combined.mp4'
clip1 = VideoFileClip("video.mp4")

white_clip = clip1.fl_image(bin_video) # NOTE: this function expects color images!!
white_clip.write_videofile(video_binary_output, audio=False)
