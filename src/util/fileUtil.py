import tkinter as tk
from tkinter import filedialog
import cv2 as cv
from PIL import Image, ImageTk

resized_img = None


def upload_image(mainCanvas):
    global resized_img
    global image_on_canvas
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp")])
    if file_path:
        image = cv.imread(file_path)
        if image is not None:
            max_width, max_height = 600, 600 
            resized_img = resize_image(image, max_width, max_height)
            display_image(resized_img,mainCanvas)
            print("Image uploaded successfully")
        else:
            print("Failed to load the image")

def resize_image(image, max_width, max_height):
    height, width = image.shape[:2]
    scaling_factor = min(max_width / width, max_height / height)
    new_width = int(width * scaling_factor)
    new_height = int(height * scaling_factor)
    resized_img = cv.resize(image, (new_width, new_height), interpolation=cv.INTER_AREA)
    return resized_img  


def display_image(cv_image,mainCanvas):
    global image_on_canvas
    cv_image = cv.cvtColor(cv_image, cv.COLOR_BGR2RGB)
    tk_image = cv2_to_tk_image(cv_image)

    mainCanvas.delete("all")
    mainCanvas.create_image(0, 0, anchor=tk.NW, image=tk_image)
    image_on_canvas = tk_image

def cv2_to_tk_image(cv_image):
    image = Image.fromarray(cv_image)
    return ImageTk.PhotoImage(image)

def get_resized_image():
    global resized_img
    return resized_img

