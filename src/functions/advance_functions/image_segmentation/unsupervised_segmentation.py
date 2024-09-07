# un-supervised segmentation algorithms

# Felzenszwalb’s Segmentation Imports
from skimage.segmentation import felzenszwalb, mark_boundaries
from skimage.color import label2rgb
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

# Mark Bounderies Imports
from skimage.segmentation import slic, mark_boundaries
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

# Simple Linear Iterative Clustering Imports
from skimage.segmentation import slic
from skimage.color import label2rgb
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

def felzenszwalbs(image_path : str):
    image = Image.open(image_path).convert("RGB")
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


def mark_bounderies(image_path : str):
    image = Image.open(image_path).convert("RGB")
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

def simple_linear_iterative_clustering(image_path : str):
    image = Image.open(image_path).convert("RGB")
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