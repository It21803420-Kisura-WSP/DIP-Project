import os
import cv2
import numpy as np
import tkinter as tk
from PIL import Image, ImageTk
from tensorflow import keras
from keras.models import load_model
from src.util.fileUtil import get_resized_image

# Step 1: Add model path verification, model loading, and signature check
def load_denoising_model(model_path):
    try:
        # Load the model directly if it's a Keras/TensorFlow model saved as H5 or SavedModel format
        model = load_model(model_path)
        print("Model loaded successfully from:", model_path)
        return model
    except Exception as e:
        print(f"Failed to load model from {model_path}: {e}")
        return None

# Function to reduce noise in the image using ML
def reducing_noise(model):

    from src.gui.mainUI import get_EditedImgCanvas
    EditedImgCanvas = get_EditedImgCanvas()

    resized_img = get_resized_image()
    if resized_img is None:
        print("No image loaded")
        return

    # Prepare the input image
    input_image = cv2.cvtColor(np.array(resized_img), cv2.COLOR_RGB2BGR)
    input_image = input_image.astype('float32') / 255.0  # Normalize
    input_image = np.expand_dims(input_image, axis=0)  # Add batch dimension (shape becomes (1, height, width, 3))

    # Check input signature and adjust key names based on model's input signature
    try:
        # Use the model directly if it has a simple Keras call signature
        output = model(input_image)  # Directly call the model
        denoised_image = output.numpy()  # Convert tensor to NumPy array if it's a TensorFlow output
    except Exception as e:
        print(f"Error during noise reduction: {e}")
        return

    # Squeeze the image and prepare it for display
    denoised_image = np.squeeze(denoised_image)  # Remove batch dimension
    denoised_image = (denoised_image * 255).astype(np.uint8)  # Rescale to 0-255 for display
    denoised_image_rgb = cv2.cvtColor(denoised_image, cv2.COLOR_BGR2RGB)

    # Display the final image
    final_img = ImageTk.PhotoImage(Image.fromarray(denoised_image_rgb))
    for widget in EditedImgCanvas.winfo_children():
        widget.destroy()

    img_label = tk.Label(EditedImgCanvas, image=final_img)
    img_label.image = final_img
    img_label.pack()


# Load the denoising model
model_path = r'C:\Users\madha\.cache\kagglehub\models\kaggle\maxim\tensorFlow2\s-3-denoising-sidd\1'
model = load_denoising_model(model_path)

noise_reduction_intensity = 5  # Adjust as needed (0-10)

if model is None:
    print("Model loading failed. Exiting...")
else:
    # Example of how you might call reducing_noise() when needed
    # reducing_noise(model)
    print("Model is ready for use.")
