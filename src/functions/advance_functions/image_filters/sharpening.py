import cv2 as cv
import numpy as np
import tkinter as tk
from PIL import Image, ImageTk
from src.util.fileUtil import get_resized_image

def apply_image_sharpening(intensity):
    from src.gui.mainUI import get_EditedImgCanvas
    EditedImgCanvas = get_EditedImgCanvas()
    
    resized_img = get_resized_image()
    if resized_img is None:
        print("No image loaded")
        return
    
    intensity = float(intensity)

    sharpening_kernel = np.array([[0, -1, 0],
                                   [-1, 5 + intensity, -1],
                                   [0, -1, 0]])
    
    
    sharpened_image = cv.filter2D(resized_img, -1, sharpening_kernel)

    
    alpha = 0.5  
    blended_image = cv.addWeighted(resized_img, 1 - alpha, sharpened_image, alpha, 0)

    blended_image = cv.cvtColor(blended_image, cv.COLOR_BGR2RGB)
    finalImg = Image.fromarray(blended_image)
    finalfinalImg = ImageTk.PhotoImage(finalImg)

    for widget in EditedImgCanvas.winfo_children():
        widget.destroy()

    img_label = tk.Label(EditedImgCanvas, image=finalfinalImg)
    img_label.image = finalfinalImg
    img_label.pack()