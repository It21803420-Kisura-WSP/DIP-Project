from PIL import Image, ImageEnhance, ImageTk
import tkinter as tk
import numpy as np
from src.util.fileUtil import get_resized_image
import cv2 as cv

def enhance_brightness(brightness_value):
    """
    Adjust the brightness of the image based on the slider value.
    """
    from src.gui.mainUI import get_EditedImgCanvas
    EditedImgCanvas = get_EditedImgCanvas()

    resized_img = get_resized_image()
    if resized_img is None:
        print("No image loaded")
        return


    resized_img_rgb = cv.cvtColor(resized_img, cv.COLOR_BGR2RGB)
    pil_image = Image.fromarray(resized_img_rgb.astype('uint8'))

    
    brightness_enhancer = ImageEnhance.Brightness(pil_image)
    enhanced_image = brightness_enhancer.enhance(brightness_value)

    
    final_img = ImageTk.PhotoImage(enhanced_image)

    
    for widget in EditedImgCanvas.winfo_children():
        widget.destroy()

    
    img_label = tk.Label(EditedImgCanvas, image=final_img)
    img_label.image = final_img 
    img_label.pack()


def get_current_brightness():

    resized_img = get_resized_image()
    """
    Get the average brightness level of the image.
    """
    grayscale_img = cv.cvtColor(resized_img, cv.COLOR_BGR2GRAY)  
    avg_brightness = np.mean(grayscale_img) / 255  
    return avg_brightness