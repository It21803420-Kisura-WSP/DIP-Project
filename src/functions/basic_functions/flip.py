from PIL import Image, ImageTk
import cv2 as cv
from src.util.fileUtil import get_resized_image
import tkinter as tk

def vertical_flip():
    from src.gui.mainUI import get_EditedImgCanvas
    EditedImgCanvas = get_EditedImgCanvas()
    
    # Get the resized image (assumed to be a NumPy array)
    resized_img = get_resized_image()
    if resized_img is None:
        print("No image loaded")
        return
    
    # Convert the NumPy array to a PIL Image
    pil_image = Image.fromarray(cv.cvtColor(resized_img, cv.COLOR_BGR2RGB))

    # Perform vertical flip
    vertical_image = pil_image.transpose(method=Image.FLIP_TOP_BOTTOM)

    # Convert back to PhotoImage for Tkinter
    finalImg = ImageTk.PhotoImage(vertical_image)

    # Clear previous widgets from the canvas
    for widget in EditedImgCanvas.winfo_children():
        widget.destroy()

    # Display the flipped image in the Tkinter canvas
    img_label = tk.Label(EditedImgCanvas, image=finalImg)
    img_label.image = finalImg  # Keep a reference to avoid garbage collection
    img_label.pack()


def horizontal_flip():
    from src.gui.mainUI import get_EditedImgCanvas
    EditedImgCanvas = get_EditedImgCanvas()
    
    # Get the resized image (assumed to be a NumPy array)
    resized_img = get_resized_image()
    if resized_img is None:
        print("No image loaded")
        return
    
    # Convert the NumPy array to a PIL Image
    pil_image = Image.fromarray(cv.cvtColor(resized_img, cv.COLOR_BGR2RGB))

    # Perform vertical flip
    vertical_image = pil_image.transpose(method=Image.FLIP_LEFT_RIGHT)

    # Convert back to PhotoImage for Tkinter
    finalImg = ImageTk.PhotoImage(vertical_image)

    # Clear previous widgets from the canvas
    for widget in EditedImgCanvas.winfo_children():
        widget.destroy()

    # Display the flipped image in the Tkinter canvas
    img_label = tk.Label(EditedImgCanvas, image=finalImg)
    img_label.image = finalImg  # Keep a reference to avoid garbage collection
    img_label.pack()