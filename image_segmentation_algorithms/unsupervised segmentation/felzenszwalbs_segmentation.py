# Felzenszwalb’s Segmentation 
from skimage.segmentation import felzenszwalb, mark_boundaries
from skimage.color import label2rgb
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

image = Image.open("image.png").convert("RGB")
image_array = np.array(image)

plt.figure(figsize=(15,15))
 
# computing the Felzenszwalb's
# Segmentation with sigma = 5 and minimum
# size = 100
image_segments = felzenszwalb(image_array, scale = 2, sigma=5, min_size=100)
 
# Plotting the original image
plt.subplot(1,2,1)
plt.imshow(image_array)
 
# Marking the boundaries of
# Felzenszwalb's segmentations
plt.subplot(1,2,2)
plt.imshow(mark_boundaries(image_array, image_segments))