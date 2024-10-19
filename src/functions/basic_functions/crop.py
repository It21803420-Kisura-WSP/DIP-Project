import cv2 as cv
import numpy as np
import tkinter as tk
from PIL import Image, ImageTk
from src.util.fileUtil import get_resized_image

def crop(startx, endx, starty, endy):
    from src.gui.mainUI import get_EditedImgCanvas
    EditedImgCanvas = get_EditedImgCanvas()

    
    resized_img = get_resized_image()
    if resized_img is None:
        print("No image loaded")
        return

    
    pil_image = Image.fromarray(cv.cvtColor(resized_img, cv.COLOR_BGR2RGB))

    
    cropped_image = pil_image.crop((startx, starty, endx, endy))

    
    finalImg = ImageTk.PhotoImage(cropped_image)

    
    for widget in EditedImgCanvas.winfo_children():
        widget.destroy()

    
    img_label = tk.Label(EditedImgCanvas, image=finalImg)
    img_label.image = finalImg  
    img_label.pack()
