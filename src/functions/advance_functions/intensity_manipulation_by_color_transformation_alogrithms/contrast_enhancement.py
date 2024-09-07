from PIL import Image, ImageEnhance, ImageTk
import tkinter as tk
import numpy as np
from src.util.fileUtil import get_resized_image
import cv2 as cv

def enhance_contrast():
    from src.gui.mainUI import get_EditedImgCanvas
    EditedImgCanvas = get_EditedImgCanvas()

    # Load the resized image using the utility function
    resized_img = get_resized_image()
    if resized_img is None:
        print("No image loaded")
        return

    # Convert the BGR numpy array to RGB before converting to PIL Image
    resized_img_rgb = cv.cvtColor(resized_img, cv.COLOR_BGR2RGB)
    pil_image = Image.fromarray(resized_img_rgb.astype('uint8'))

    # Enhance the contrast of the image
    contrast_value = 2.5  # Set desired contrast level
    contrast_enhancer = ImageEnhance.Contrast(pil_image)
    enhanced_image = contrast_enhancer.enhance(contrast_value)

    # Convert the enhanced image to ImageTk for display in Tkinter
    final_img = ImageTk.PhotoImage(enhanced_image)

    # Clear the canvas before displaying the new image
    for widget in EditedImgCanvas.winfo_children():
        widget.destroy()

    # Display the enhanced image in the Tkinter canvas
    img_label = tk.Label(EditedImgCanvas, image=final_img)
    img_label.image = final_img  # Keep reference to avoid garbage collection
    img_label.pack()

