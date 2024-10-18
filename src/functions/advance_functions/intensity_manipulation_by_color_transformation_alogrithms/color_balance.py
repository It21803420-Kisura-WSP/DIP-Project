import cv2
from PIL import Image, ImageTk
import numpy as np
from src.util.fileUtil import get_resized_image
import tkinter as tk

import cv2
from PIL import Image, ImageTk
import numpy as np
from src.util.fileUtil import get_resized_image

def color_correction(hue, saturation, value):
    from src.gui.mainUI import get_EditedImgCanvas
    EditedImgCanvas = get_EditedImgCanvas()

    # Get the resized image
    resized_img = get_resized_image()
    if resized_img is None:
        print("No image loaded")
        return

    # Convert resized image to numpy array for manipulation
    img_array = np.array(resized_img)

    # Convert to HSV
    hsv_img = cv2.cvtColor(img_array, cv2.COLOR_RGB2HSV)

    # Adjust Hue
    hsv_img[..., 0] = (hsv_img[..., 0] + hue) % 180  # Wrap around using modulo

    # Adjust Saturation
    hsv_img[..., 1] = np.clip(hsv_img[..., 1] * saturation, 0, 255)

    # Adjust Value (Brightness)
    hsv_img[..., 2] = np.clip(hsv_img[..., 2] * value, 0, 255)

    # Convert back to RGB
    corrected_img_array = cv2.cvtColor(hsv_img, cv2.COLOR_HSV2RGB)

    # Convert the corrected image array back to a PIL Image
    final_img = Image.fromarray(corrected_img_array.astype('uint8'))

    # Clear the canvas before displaying the new image
    for widget in EditedImgCanvas.winfo_children():
        widget.destroy()

    # Convert final image to ImageTk format for display in Tkinter
    final_img_tk = ImageTk.PhotoImage(final_img)

    # Display the image in the Tkinter canvas
    img_label = tk.Label(EditedImgCanvas, image=final_img_tk)
    img_label.image = final_img_tk  # Keep reference to avoid garbage collection
    img_label.pack()