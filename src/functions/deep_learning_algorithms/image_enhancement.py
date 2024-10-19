import cv2
from matplotlib import pyplot as plt
import numpy as np
from src.util.fileUtil import get_resized_image
import tkinter as tk
from PIL import Image, ImageTk

def reducing_noise(intensity):
    from src.gui.mainUI import get_EditedImgCanvas
    EditedImgCanvas = get_EditedImgCanvas()

    resized_img = get_resized_image()
    if resized_img is None:
        print("No image loaded")
        return

    # Apply fast non-local means denoising with intensity control
    h = intensity  
    dst = cv2.fastNlMeansDenoisingColored(np.array(resized_img), None, h, 7, 21)

    # Convert to RGB for Tkinter
    denoised_image_rgb = cv2.cvtColor(dst, cv2.COLOR_BGR2RGB)
    final_img = ImageTk.PhotoImage(Image.fromarray(denoised_image_rgb))

    # Clear the canvas and display the new image
    for widget in EditedImgCanvas.winfo_children():
        widget.destroy()

    img_label = tk.Label(EditedImgCanvas, image=final_img)
    img_label.image = final_img
    img_label.pack()

def reducing_noise_colored(intensity):
    from src.gui.mainUI import get_EditedImgCanvas
    EditedImgCanvas = get_EditedImgCanvas()

    resized_img = get_resized_image()
    if resized_img is None:
        print("No image loaded")
        return

    # Adjust noise reduction intensity for both color and luminance
    h = intensity  
    dst = cv2.fastNlMeansDenoisingColored(np.array(resized_img), None, h, h, 7, 21)

    # Convert to RGB for Tkinter
    denoised_image_rgb = cv2.cvtColor(dst, cv2.COLOR_BGR2RGB)
    denoised_img_tk = ImageTk.PhotoImage(Image.fromarray(denoised_image_rgb))

    # Clear the canvas and display the new image
    for widget in EditedImgCanvas.winfo_children():
        widget.destroy()

    img_label = tk.Label(EditedImgCanvas, image=denoised_img_tk)
    img_label.image = denoised_img_tk
    img_label.pack()

def sharpening_image(intensity):
    from src.gui.mainUI import get_EditedImgCanvas
    EditedImgCanvas = get_EditedImgCanvas()

    resized_img = get_resized_image()
    if resized_img is None:
        print("No image loaded")
        return

    # Create a sharpening kernel adjusted by intensity
    intensity_value = max(intensity, 1)  
    kernel = np.array([[0, -1, 0], [-1, 5 + intensity_value, -1], [0, -1, 0]])

    # Apply sharpening
    sharpened_image = cv2.filter2D(resized_img, -1, kernel)

    # Convert to RGB for Tkinter
    sharpened_image_rgb = cv2.cvtColor(sharpened_image, cv2.COLOR_BGR2RGB)
    sharpened_img_tk = ImageTk.PhotoImage(Image.fromarray(sharpened_image_rgb))

    # Clear the canvas and display the new image
    for widget in EditedImgCanvas.winfo_children():
        widget.destroy()

    img_label = tk.Label(EditedImgCanvas, image=sharpened_img_tk)
    img_label.image = sharpened_img_tk
    img_label.pack()