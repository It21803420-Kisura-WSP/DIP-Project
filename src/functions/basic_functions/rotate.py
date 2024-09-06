import cv2 as cv
import numpy as np
import tkinter as tk
from PIL import Image, ImageTk


def rotate(resized_img):
    (h, w) = resized_img.shape[:2]
    center = (w // 2, h // 2)
    angle = 90
    rotation_matrix = cv.getRotationMatrix2D(center, angle)
    rotated_image = cv.warpAffine(resized_img, rotation_matrix, (w, h))
    print('wada wada')
    global image_on_canvas
    rgbConverted = cv.cvtColor(rotated_image, cv.COLOR_BGR2RGB)
    outputImg = cv2_to_tk_image(rgbConverted)

    frame3.delete("all")
    frame3.create_image(0, 0, anchor=tk.NW, image=outputImg)
    image_on_canvas = outputImg

def cv2_to_tk_image(rgbConverted):
    image = Image.fromarray(rgbConverted)
    return ImageTk.PhotoImage(image)
