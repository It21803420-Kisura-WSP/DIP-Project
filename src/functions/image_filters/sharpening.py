import cv2
import numpy as np

def image_sharpening(image_path):
    image = cv2.imread(image_path)
    sharpening_kernal = np.array([[0, -1, 0],
                   [-1, 5, -1],
                   [0, -1, 0]])
    sharpened_image = cv2.filter2D(image, -1, sharpening_kernal)
    cv2.imwrite("sharpened_image.png", sharpened_image)

"""
Tests
- Run this in jupyter notebook (Uncomment This when your running it)

image_sharpening("image.png")
"""