'''PIL –Python Imaging Library adds image processing capabilities to Python interpreter used in the code to:
•	read an image and store it as a variable
•	obtain the size of image in pixels
•	obtain value of RGB (Red, Green, Blue) of each pixel
•	alter value of RGB of each pixel
•	save output image

numpy –Python library used for working with arrays used in the code to:
•	create an array of pixel from an image
•	obtaining single channel pixel values from 3D array containing information about height, width and value of pixels
•	obtaining average pixel intensity value for each channel (sum of pixel intensities/total number of pixels)
•	stacking input and obtained output images
OpenCV (cv2) - Library of programming functions mainly for real-time computer vision used in the code to: 
•	read image 
•	split a 3-colour channel image into single channels 
•	resize image
•	normalize image
•	merge single channels into a 3-colour channel image
•	convert a BGR (Blue, Green, Red) colour space to Lab (Light, Red/Green value, Blue/Yellow value)
•	create a CLAHE of the image and apply it
•	display output image

Contrast Limited Adaptive Histogram Equalization (CLAHE) - improves the contrast of the image and visibility, thus aiding in improved image clarity

Imports the required libraries'''

import cv2 as cv
from PIL import Image
import numpy as np

#Reads image and create array of pixel values 
image = Image.open("inputpic.jpeg")
image_array = np.array(image)

#Stores Index values for each channel 
R = np.mean(image_array[:, :, 2])
G = np.mean(image_array[:, :, 1])
B = np.mean(image_array[:, :, 0])
#Target colour balance values 
R_ = G_ = B_ = 150


#Creating colour-corrected image by traversing the 2-D array of pixels, changing the value of each pixel using the below given formula and assembling back all of the pixels.

for x in range(image.size[0]):
    for y in range(image.size[1]):
        b, g, r = image.getpixel((x, y))
        r_ = int(r + (R_ - R))
        g_ = int(g + (G_ - G))
        b_ = int(b + (B_ - B))
        image.putpixel((x, y), (b_, g_, r_))

# Converting colour corrected image to an array pixel values
corrected_image_array = np.array(image)


step2_input = corrected_image_array
step2_input = cv.resize(step2_input, (500, 500))

#Splits the image into primary colour channels
rc, gc, bc = cv.split(step2_input)

#normalization of each of the colour channels- Blue, Green and Red to change the intensity of the pixels, improving contrast
stepr = cv.normalize(rc, rc.copy(), 0, 255, cv.NORM_MINMAX)
stepg = cv.normalize(gc, gc.copy(), 0, 255, cv.NORM_MINMAX)
stepb = cv.normalize(bc, bc.copy(), 0, 255, cv.NORM_MINMAX)

#The normalized channel values are merged together again to form a normalized image 
merge1 = cv.merge((stepr, stepg, stepb))

 #Converting the image that is in BGR primary colours to Lab colorspace, where L is the lightness value in the image

lab = cv.cvtColor(merge1, cv.COLOR_BGR2LAB)
#Splits the Lab space image into single channels
l_channel, a, b = cv.split(lab)

#CLAHE is being applied on the Lightness channel of the image, after which all channels are merged together to improve the contrast and clarity of image


clahe = cv.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
cl = clahe.apply(l_channel)
#The channels are merged after CLAHE is applied to lightness channel
limg = cv.merge((cl, a, b))

#Lab colorspace image is converted back to RGB image
enhanced_img = cv.cvtColor(limg, cv.COLOR_LAB2RGB)

#Output image
cv.imshow('Result', enhanced_img)
cv.waitKey(0)
