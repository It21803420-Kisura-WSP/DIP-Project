
import tensorflow_hub as hub  
import tensorflow as tf  
import numpy as np  
import cv2  
from PIL import Image, ImageTk  
from src.util.fileUtil import get_resized_image
import tkinter as tk

model = hub.load('https://tfhub.dev/google/magenta/arbitrary-image-stylization-v1-256/2')

def using_google_arbitary_image_stylization_model(style: str, intensity: float):
    from src.gui.mainUI import get_EditedImgCanvas

    
    def load_image(img_path):
        try:
            img = tf.io.read_file(img_path)
            img = tf.image.decode_image(img, channels=3)
            img = tf.image.convert_image_dtype(img, tf.float32)
            img = img[tf.newaxis, :]
            return img
        except Exception as e:
            print(f"Error loading image from {img_path}: {e}")
            return None

   
    resized_img = get_resized_image()
    if resized_img is None:
        print("No image loaded")
        return

    if isinstance(resized_img, np.ndarray):
        content_image = tf.convert_to_tensor(resized_img, dtype=tf.float32)
        content_image = content_image[tf.newaxis, :]
    else:
        content_image = load_image(resized_img)

    style_image = load_image(style)

    
    stylized_image = model(tf.constant(content_image), tf.constant(style_image))[0] * intensity

    
    styled_image_rgb = cv2.cvtColor(np.squeeze(stylized_image) * 255, cv2.COLOR_BGR2RGB)

   
    final_img = ImageTk.PhotoImage(Image.fromarray(styled_image_rgb.astype(np.uint8)))

    EditedImgCanvas = get_EditedImgCanvas()

   
    for widget in EditedImgCanvas.winfo_children():
        widget.destroy()

    img_label = tk.Label(EditedImgCanvas, image=final_img)
    img_label.image = final_img
    img_label.pack()