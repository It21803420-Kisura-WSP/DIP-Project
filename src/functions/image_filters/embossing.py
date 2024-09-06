import cv2
import numpy as np

def embossing(image_path):
    image = cv2.imread(image_path)
    embossing_kernel = np.array([[ -2, -1, 0],
                   [ -1,  1, 1],
                   [  0,  1, 2]])
    embossed_image = cv2.filter2D(image, -1, embossing_kernel)
    cv2.imwrite("embossed_image.png", embossed_image)

"""
Tests
- Run this in jupyter notebook (Uncomment This when your running it)

embossing("image.png")
"""