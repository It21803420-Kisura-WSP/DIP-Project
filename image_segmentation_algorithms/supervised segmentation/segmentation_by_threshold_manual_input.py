# Segmentation by Threshold - Manual Input
from skimage.color import rgb2gray
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np

image = Image.open("image.png").convert("RGB")
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