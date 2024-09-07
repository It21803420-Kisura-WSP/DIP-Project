import cv2 as cv
import numpy as np
import tkinter as tk
from PIL import Image, ImageTk
from src.util.fileUtil import get_resized_image

def image_sharpening():

    from src.gui.mainUI import get_EditedImgCanvas
    EditedImgCanvas = get_EditedImgCanvas()
    resized_img = get_resized_image()

    sharpening_kernal = np.array([[0, -1, 0],
                   [-1, 5, -1],
                   [0, -1, 0]])
    sharpened_image = cv.filter2D(resized_img, -1, sharpening_kernal)

    sharpened_image = cv.cvtColor(sharpened_image, cv.COLOR_BGR2RGB)
    finalImg = Image.fromarray(sharpened_image)
    finalfinalImg = ImageTk.PhotoImage(finalImg)

    for widget in EditedImgCanvas.winfo_children():
        widget.destroy()

    img_label = tk.Label(EditedImgCanvas, image=finalfinalImg)
    img_label.image = finalfinalImg
    img_label.pack()


