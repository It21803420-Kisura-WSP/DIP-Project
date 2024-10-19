import cv2 as cv
import tkinter as tk
from skimage import filters
from src.util.fileUtil import get_resized_image
from skimage.color import rgb2gray
from PIL import Image, ImageTk
import numpy as np
from skimage.segmentation import chan_vese
import matplotlib.pyplot as plt

def chan_vese_segmentation(max_iterations):
    from src.gui.mainUI import get_EditedImgCanvas
    EditedImgCanvas = get_EditedImgCanvas()

    resized_img = get_resized_image()
    print(f"Resized Image: {resized_img is not None}")
    if resized_img is None:
        print("No image loaded")
        return
    
    gray_image = rgb2gray(resized_img)

    chanvese_result = chan_vese(gray_image, max_num_iter=max_iterations, extended_output=True)
    print(f"Chan-Vese Result: {chanvese_result}")


    segmented_image = chanvese_result[0]  
    final_level_set = chanvese_result[1]  
    

    mask = segmented_image > 0
    output_image = np.zeros_like(gray_image)
    output_image[mask] = segmented_image[mask]


    combined_image = np.hstack((gray_image, output_image, final_level_set))
    print(f"Combined Image Shape: {combined_image.shape}, dtype: {combined_image.dtype}")


    combined_image_pil = Image.fromarray((combined_image * 255).astype(np.uint8))  
    final_img = ImageTk.PhotoImage(combined_image_pil)

    for widget in EditedImgCanvas.winfo_children():
        print(f"Clearing Widget: {widget}")
        widget.destroy()

    img_label = tk.Label(EditedImgCanvas, image=final_img)
    img_label.image = final_img  
    img_label.pack()





def threshold_manual_input(image_path : str):
    image = Image.open(image_path).convert("RGB")
    image_array = np.array(image)

    gray_image = rgb2gray(image)

    plt.figure(figsize=(10,10))

    for i in range(10):
        binarized_gray = (gray_image > i*0.1)*1
        plt.subplot(5,2,i+1)
        plt.title("Threshold: >"+str(round(i*0.1,1)))
        plt.imshow(binarized_gray, cmap = 'gray')
    plt.tight_layout()

import tkinter as tk
from skimage import filters
import numpy as np
from PIL import Image, ImageTk

def normalize_image(image):
    normalized_image = (image - np.min(image)) / (np.max(image) - np.min(image)) * 255
    return normalized_image.astype(np.uint8)  

def threshold_using_skiimage_filter(otsu_threshold, niblack_threshold, sauvola_threshold):
    from src.gui.mainUI import get_EditedImgCanvas
    EditedImgCanvas = get_EditedImgCanvas()

    resized_img = get_resized_image()
    if resized_img is None:
        print("No image loaded")
        return
    
    gray_image = rgb2gray(resized_img)


    normalized_gray_image = normalize_image(gray_image)


    if otsu_threshold == 0:
        otsu_threshold = filters.threshold_otsu(normalized_gray_image)
    binarized_image_otsu = (normalized_gray_image > otsu_threshold).astype(np.uint8) * 255  

    if niblack_threshold == 0:
        niblack_threshold = filters.threshold_niblack(normalized_gray_image)
    binarized_image_niblack = (normalized_gray_image > niblack_threshold).astype(np.uint8) * 255


    if sauvola_threshold == 0:
        sauvola_threshold = filters.threshold_sauvola(normalized_gray_image)
    binarized_image_sauvola = (normalized_gray_image > sauvola_threshold).astype(np.uint8) * 255

    
    combined_image = np.hstack((binarized_image_otsu, binarized_image_niblack, binarized_image_sauvola))

    
    binarized_image_pil = Image.fromarray(combined_image)
    final_img = ImageTk.PhotoImage(binarized_image_pil)

    for widget in EditedImgCanvas.winfo_children():
        widget.destroy()


    img_label = tk.Label(EditedImgCanvas, image=final_img)
    img_label.image = final_img  
    img_label.pack()
