import cv2 as cv
import numpy as np
import tkinter as tk
from PIL import Image, ImageTk
from src.util.fileUtil import get_resized_image

def apply_edge_detection(low_threshold, upper_threshold):
    from src.gui.mainUI import get_EditedImgCanvas
    EditedImgCanvas = get_EditedImgCanvas()

    resized_img = get_resized_image()
    if resized_img is None:
        print("No image loaded")
        return

    low_threshold = int(low_threshold)  
    upper_threshold = int(upper_threshold)
    
    edged_image = cv.Canny(resized_img, low_threshold, upper_threshold)
    

    edged_image = cv.cvtColor(edged_image, cv.COLOR_BGR2RGB)
    finalImg = Image.fromarray(edged_image)
    finalfinalImg = ImageTk.PhotoImage(finalImg)

    for widget in EditedImgCanvas.winfo_children():
        widget.destroy()

    img_label = tk.Label(EditedImgCanvas, image=finalfinalImg)
    img_label.image = finalfinalImg
    img_label.pack()
