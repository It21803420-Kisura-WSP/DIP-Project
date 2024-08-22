# Segmentation by Thresholding  Using skimage.filters module
from skimage import filters
from skimage.color import rgb2gray
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np

image = Image.open("image.png").convert("RGB")
image_array = np.array(image)
gray_image = rgb2gray(image)

plt.figure(figsize=(15,15))
threshold = filters.threshold_otsu(gray_image)

binarized_image = (gray_image > threshold)*1
plt.subplot(2,2,1)
plt.title("Threshold: >"+str(threshold))
plt.imshow(binarized_image, cmap = "gray")

threshold = filters.threshold_niblack(gray_image)

# Niblack Thresholding
binarized_image = (gray_image > threshold)*1
plt.subplot(2,2,2)
plt.title("Niblack Thresholding")
plt.imshow(binarized_image, cmap = "gray")

# Sauvola Thresholding
threshold = filters.threshold_sauvola(gray_image)
plt.subplot(2,2,3)
plt.title("Sauvola Thresholding")
plt.imshow(threshold, cmap = "gray")

# Sauvola Thresholding - Converting to 0's and 1's
binarized_image = (gray_image > threshold)*1
plt.subplot(2,2,4)
plt.title("Sauvola Thresholding - Converting to 0's and 1's")
plt.imshow(binarized_image, cmap = "gray")