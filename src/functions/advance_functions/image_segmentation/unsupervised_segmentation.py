# un-supervised segmentation algorithms

# Global Imports
from skimage.segmentation import slic, mark_boundaries, felzenszwalb
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from skimage.color import label2rgb
import cv2

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


def k_means_clustering(image_path : str, kvalue : int):
    image = cv2.imread(image_path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Reshaping the image into a 2D array of pixels and 3 color values (RGB)
    pixel_vals = image.reshape((-1,3))
    
    # Convert to float type
    pixel_vals = np.float32(pixel_vals)

    #the below line of code defines the criteria for the algorithm to stop running, 
    #which will happen is 100 iterations are run or the epsilon (which is the required accuracy) 
    #becomes 85%
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.85)
    
    # then perform k-means clustering with number of clusters defined as 3
    #also random centres are initially choosed for k-means clustering
    k = kvalue
    retval, labels, centers = cv2.kmeans(pixel_vals, k, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)
    
    # convert data into 8-bit values
    centers = np.uint8(centers)
    segmented_data = centers[labels.flatten()]
    
    # reshape data into the original image dimensions
    segmented_image = segmented_data.reshape((image.shape))
    
    plt.imshow(segmented_image)

"""
test for k-means clustering
k_means_clustering("image.png", 3)
"""