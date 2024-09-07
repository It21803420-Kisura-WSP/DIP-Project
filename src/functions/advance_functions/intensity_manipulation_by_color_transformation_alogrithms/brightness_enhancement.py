from PIL import Image, ImageEnhance, ImageTk
import tkinter as tk
import numpy as np
from src.util.fileUtil import get_resized_image
import cv2 as cv


def enhance_brightness_for_image(image_path, brightness_value):
    image = Image.open(image_path)
    brightness_enhancer = ImageEnhance.Brightness(image)
    outputted_image = brightness_enhancer.enhance(brightness_value)

    outputted_image.save('brightness_image.png')


def enhance_brightness():
    from src.gui.mainUI import get_EditedImgCanvas
    EditedImgCanvas = get_EditedImgCanvas()

    resized_img = get_resized_image()
    if resized_img is None:
        print("No image loaded")
        return

    resized_img_rgb = cv.cvtColor(resized_img, cv.COLOR_BGR2RGB)
    pil_image = Image.fromarray(resized_img_rgb.astype('uint8'))

    brightness_value = 2.5  
    brightness_enhancer = ImageEnhance.Brightness(pil_image)
    enhanced_image = brightness_enhancer.enhance(brightness_value)

    final_img = ImageTk.PhotoImage(enhanced_image)

    for widget in EditedImgCanvas.winfo_children():
        widget.destroy()

    img_label = tk.Label(EditedImgCanvas, image=final_img)
    img_label.image = final_img  
    img_label.pack()
