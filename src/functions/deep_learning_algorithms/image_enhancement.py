import os
import cv2
import numpy as np
import tkinter as tk
from PIL import Image, ImageTk
import kagglehub
import tensorflow as tf
from keras.layers import TFSMLayer  
from src.util.fileUtil import get_resized_image


# Step 1: Add model path verification, model loading, and signature check
def load_denoising_model(model_path):
    try:
        # Use the correct endpoint
        model = TFSMLayer(model_path, call_endpoint='serving_default')
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
    input_image = np.expand_dims(input_image, axis=0)  # Add batch dimension

    # Get the model's default serving signature
    serving_fn = model.signatures['serving_default']

    # Get the input tensor names from the signature dynamically
    input_keys = list(serving_fn.structured_input_signature[1].keys())

    # Create the input dictionary based on the expected keys
    if len(input_keys) >= 2:
        input_dict = {
            input_keys[0]: input_image,
            input_keys[1]: input_image,  # Adjust if the placeholders require different data
        }
    else:
        print("Unexpected number of inputs in the model signature")
        return

    # Call the model with the input dictionary
    try:
        output = serving_fn(**input_dict)  # Ensure you're using named arguments
        output_key = list(output.keys())[0]  # Get the output key dynamically
        denoised_image = output[output_key].numpy()  # Access output using the dynamic key
    except TypeError as e:
        print("TypeError:", e)
        return

    # Squeeze the image and prepare it for display
    denoised_image = np.squeeze(denoised_image)
    denoised_image = (denoised_image * 255).astype(np.uint8)  # Rescale to 0-255
    denoised_image_rgb = cv2.cvtColor(denoised_image, cv2.COLOR_BGR2RGB)

    # Display the final image
    final_img = ImageTk.PhotoImage(Image.fromarray(denoised_image_rgb))
    for widget in EditedImgCanvas.winfo_children():
        widget.destroy()

    img_label = tk.Label(EditedImgCanvas, image=final_img)
    img_label.image = final_img
    img_label.pack()


# Download and load the denoising model using kagglehub
path = kagglehub.model_download("kaggle/maxim/tensorFlow2/s-3-denoising-sidd")
print("Path to model files:", path)

model = load_denoising_model(path)

noise_reduction_intensity = 5  # Adjust as needed (0-10)

if model is None:
    print("Model loading failed. Exiting...")
else:
    # Call reducing_noise() when you want to reduce noise in an image
    # For example: reducing_noise(model)
    print("Model is ready for use.")
