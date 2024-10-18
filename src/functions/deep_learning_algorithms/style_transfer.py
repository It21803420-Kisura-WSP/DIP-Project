
import tensorflow_hub as hub  
import tensorflow as tf  
import numpy as np  
import cv2  
from PIL import Image, ImageTk  
from src.util.fileUtil import get_resized_image
import tkinter as tk

# Load the model once at the start
model = hub.load('https://tfhub.dev/google/magenta/arbitrary-image-stylization-v1-256/2')

def using_google_arbitary_image_stylization_model(style: str, intensity: float):
    from src.gui.mainUI import get_EditedImgCanvas

    # Function to load an image from a file path (unchanged)
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

    # Get the resized image for content
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

    # Stylize the image with intensity consideration
    stylized_image = model(tf.constant(content_image), tf.constant(style_image))[0] * intensity

    # Convert the stylized image to RGB format for Pillow (unchanged)
    styled_image_rgb = cv2.cvtColor(np.squeeze(stylized_image) * 255, cv2.COLOR_BGR2RGB)

    # Convert the image to a format compatible with Tkinter (unchanged)
    final_img = ImageTk.PhotoImage(Image.fromarray(styled_image_rgb.astype(np.uint8)))

    EditedImgCanvas = get_EditedImgCanvas()

    # Clear the canvas before displaying the new image (unchanged)
    for widget in EditedImgCanvas.winfo_children():
        widget.destroy()

    img_label = tk.Label(EditedImgCanvas, image=final_img)
    img_label.image = final_img
    img_label.pack()