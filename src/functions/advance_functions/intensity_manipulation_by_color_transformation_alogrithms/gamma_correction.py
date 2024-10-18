# import cv2
# import numpy as np

# def gamma_correction(gamma_value):
#     inv_gamma = 1/gamma_value
#     table = [((i / 255) ** inv_gamma) * 255 for i in range(256)]
#     table = np.array(table, np.uint8)

#     return cv2.LUT(image_path, table)

# image = cv2.imread("image.png")
# gamma_image = gamma_correction(image, .2)

# cv2.imshow('Original image', image)
# cv2.imshow('Gamma corrected image', gamma_image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

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
    img_label.image = final_img  # Keep reference to avoid garbage collection
    img_label.pack()
