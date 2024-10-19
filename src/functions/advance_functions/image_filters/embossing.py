import cv2 as cv
import numpy as np
import tkinter as tk
from PIL import Image, ImageTk
from src.util.fileUtil import get_resized_image

def apply_emboss_filter(intensity):
    from src.gui.mainUI import get_EditedImgCanvas
    EditedImgCanvas = get_EditedImgCanvas()
    
    # Get the resized image
    resized_img = get_resized_image()
    if resized_img is None:
        print("No image loaded")
        return
    
    intensity = float(intensity)  
    
    if intensity == 0:
        # Show original image if intensity is 0
        original_img = cv.cvtColor(resized_img, cv.COLOR_BGR2RGB)
        finalImg = Image.fromarray(original_img)
        finalfinalImg = ImageTk.PhotoImage(finalImg)
        for widget in EditedImgCanvas.winfo_children():
            widget.destroy()
        img_label = tk.Label(EditedImgCanvas, image=finalfinalImg)
        img_label.image = finalfinalImg
        img_label.pack()
        return
    
    # Adjust embossing kernel based on intensity value
    embossing_kernel = np.array([[ -2 * intensity, -1 * intensity, 0],
                                 [ -1 * intensity,  1, 1 * intensity],
                                 [  0,  1 * intensity, 2 * intensity]])
    
    embossed_image = cv.filter2D(resized_img, -1, embossing_kernel)
    embossed_image = cv.cvtColor(embossed_image, cv.COLOR_BGR2RGB)
    
    finalImg = Image.fromarray(embossed_image)
    finalfinalImg = ImageTk.PhotoImage(finalImg)
    
    for widget in EditedImgCanvas.winfo_children():
        widget.destroy()

    img_label = tk.Label(EditedImgCanvas, image=finalfinalImg)
    img_label.image = finalfinalImg
    img_label.pack()
