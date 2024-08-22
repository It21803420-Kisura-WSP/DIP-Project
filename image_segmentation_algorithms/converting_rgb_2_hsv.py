# Converting RGB to HSV
from PIL import Image
import numpy as np
from skimage.color import rgb2hsv
import matplotlib.pyplot as plt

# load image
image = Image.open("image.png").convert("RGB") 
image_array = np.array(image)

# plotting the image
plt.figure(figsize=(20,20))
plt.subplot(1, 2, 1)
image_colorbar = plt.imshow(image)
plt.colorbar(image_colorbar, fraction=0.046, pad=0.04)

# hsv image
hsv_image = rgb2hsv(image_array)
plt.subplot(1, 2, 2)
hsv_colorbar = plt.imshow(hsv_image)
plt.colorbar(hsv_colorbar, fraction=0.046, pad=0.04)