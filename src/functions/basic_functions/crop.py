import cv2 as cv
import numpy as np
import tkinter as tk
from PIL import Image, ImageTk
from src.util.fileUtil import get_resized_image

def crop(startx, endx, starty, endy):
    from src.gui.mainUI import get_EditedImgCanvas
    EditedImgCanvas = get_EditedImgCanvas()

    # Get the resized image (assumed to be a NumPy array)
    resized_img = get_resized_image()
    if resized_img is None:
        print("No image loaded")
        return

    # Convert the NumPy array to a PIL Image
    pil_image = Image.fromarray(cv.cvtColor(resized_img, cv.COLOR_BGR2RGB))

    # Perform cropping
    # Note: The crop method requires a bounding box (left, upper, right, lower)
    cropped_image = pil_image.crop((startx, starty, endx, endy))

    # Convert back to PhotoImage for Tkinter
    finalImg = ImageTk.PhotoImage(cropped_image)

    # Clear previous widgets from the canvas
    for widget in EditedImgCanvas.winfo_children():
        widget.destroy()

    # Display the cropped image in the Tkinter canvas
    img_label = tk.Label(EditedImgCanvas, image=finalImg)
    img_label.image = finalImg  
    img_label.pack()
