import cv2 as cv
import numpy as np
import tkinter as tk
from PIL import Image, ImageTk
from src.util.fileUtil import get_resized_image


def convert_image_to_grayscale(intensity):
    from src.gui.mainUI import get_EditedImgCanvas
    EditedImgCanvas = get_EditedImgCanvas()

    resized_img = get_resized_image()
    if resized_img is None:
        print("No image loaded")
        return

    gray_image = cv.cvtColor(resized_img, cv.COLOR_BGR2GRAY)
    
    
    intensity = float(intensity) / 100  
    gray_image = cv.convertScaleAbs(gray_image, alpha=intensity)
    
    finalImg = Image.fromarray(gray_image)
    finalfinalImg = ImageTk.PhotoImage(finalImg)

    for widget in EditedImgCanvas.winfo_children():
        widget.destroy()

    img_label = tk.Label(EditedImgCanvas, image=finalfinalImg)
    img_label.image = finalfinalImg
    img_label.pack()


def convert_image_to_bw(intensity):
    from src.gui.mainUI import get_EditedImgCanvas
    EditedImgCanvas = get_EditedImgCanvas()

    resized_img = get_resized_image()
    if resized_img is None:
        print("No image loaded")
        return
    
    black_n_white_image = cv.cvtColor(resized_img, cv.COLOR_BGR2GRAY)
    
    
    threshold_value = int(intensity)
    (_, black_n_white_image) = cv.threshold(black_n_white_image, threshold_value, 255, cv.THRESH_BINARY)
    
    finalImg = Image.fromarray(black_n_white_image)
    finalfinalImg = ImageTk.PhotoImage(finalImg)

    for widget in EditedImgCanvas.winfo_children():
        widget.destroy()

    img_label = tk.Label(EditedImgCanvas, image=finalfinalImg)
    img_label.image = finalfinalImg
    img_label.pack()


def convert_image_to_color():
    from src.gui.mainUI import get_EditedImgCanvas
    EditedImgCanvas = get_EditedImgCanvas()

    resized_img = get_resized_image()
    if resized_img is None:
        print("No image loaded")
        return
    
    color_image = cv.cvtColor(resized_img, cv.COLOR_BGR2RGB)
    finalImg = Image.fromarray(color_image)
    finalfinalImg = ImageTk.PhotoImage(finalImg)

    for widget in EditedImgCanvas.winfo_children():
        widget.destroy()

    img_label = tk.Label(EditedImgCanvas, image=finalfinalImg)
    img_label.image = finalfinalImg
    img_label.pack()