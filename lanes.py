import cv2
from matplotlib.patches import Polygon
import numpy as np
import matplotlib.pyplot as plt
def canny(image):
    gray = cv2.cvtColor(lane_image,cv2.COLOR_RGB2GRAY)
    blur = cv2.GaussianBlur(gray,(5,5),0)
    canny = cv2.Canny(blur,50,150)
    return canny

def region(image):
    height=image.shape[0]
    Polygon=np.array([[(200,height),(1100,height),(550,250)]])
    mask=np.zeros_like(image)
    cv2.fillPoly(mask,Polygon,255)
    return mask

image=cv2.imread('test_image.jpg')
lane_image=np.copy(image)
canny=canny(lane_image)
cv2.imshow('result',region(canny))
cv2.waitKey(0)
