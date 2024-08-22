# Simple Linear Iterative Clustering
from skimage.segmentation import slic
from skimage.color import label2rgb
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

image = Image.open("image.png").convert("RGB")
image_array = np.array(image)

plt.figure(figsize=(15,15))
 
# Applying Simple Linear Iterative
# Clustering on the image
# - 50 segments & compactness = 10
image_segments = slic(image_array, n_segments=50, compactness=10)
plt.subplot(1,2,1)
 
# Plotting the original image
plt.imshow(image_array)
plt.subplot(1,2,2)
 
# Converts a label image into
# an RGB color image for visualizing
# the labeled regions. 
plt.imshow(label2rgb(image_segments, image_array, kind = 'avg'))