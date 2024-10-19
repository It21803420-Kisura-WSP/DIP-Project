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

   
    resized_img = get_resized_image()
    if resized_img is None:
        print("No image loaded")
        return

    
    img_array = np.array(resized_img)

    
    hsv_img = cv2.cvtColor(img_array, cv2.COLOR_RGB2HSV)

    
    hsv_img[..., 0] = (hsv_img[..., 0] + hue) % 180  

    
    hsv_img[..., 1] = np.clip(hsv_img[..., 1] * saturation, 0, 255)

    
    hsv_img[..., 2] = np.clip(hsv_img[..., 2] * value, 0, 255)

    
    corrected_img_array = cv2.cvtColor(hsv_img, cv2.COLOR_HSV2RGB)

    
    final_img = Image.fromarray(corrected_img_array.astype('uint8'))

    
    for widget in EditedImgCanvas.winfo_children():
        widget.destroy()

    
    final_img_tk = ImageTk.PhotoImage(final_img)

    
    img_label = tk.Label(EditedImgCanvas, image=final_img_tk)
    img_label.image = final_img_tk  
    img_label.pack()