# Image Enhancement Algorithms
import cv2
from matplotlib import pyplot as plt
import numpy as np 

def reducing_noise(image_path : str):
    img = cv2.imread(image_path)
    dst = cv2.fastNlMeansDenoising(img,None,3,7,21)
    plt.subplot(121),plt.imshow(img)
    plt.subplot(122),plt.imshow(dst)
    plt.show()

def reducing_noise_colored(image_path : str):
    img = cv2.imread(image_path)
    dst = cv2.fastNlMeansDenoisingColored(img,None,10,10,7,21)
    plt.subplot(121),plt.imshow(img)
    plt.subplot(122),plt.imshow(dst)
    plt.show()

def sharpening_image(image_path : str):
    # Load the image 
    image = cv2.imread(image_path) 
    
    #Plot the original image 
    plt.subplot(1, 2, 1) 
    plt.title("Original") 
    plt.imshow(image) 
    
    # Create the sharpening kernel 
    kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]]) 
    
    # Sharpen the image 
    sharpened_image = cv2.filter2D(image, -1, kernel) 
    
    #Save the image 
    cv2.imwrite('sharpened_image.jpg', sharpened_image) 
    
    #Plot the sharpened image 
    plt.subplot(1, 2, 2) 
    plt.title("Sharpening") 
    plt.imshow(sharpened_image) 
    plt.show()

    return sharpened_image

def histogram_equalization(image):
    ycrcb = cv2.cvtColor(image, cv2.COLOR_BGR2YCrCb)
    
    ycrcb[:, :, 0] = cv2.equalizeHist(ycrcb[:, :, 0])
    
    equalized_image = cv2.cvtColor(ycrcb, cv2.COLOR_YCrCb2BGR)

    return equalized_image

def CLAHE(image):
    lab = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
   
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    lab[:, :, 0] = clahe.apply(lab[:, :, 0])
 
    clahe_image = cv2.cvtColor(lab, cv2.COLOR_LAB2BGR)

    return clahe_image