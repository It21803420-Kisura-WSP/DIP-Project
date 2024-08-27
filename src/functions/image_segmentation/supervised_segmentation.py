# supervised segmentation algorithms

# Active Contour Imports
import numpy as np
import matplotlib.pyplot as plt
from skimage.color import rgb2gray
from skimage.filters import gaussian
from skimage.segmentation import active_contour
from PIL import Image

# Chan Vese Imports
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from skimage.color import rgb2gray
from skimage.segmentation import chan_vese

# Segmentation by threshold Manual Input
from skimage.color import rgb2gray
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np

# Segmentation by Skiimage Filter
from skimage import filters
from skimage.color import rgb2gray
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np



def active_contour(image_path : str):
    image = Image.open(image_path).convert("RGB")
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

def chan_vese(image_path : str):
    fig, axes = plt.subplots(1, 3, figsize=(10, 10))

    image = Image.open(image_path).convert("RGB")
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

def threshold_manual_input(image_path : str):
    image = Image.open(image_path).convert("RGB")
    image_array = np.array(image)

    gray_image = rgb2gray(image)

    # draw plot 
    plt.figure(figsize=(10,10))

    for i in range(10):
        binarized_gray = (gray_image > i*0.1)*1
        plt.subplot(5,2,i+1)
        plt.title("Threshold: >"+str(round(i*0.1,1)))
        plt.imshow(binarized_gray, cmap = 'gray')
    plt.tight_layout()

def threshold_using_skiimage_filter(image_path : str):
    image = Image.open(image_path).convert("RGB")
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