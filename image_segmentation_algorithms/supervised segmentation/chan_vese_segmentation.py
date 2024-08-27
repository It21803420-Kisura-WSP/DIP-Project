# Chan-Vese Segmentation
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from skimage.color import rgb2gray
from skimage.segmentation import chan_vese

fig, axes = plt.subplots(1, 3, figsize=(10, 10))

image = Image.open("image.png").convert("RGB")
image_array = np.array(image)
gray_image = rgb2gray(image)

# Computing the Chan VESE segmentation technique
chanvese_gray_image = chan_vese(gray_image, max_num_iter=100, extended_output=True)
ax = axes.flatten()
 
# Plotting the original image
ax[0].imshow(gray_image, cmap="gray")
ax[0].set_title("Original Image")
 
# Plotting the segmented - 100 iterations image
ax[1].imshow(chanvese_gray_image[0], cmap="gray")
title = "Chan-Vese segmentation - {} iterations".format(len(chanvese_gray_image[2]))
 
ax[1].set_title(title)
 
# Plotting the final level set
ax[2].imshow(chanvese_gray_image[1], cmap="gray")
ax[2].set_title("Final Level Set")
plt.show()