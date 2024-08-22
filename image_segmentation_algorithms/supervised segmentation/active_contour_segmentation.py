# Active Contour Segmentation
import numpy as np
import matplotlib.pyplot as plt
from skimage.color import rgb2gray
from skimage.filters import gaussian
from skimage.segmentation import active_contour
from PIL import Image

image = Image.open("image.png").convert("RGB")
image_array = np.array(image)
gray_image = rgb2gray(image)

# apply gaussian filter
gray_image_noiseless = gaussian(gray_image, 1)

# Localising the circle's center at 220, 110
x1 = 220 + 100*np.cos(np.linspace(0, 2*np.pi, 500))
x2 = 100 + 100*np.sin(np.linspace(0, 2*np.pi, 500))

# Generating a circle based on x1, x2
snake = np.array([x1, x2]).T

# Computing the Active Contour for the given image
image_snake = active_contour(gray_image_noiseless, snake)

fig = plt.figure(figsize=(10, 10))

ax = fig.add_subplot(111)
ax.imshow(gray_image_noiseless)

# Plotting the face boundary marker
ax.plot(image_snake[:, 0], image_snake[:, 1], '-b', lw=5)

ax.plot(snake[:, 0], snake[:, 1], '--r', lw=5)