# Mark Bounderies
from skimage.segmentation import slic, mark_boundaries
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

image = Image.open("image.png").convert("RGB")
image_array = np.array(image)

plt.figure(figsize=(15, 15))

# Applying SLIC segmentation
# for the edges to be drawn over
image_segments = slic(image_array, n_segments=100, compactness=1)

plt.subplot(1, 2, 1)
plt.imshow(image)

# Detecting boundaries for labels
plt.subplot(1, 2, 2)
 
# Plotting the output of marked_boundaries
# function i.e. the image with segmented boundaries
plt.imshow(mark_boundaries(image_array, image_segments))