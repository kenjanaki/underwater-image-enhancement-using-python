'''Mean Squared Error:  It assesses the deviance of the observed values to the predicted values.
M.S.E= Σ(yi-y'i)^2/n'''

import numpy as np
import cv2 as cv
image1 = cv.imread("input.jpeg")
image1 = cv.resize(image1,(500,500))
image2 = cv.imread("output.jpeg")
image2 = cv.resize(image2,(500,500))

def mse(imageA, imageB):
    err = np.sum((imageA.astype("float") - imageB.astype("float"))**2)
    err /= float(imageA.shape[0] * imageA.shape[1])
    return err

mean = mse(image1, image2)
print(mean)
