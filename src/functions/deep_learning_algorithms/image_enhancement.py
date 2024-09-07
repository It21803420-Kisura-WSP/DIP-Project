# Image Enhancement Algorithms

# Reducing Noise Imports
import cv2 as cv
from matplotlib import pyplot as plt

def reducing_noise(image_path : str):
    img = cv.imread(image_path)
    dst = cv.fastNlMeansDenoising(img,None,3,7,21)
    plt.subplot(121),plt.imshow(img)
    plt.subplot(122),plt.imshow(dst)
    plt.show()

def reducing_noise_colored(image_path : str):
    img = cv.imread(image_path)
    dst = cv.fastNlMeansDenoisingColored(img,None,10,10,7,21)
    plt.subplot(121),plt.imshow(img)
    plt.subplot(122),plt.imshow(dst)
    plt.show()

"""
TEST CASES
reducing_noise("noisy.jpg") # GrayScale
reducing_noise_colored("image.png") # Colored
"""

def sharpening_image():
    pass

def adjusting_contrast():
    pass

def histogram_equalization():
    pass

def CLAHE():
    pass

# use deep learning models for super-resolution