import cv2 as cv
import numpy as np
import tkinter as tk
from PIL import Image, ImageTk
from src.util.fileUtil import get_resized_image

def apply_smoothing(kernel_size, std_deviation):
    from src.gui.mainUI import get_EditedImgCanvas
    EditedImgCanvas = get_EditedImgCanvas()

    resized_img = get_resized_image()
    if resized_img is None:
        print("No image loaded")
        return
    

    kernel_size = int(kernel_size)
    if kernel_size % 2 == 0:
        kernel_size += 1  

    smoothed_image = cv.GaussianBlur(resized_img, (kernel_size, kernel_size), std_deviation)
    
    smoothed_image = cv.cvtColor(smoothed_image, cv.COLOR_BGR2RGB)
    finalImg = Image.fromarray(smoothed_image)
    finalfinalImg = ImageTk.PhotoImage(finalImg)

    for widget in EditedImgCanvas.winfo_children():
        widget.destroy()

    img_label = tk.Label(EditedImgCanvas, image=finalfinalImg)
    img_label.image = finalfinalImg
    img_label.pack()