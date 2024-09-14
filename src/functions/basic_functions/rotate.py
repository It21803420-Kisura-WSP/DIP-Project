import cv2 as cv
import numpy as np
import tkinter as tk
from PIL import Image, ImageTk
from src.util.fileUtil import get_resized_image

# Clockwise rotation functions
def rotate_90_cw():
    from src.gui.mainUI import get_EditedImgCanvas
    EditedImgCanvas = get_EditedImgCanvas()

    resized_img = get_resized_image()
    if resized_img is None:
        print("No image loaded")
        return
    (h, w) = resized_img.shape[:2]
    center = (w // 2, h // 2)
    angle = -90
    scale = 1.0
    rotation_matrix = cv.getRotationMatrix2D(center, angle,scale)

    abs_cos = abs(rotation_matrix[0, 0])
    abs_sin = abs(rotation_matrix[0, 1])
    new_w = int(h * abs_sin + w * abs_cos)
    new_h = int(h * abs_cos + w * abs_sin)
    
    rotation_matrix[0, 2] += new_w / 2 - center[0]
    rotation_matrix[1, 2] += new_h / 2 - center[1]

    rotated_image = cv.warpAffine(resized_img, rotation_matrix, (new_w, new_h))

    rotated_image = cv.cvtColor(rotated_image, cv.COLOR_BGR2RGB)
    finalImg = Image.fromarray(rotated_image)
    finalfinalImg = ImageTk.PhotoImage(finalImg)

    for widget in EditedImgCanvas.winfo_children():
        widget.destroy()

    img_label = tk.Label(EditedImgCanvas, image=finalfinalImg)
    img_label.image = finalfinalImg
    img_label.pack()

def rotate_180_cw():
    from src.gui.mainUI import get_EditedImgCanvas
    EditedImgCanvas = get_EditedImgCanvas()

    resized_img = get_resized_image()
    if resized_img is None:
        print("No image loaded")
        return
    (h, w) = resized_img.shape[:2]
    center = (w // 2, h // 2)
    angle = -180
    scale = 1.0
    rotation_matrix = cv.getRotationMatrix2D(center, angle,scale)

    abs_cos = abs(rotation_matrix[0, 0])
    abs_sin = abs(rotation_matrix[0, 1])
    new_w = int(h * abs_sin + w * abs_cos)
    new_h = int(h * abs_cos + w * abs_sin)
    
    rotation_matrix[0, 2] += new_w / 2 - center[0]
    rotation_matrix[1, 2] += new_h / 2 - center[1]

    rotated_image = cv.warpAffine(resized_img, rotation_matrix, (new_w, new_h))

    rotated_image = cv.cvtColor(rotated_image, cv.COLOR_BGR2RGB)
    finalImg = Image.fromarray(rotated_image)
    finalfinalImg = ImageTk.PhotoImage(finalImg)

    for widget in EditedImgCanvas.winfo_children():
        widget.destroy()

    img_label = tk.Label(EditedImgCanvas, image=finalfinalImg)
    img_label.image = finalfinalImg
    img_label.pack()

def rotate_270_cw():
    from src.gui.mainUI import get_EditedImgCanvas
    EditedImgCanvas = get_EditedImgCanvas()

    resized_img = get_resized_image()
    if resized_img is None:
        print("No image loaded")
        return
    (h, w) = resized_img.shape[:2]
    center = (w // 2, h // 2)
    angle = -270
    scale = 1.0
    rotation_matrix = cv.getRotationMatrix2D(center, angle,scale)

    abs_cos = abs(rotation_matrix[0, 0])
    abs_sin = abs(rotation_matrix[0, 1])
    new_w = int(h * abs_sin + w * abs_cos)
    new_h = int(h * abs_cos + w * abs_sin)
    
    rotation_matrix[0, 2] += new_w / 2 - center[0]
    rotation_matrix[1, 2] += new_h / 2 - center[1]

    rotated_image = cv.warpAffine(resized_img, rotation_matrix, (new_w, new_h))

    rotated_image = cv.cvtColor(rotated_image, cv.COLOR_BGR2RGB)
    finalImg = Image.fromarray(rotated_image)
    finalfinalImg = ImageTk.PhotoImage(finalImg)

    for widget in EditedImgCanvas.winfo_children():
        widget.destroy()

    img_label = tk.Label(EditedImgCanvas, image=finalfinalImg)
    img_label.image = finalfinalImg
    img_label.pack()

def rotate_360_cw():
    from src.gui.mainUI import get_EditedImgCanvas
    EditedImgCanvas = get_EditedImgCanvas()

    resized_img = get_resized_image()
    if resized_img is None:
        print("No image loaded")
        return
    (h, w) = resized_img.shape[:2]
    center = (w // 2, h // 2)
    angle = -360
    scale = 1.0
    rotation_matrix = cv.getRotationMatrix2D(center, angle,scale)

    abs_cos = abs(rotation_matrix[0, 0])
    abs_sin = abs(rotation_matrix[0, 1])
    new_w = int(h * abs_sin + w * abs_cos)
    new_h = int(h * abs_cos + w * abs_sin)
    
    rotation_matrix[0, 2] += new_w / 2 - center[0]
    rotation_matrix[1, 2] += new_h / 2 - center[1]

    rotated_image = cv.warpAffine(resized_img, rotation_matrix, (new_w, new_h))

    rotated_image = cv.cvtColor(rotated_image, cv.COLOR_BGR2RGB)
    finalImg = Image.fromarray(rotated_image)
    finalfinalImg = ImageTk.PhotoImage(finalImg)

    for widget in EditedImgCanvas.winfo_children():
        widget.destroy()

    img_label = tk.Label(EditedImgCanvas, image=finalfinalImg)
    img_label.image = finalfinalImg
    img_label.pack()

# Counter-clockwise rotation functions
def rotate_90_ccw():
    from src.gui.mainUI import get_EditedImgCanvas
    EditedImgCanvas = get_EditedImgCanvas()

    resized_img = get_resized_image()
    if resized_img is None:
        print("No image loaded")
        return
    (h, w) = resized_img.shape[:2]
    center = (w // 2, h // 2)
    angle = 90
    scale = 1.0
    rotation_matrix = cv.getRotationMatrix2D(center, angle,scale)

    abs_cos = abs(rotation_matrix[0, 0])
    abs_sin = abs(rotation_matrix[0, 1])
    new_w = int(h * abs_sin + w * abs_cos)
    new_h = int(h * abs_cos + w * abs_sin)
    
    rotation_matrix[0, 2] += new_w / 2 - center[0]
    rotation_matrix[1, 2] += new_h / 2 - center[1]

    rotated_image = cv.warpAffine(resized_img, rotation_matrix, (new_w, new_h))

    rotated_image = cv.cvtColor(rotated_image, cv.COLOR_BGR2RGB)
    finalImg = Image.fromarray(rotated_image)
    finalfinalImg = ImageTk.PhotoImage(finalImg)

    for widget in EditedImgCanvas.winfo_children():
        widget.destroy()

    img_label = tk.Label(EditedImgCanvas, image=finalfinalImg)
    img_label.image = finalfinalImg
    img_label.pack()

def rotate_180_ccw():
    from src.gui.mainUI import get_EditedImgCanvas
    EditedImgCanvas = get_EditedImgCanvas()

    resized_img = get_resized_image()
    if resized_img is None:
        print("No image loaded")
        return
    (h, w) = resized_img.shape[:2]
    center = (w // 2, h // 2)
    angle = 180
    scale = 1.0
    rotation_matrix = cv.getRotationMatrix2D(center, angle,scale)

    abs_cos = abs(rotation_matrix[0, 0])
    abs_sin = abs(rotation_matrix[0, 1])
    new_w = int(h * abs_sin + w * abs_cos)
    new_h = int(h * abs_cos + w * abs_sin)
    
    rotation_matrix[0, 2] += new_w / 2 - center[0]
    rotation_matrix[1, 2] += new_h / 2 - center[1]

    rotated_image = cv.warpAffine(resized_img, rotation_matrix, (new_w, new_h))

    rotated_image = cv.cvtColor(rotated_image, cv.COLOR_BGR2RGB)
    finalImg = Image.fromarray(rotated_image)
    finalfinalImg = ImageTk.PhotoImage(finalImg)

    for widget in EditedImgCanvas.winfo_children():
        widget.destroy()

    img_label = tk.Label(EditedImgCanvas, image=finalfinalImg)
    img_label.image = finalfinalImg
    img_label.pack()

def rotate_270_ccw():
    from src.gui.mainUI import get_EditedImgCanvas
    EditedImgCanvas = get_EditedImgCanvas()

    resized_img = get_resized_image()
    if resized_img is None:
        print("No image loaded")
        return
    (h, w) = resized_img.shape[:2]
    center = (w // 2, h // 2)
    angle = 270
    scale = 1.0
    rotation_matrix = cv.getRotationMatrix2D(center, angle,scale)

    abs_cos = abs(rotation_matrix[0, 0])
    abs_sin = abs(rotation_matrix[0, 1])
    new_w = int(h * abs_sin + w * abs_cos)
    new_h = int(h * abs_cos + w * abs_sin)
    
    rotation_matrix[0, 2] += new_w / 2 - center[0]
    rotation_matrix[1, 2] += new_h / 2 - center[1]

    rotated_image = cv.warpAffine(resized_img, rotation_matrix, (new_w, new_h))

    rotated_image = cv.cvtColor(rotated_image, cv.COLOR_BGR2RGB)
    finalImg = Image.fromarray(rotated_image)
    finalfinalImg = ImageTk.PhotoImage(finalImg)

    for widget in EditedImgCanvas.winfo_children():
        widget.destroy()

    img_label = tk.Label(EditedImgCanvas, image=finalfinalImg)
    img_label.image = finalfinalImg
    img_label.pack()

def rotate_360_ccw():
    from src.gui.mainUI import get_EditedImgCanvas
    EditedImgCanvas = get_EditedImgCanvas()

    resized_img = get_resized_image()
    if resized_img is None:
        print("No image loaded")
        return
    (h, w) = resized_img.shape[:2]
    center = (w // 2, h // 2)
    angle = 360
    scale = 1.0
    rotation_matrix = cv.getRotationMatrix2D(center, angle,scale)

    abs_cos = abs(rotation_matrix[0, 0])
    abs_sin = abs(rotation_matrix[0, 1])
    new_w = int(h * abs_sin + w * abs_cos)
    new_h = int(h * abs_cos + w * abs_sin)
    
    rotation_matrix[0, 2] += new_w / 2 - center[0]
    rotation_matrix[1, 2] += new_h / 2 - center[1]

    rotated_image = cv.warpAffine(resized_img, rotation_matrix, (new_w, new_h))

    rotated_image = cv.cvtColor(rotated_image, cv.COLOR_BGR2RGB)
    finalImg = Image.fromarray(rotated_image)
    finalfinalImg = ImageTk.PhotoImage(finalImg)

    for widget in EditedImgCanvas.winfo_children():
        widget.destroy()

    img_label = tk.Label(EditedImgCanvas, image=finalfinalImg)
    img_label.image = finalfinalImg
    img_label.pack()