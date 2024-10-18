# # Image Enhancement Algorithms
# import cv2
# from matplotlib import pyplot as plt
# import numpy as np 
# from src.util.fileUtil import get_resized_image
# import tkinter as tk
# from PIL import Image, ImageTk

# def reducing_noise():
#     from src.gui.mainUI import get_EditedImgCanvas
#     EditedImgCanvas = get_EditedImgCanvas()

#     resized_img = get_resized_image()
#     if resized_img is None:
#         print("No image loaded")
#         return

#     # Convert the resized image to a numpy array
#     image_array = np.array(resized_img)

#     # Apply fast non-local means denoising
#     dst = cv2.fastNlMeansDenoisingColored(image_array, None, 3, 7, 21)

#     # Convert the denoised image to RGB format for Pillow
#     denoised_image_rgb = cv2.cvtColor(dst, cv2.COLOR_BGR2RGB)

#     # Convert the image to a format compatible with Tkinter
#     final_img = ImageTk.PhotoImage(Image.fromarray(denoised_image_rgb))

#     # Clear the canvas before displaying the new image
#     for widget in EditedImgCanvas.winfo_children():
#         widget.destroy()

#     # Display the denoised image in the Tkinter canvas
#     img_label = tk.Label(EditedImgCanvas, image=final_img)
#     img_label.image = final_img  # Keep reference to avoid garbage collection
#     img_label.pack()


# def reducing_noise_colored():
#     from src.gui.mainUI import get_EditedImgCanvas

#     EditedImgCanvas = get_EditedImgCanvas()

#     # Get the resized image
#     resized_img = get_resized_image()
#     if resized_img is None:
#         print("No image loaded")
#         return

#     # Increase the effect of the denoising process
#     h = 30  # Increased filter strength
#     templateWindowSize = 7  # Increased size of the template window
#     searchWindowSize = 21  # Increased size of the search window

#     # Apply fast non-local means denoising
#     dst = cv2.fastNlMeansDenoisingColored(resized_img, None, h, h, templateWindowSize, searchWindowSize)

#     # Convert the denoised image to RGB format for Pillow
#     denoised_image_rgb = cv2.cvtColor(dst, cv2.COLOR_BGR2RGB)

#     # Convert the denoised image to a format compatible with Tkinter
#     denoised_img_tk = ImageTk.PhotoImage(Image.fromarray(denoised_image_rgb))

#     # Clear the canvas before displaying the new image
#     for widget in EditedImgCanvas.winfo_children():
#         widget.destroy()

#     # Create a label for the denoised image
#     denoised_label = tk.Label(EditedImgCanvas, image=denoised_img_tk)
#     denoised_label.image = denoised_img_tk  # Keep reference to avoid garbage collection
#     denoised_label.pack()  # Display the denoised image





# def sharpening_image():
#     from src.gui.mainUI import get_EditedImgCanvas

#     EditedImgCanvas = get_EditedImgCanvas()

#     # Get the resized image
#     resized_img = get_resized_image()
#     if resized_img is None:
#         print("No image loaded")
#         return

#     # Create the sharpening kernel
#     kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])

#     # Sharpen the image
#     sharpened_image = cv2.filter2D(resized_img, -1, kernel)

#     # Convert the sharpened image to RGB format for Pillow
#     sharpened_image_rgb = cv2.cvtColor(sharpened_image, cv2.COLOR_BGR2RGB)

#     # Convert the sharpened image to a format compatible with Tkinter
#     sharpened_img_tk = ImageTk.PhotoImage(Image.fromarray(sharpened_image_rgb))

#     # Clear the canvas before displaying the new image
#     for widget in EditedImgCanvas.winfo_children():
#         widget.destroy()

#     # Create a label for the sharpened image
#     sharpened_label = tk.Label(EditedImgCanvas, image=sharpened_img_tk)
#     sharpened_label.image = sharpened_img_tk  # Keep reference to avoid garbage collection
#     sharpened_label.pack()  # Display the sharpened image

#     # Save the sharpened image (optional)
#     cv2.imwrite('sharpened_image.jpg', sharpened_image)


import cv2
from matplotlib import pyplot as plt
import numpy as np
from src.util.fileUtil import get_resized_image
import tkinter as tk
from PIL import Image, ImageTk

def reducing_noise(intensity):
    from src.gui.mainUI import get_EditedImgCanvas
    EditedImgCanvas = get_EditedImgCanvas()

    resized_img = get_resized_image()
    if resized_img is None:
        print("No image loaded")
        return

    # Apply fast non-local means denoising with intensity control
    h = intensity  
    dst = cv2.fastNlMeansDenoisingColored(np.array(resized_img), None, h, 7, 21)

    # Convert to RGB for Tkinter
    denoised_image_rgb = cv2.cvtColor(dst, cv2.COLOR_BGR2RGB)
    final_img = ImageTk.PhotoImage(Image.fromarray(denoised_image_rgb))

    # Clear the canvas and display the new image
    for widget in EditedImgCanvas.winfo_children():
        widget.destroy()

    img_label = tk.Label(EditedImgCanvas, image=final_img)
    img_label.image = final_img
    img_label.pack()

def reducing_noise_colored(intensity):
    from src.gui.mainUI import get_EditedImgCanvas
    EditedImgCanvas = get_EditedImgCanvas()

    resized_img = get_resized_image()
    if resized_img is None:
        print("No image loaded")
        return

    # Adjust noise reduction intensity for both color and luminance
    h = intensity  
    dst = cv2.fastNlMeansDenoisingColored(np.array(resized_img), None, h, h, 7, 21)

    # Convert to RGB for Tkinter
    denoised_image_rgb = cv2.cvtColor(dst, cv2.COLOR_BGR2RGB)
    denoised_img_tk = ImageTk.PhotoImage(Image.fromarray(denoised_image_rgb))

    # Clear the canvas and display the new image
    for widget in EditedImgCanvas.winfo_children():
        widget.destroy()

    img_label = tk.Label(EditedImgCanvas, image=denoised_img_tk)
    img_label.image = denoised_img_tk
    img_label.pack()

def sharpening_image(intensity):
    from src.gui.mainUI import get_EditedImgCanvas
    EditedImgCanvas = get_EditedImgCanvas()

    resized_img = get_resized_image()
    if resized_img is None:
        print("No image loaded")
        return

    # Create a sharpening kernel adjusted by intensity
    intensity_value = max(intensity, 1)  
    kernel = np.array([[0, -1, 0], [-1, 5 + intensity_value, -1], [0, -1, 0]])

    # Apply sharpening
    sharpened_image = cv2.filter2D(resized_img, -1, kernel)

    # Convert to RGB for Tkinter
    sharpened_image_rgb = cv2.cvtColor(sharpened_image, cv2.COLOR_BGR2RGB)
    sharpened_img_tk = ImageTk.PhotoImage(Image.fromarray(sharpened_image_rgb))

    # Clear the canvas and display the new image
    for widget in EditedImgCanvas.winfo_children():
        widget.destroy()

    img_label = tk.Label(EditedImgCanvas, image=sharpened_img_tk)
    img_label.image = sharpened_img_tk
    img_label.pack()