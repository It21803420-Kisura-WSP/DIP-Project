from PIL import Image, ImageTk
import cv2 as cv
from src.util.fileUtil import get_resized_image
import tkinter as tk

def vertical_flip():
    from src.gui.mainUI import get_EditedImgCanvas
    EditedImgCanvas = get_EditedImgCanvas()
    

    resized_img = get_resized_image()
    if resized_img is None:
        print("No image loaded")
        return
    
    
    pil_image = Image.fromarray(cv.cvtColor(resized_img, cv.COLOR_BGR2RGB))

    
    vertical_image = pil_image.transpose(method=Image.FLIP_TOP_BOTTOM)

    
    finalImg = ImageTk.PhotoImage(vertical_image)

    
    for widget in EditedImgCanvas.winfo_children():
        widget.destroy()

   
    img_label = tk.Label(EditedImgCanvas, image=finalImg)
    img_label.image = finalImg 
    img_label.pack()


def horizontal_flip():
    from src.gui.mainUI import get_EditedImgCanvas
    EditedImgCanvas = get_EditedImgCanvas()
    
    
    resized_img = get_resized_image()
    if resized_img is None:
        print("No image loaded")
        return
    
    
    pil_image = Image.fromarray(cv.cvtColor(resized_img, cv.COLOR_BGR2RGB))

    
    vertical_image = pil_image.transpose(method=Image.FLIP_LEFT_RIGHT)

    
    finalImg = ImageTk.PhotoImage(vertical_image)

    
    for widget in EditedImgCanvas.winfo_children():
        widget.destroy()

   
    img_label = tk.Label(EditedImgCanvas, image=finalImg)
    img_label.image = finalImg  
    img_label.pack()