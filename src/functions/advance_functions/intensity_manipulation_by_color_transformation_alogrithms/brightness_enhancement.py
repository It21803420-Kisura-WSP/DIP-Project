from PIL import Image, ImageEnhance

def enhance_brightness_for_image(image_path, brightness_value):
    image = Image.open(image_path)
    brightness_enhancer = ImageEnhance.Brightness(image)
    outputted_image = brightness_enhancer.enhance(brightness_value)

    outputted_image.save('brightness_image.png')

    from PIL import Image, ImageEnhance, ImageTk
import tkinter as tk
import numpy as np
from src.util.fileUtil import get_resized_image
import cv2 as cv

def enhance_brightness():
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

    # Enhance the brightness of the image
    brightness_value = 2.5  # Set desired brightness level
    brightness_enhancer = ImageEnhance.Brightness(pil_image)
    enhanced_image = brightness_enhancer.enhance(brightness_value)

    # Convert the enhanced image to ImageTk for display in Tkinter
    final_img = ImageTk.PhotoImage(enhanced_image)

    # Clear the canvas before displaying the new image
    for widget in EditedImgCanvas.winfo_children():
        widget.destroy()

    # Display the enhanced image in the Tkinter canvas
    img_label = tk.Label(EditedImgCanvas, image=final_img)
    img_label.image = final_img  # Keep reference to avoid garbage collection
    img_label.pack()

# Example usage: enhance_brightness()