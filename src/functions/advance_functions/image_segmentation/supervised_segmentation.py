# supervised segmentation algorithms

# Active Contour Imports
import cv2 as cv
import numpy as np
import tkinter as tk
import matplotlib.pyplot as plt
from skimage.color import rgb2gray
from skimage.filters import gaussian
from skimage.segmentation import active_contour
from PIL import Image
from src.util.fileUtil import get_resized_image


# Chan Vese Imports
from PIL import Image
import numpy as np
from PIL import Image, ImageTk
import matplotlib.pyplot as plt
from skimage.color import rgb2gray
from skimage.segmentation import chan_vese

# Segmentation by threshold Manual Input
from skimage.color import rgb2gray
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np

# Segmentation by Skiimage Filter
from skimage import filters
from skimage.color import rgb2gray
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np



def active_contour_segmentation():
    from src.gui.mainUI import get_EditedImgCanvas
    EditedImgCanvas = get_EditedImgCanvas()

    resized_img = get_resized_image()
    if resized_img is None:
        print("No image loaded")
        return
    
    image_array = np.array(resized_img)
    gray_image = rgb2gray(resized_img)

    # Apply gaussian filter
    gray_image_noiseless = gaussian(gray_image, 1)

    # Localizing the circle's center (initial snake)
    x1 = 220 + 100 * np.cos(np.linspace(0, 2 * np.pi, 500))
    x2 = 100 + 100 * np.sin(np.linspace(0, 2 * np.pi, 500))

    # Generating a circle (initial snake) based on x1, x2
    snake = np.array([x1, x2]).T

    # Computing the Active Contour for the given image using active_contour() function
    image_snake = active_contour(gray_image_noiseless, snake)

    # Create a figure and axes using Matplotlib
    fig, ax = plt.subplots()
    ax.imshow(gray_image_noiseless, cmap='gray')

    # Plot the initial snake (red dashed line)
    ax.plot(snake[:, 0], snake[:, 1], '--r', lw=3)

    # Plot the active contour result (blue solid line)
    ax.plot(image_snake[:, 0], image_snake[:, 1], '-b', lw=3)

    # Save the Matplotlib figure to a temporary file
    fig.savefig("active_contour_output.png")
    plt.close(fig)

    # Load the saved image as a PIL image
    pil_image = Image.open("active_contour_output.png")
    final_img = ImageTk.PhotoImage(pil_image)

    # Clear the canvas before displaying the new image
    for widget in EditedImgCanvas.winfo_children():
        widget.destroy()

    # Display the image in the Tkinter canvas
    img_label = tk.Label(EditedImgCanvas, image=final_img)
    img_label.image = final_img  # Keep reference to avoid garbage collection
    img_label.pack()


def chan_vese(image_path : str):
    fig, axes = plt.subplots(1, 3, figsize=(10, 10))

    image = Image.open(image_path).convert("RGB")
    image_array = np.array(image)
    gray_image = rgb2gray(image)

    # Computing the Chan VESE segmentation technique
    chanvese_gray_image = chan_vese(gray_image, max_num_iter=100, extended_output=True)
    ax = axes.flatten()
    
    # Plotting the original image
    ax[0].imshow(gray_image, cmap="gray")
    ax[0].set_title("Original Image")
    
    # Plotting the segmented - 100 iterations image
    ax[1].imshow(chanvese_gray_image[0], cmap="gray")
    title = "Chan-Vese segmentation - {} iterations".format(len(chanvese_gray_image[2]))
    
    ax[1].set_title(title)
    
    # Plotting the final level set
    ax[2].imshow(chanvese_gray_image[1], cmap="gray")
    ax[2].set_title("Final Level Set")
    plt.show()

def threshold_manual_input(image_path : str):
    image = Image.open(image_path).convert("RGB")
    image_array = np.array(image)

    gray_image = rgb2gray(image)

    # draw plot 
    plt.figure(figsize=(10,10))

    for i in range(10):
        binarized_gray = (gray_image > i*0.1)*1
        plt.subplot(5,2,i+1)
        plt.title("Threshold: >"+str(round(i*0.1,1)))
        plt.imshow(binarized_gray, cmap = 'gray')
    plt.tight_layout()

def threshold_using_skiimage_filter():
    from src.gui.mainUI import get_EditedImgCanvas
    EditedImgCanvas = get_EditedImgCanvas()

    resized_img = get_resized_image()
    if resized_img is None:
        print("No image loaded")
        return
    
    image_array = np.array(resized_img)
    gray_image = rgb2gray(resized_img)

    # Otsu Thresholding
    threshold = filters.threshold_otsu(gray_image)
    binarized_image_otsu = (gray_image > threshold).astype(np.uint8) * 255  # Convert to 0-255

    # Niblack Thresholding
    threshold_niblack = filters.threshold_niblack(gray_image)
    binarized_image_niblack = (gray_image > threshold_niblack).astype(np.uint8) * 255

    # Sauvola Thresholding
    threshold_sauvola = filters.threshold_sauvola(gray_image)
    binarized_image_sauvola = (gray_image > threshold_sauvola).astype(np.uint8) * 255

    # Combine the three images horizontally for display in Tkinter
    combined_image = np.hstack((binarized_image_otsu, binarized_image_niblack, binarized_image_sauvola))

    # Convert binary image to PIL Image and then to ImageTk for Tkinter
    binarized_image_pil = Image.fromarray(combined_image)
    final_img = ImageTk.PhotoImage(binarized_image_pil)

    # Clear the canvas before displaying new image
    for widget in EditedImgCanvas.winfo_children():
        widget.destroy()

    # Display the image in the Tkinter canvas
    img_label = tk.Label(EditedImgCanvas, image=final_img)
    img_label.image = final_img  # Keep reference to avoid garbage collection
    img_label.pack()
