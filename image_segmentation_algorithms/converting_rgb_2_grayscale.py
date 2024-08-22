# Converting RGB to GrayScale
from PIL import Image
import numpy as np
from skimage.color import rgb2gray
import matplotlib.pyplot as plt

# image had 4 channels instead of 3 so we had to convert it to 3 channels basically removing alpha channel
image = Image.open("image.png").convert("RGB") 
image_array = np.array(image)

# plotting the image
plt.figure(figsize=(20,20))
plt.subplot(1, 2, 1)
plt.imshow(image)

# gray image
gray_image = rgb2gray(image)
plt.subplot(1, 2, 2)
plt.imshow(gray_image, cmap="gray")