from PIL import Image, ImageEnhance, ImageTk
import tkinter as tk
import numpy as np
from src.util.fileUtil import get_resized_image
import cv2 as cv

# def enhance_contrast():
#     from src.gui.mainUI import get_EditedImgCanvas
#     EditedImgCanvas = get_EditedImgCanvas()

#     resized_img = get_resized_image()
#     if resized_img is None:
#         print("No image loaded")
#         return

#     resized_img_rgb = cv.cvtColor(resized_img, cv.COLOR_BGR2RGB)
#     pil_image = Image.fromarray(resized_img_rgb.astype('uint8'))


#     contrast_value = 2.5  
#     contrast_enhancer = ImageEnhance.Contrast(pil_image)
#     enhanced_image = contrast_enhancer.enhance(contrast_value)

#     final_img = ImageTk.PhotoImage(enhanced_image)

#     for widget in EditedImgCanvas.winfo_children():
#         widget.destroy()

#     img_label = tk.Label(EditedImgCanvas, image=final_img)
#     img_label.image = final_img  
#     img_label.pack()

def enhance_contrast(contrast_value):
    """
    Adjusts contrast of the image based on the given value and displays it on the canvas.
    """
    from src.gui.mainUI import get_EditedImgCanvas
    EditedImgCanvas = get_EditedImgCanvas()

    # Load the resized image
    resized_img = get_resized_image()
    if resized_img is None:
        print("No image loaded")
        return

    # Convert the OpenCV image (BGR) to RGB format for PIL
    resized_img_rgb = cv.cvtColor(resized_img, cv.COLOR_BGR2RGB)
    pil_image = Image.fromarray(resized_img_rgb.astype('uint8'))

    # Apply contrast enhancement based on the slider value
    contrast_enhancer = ImageEnhance.Contrast(pil_image)
    enhanced_image = contrast_enhancer.enhance(contrast_value)

    # Convert the enhanced image to Tkinter compatible format
    final_img = ImageTk.PhotoImage(enhanced_image)

    # Clear the canvas and display the new image
    for widget in EditedImgCanvas.winfo_children():
        widget.destroy()

    img_label = tk.Label(EditedImgCanvas, image=final_img)
    img_label.image = final_img  
    img_label.pack()
