from PIL import Image, ImageTk
import tkinter as tk
import numpy as np
from src.util.fileUtil import get_resized_image
import cv2 as cv


def apply_gamma_correction(gamma_value):
    """
    Applies gamma correction to the loaded image and displays it on the canvas.
    """
    from src.gui.mainUI import get_EditedImgCanvas
    EditedImgCanvas = get_EditedImgCanvas()

    # Load the resized image
    resized_img = get_resized_image()
    if resized_img is None:
        print("No image loaded")
        return

    # Convert the image to RGB format
    resized_img_rgb = cv.cvtColor(resized_img, cv.COLOR_BGR2RGB)

    # Apply gamma correction
    inv_gamma = 1.0 / gamma_value
    table = np.array([(i / 255.0) ** inv_gamma * 255 for i in np.arange(0, 256)]).astype("uint8")
    corrected_img = cv.LUT(resized_img_rgb, table)

    # Convert to PIL Image for Tkinter display
    pil_image = Image.fromarray(corrected_img)

    # Convert the PIL image to Tkinter compatible format
    final_img = ImageTk.PhotoImage(pil_image)

    # Clear the canvas and display the new image
    for widget in EditedImgCanvas.winfo_children():
        widget.destroy()

    img_label = tk.Label(EditedImgCanvas, image=final_img)
    img_label.image = final_img  
    img_label.pack()
