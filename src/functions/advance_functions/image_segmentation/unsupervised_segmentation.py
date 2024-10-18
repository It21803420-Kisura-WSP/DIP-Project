# un-supervised segmentation algorithms
from skimage.segmentation import slic, mark_boundaries, felzenszwalb
import tkinter as tk
from PIL import Image, ImageTk
import numpy as np
import matplotlib.pyplot as plt
from skimage.color import label2rgb
import cv2
from src.util.fileUtil import get_resized_image
import cv2 as cv
import numpy as np
import tkinter as tk
from PIL import Image, ImageTk
import matplotlib.pyplot as plt
from skimage.segmentation import felzenszwalb, mark_boundaries
from src.util.fileUtil import get_resized_image
import cv2 as cv
import numpy as np
import tkinter as tk
from PIL import Image, ImageTk
from skimage.segmentation import felzenszwalb, mark_boundaries
from src.util.fileUtil import get_resized_image


def felzenszwalbs(scale_slider, sigma_slider, min_size_slider):
    scale = scale_slider.get()
    sigma = sigma_slider.get()
    min_size = min_size_slider.get()

    from skimage.segmentation import felzenszwalb, mark_boundaries
    from src.gui.mainUI import get_EditedImgCanvas
    EditedImgCanvas = get_EditedImgCanvas()

    # Get the resized image
    resized_img = get_resized_image()
    if resized_img is None:
        print("No image loaded")
        return

    image_array = np.array(resized_img)

    # Getting values from sliders
    scale = scale_slider.get()
    sigma = sigma_slider.get()
    min_size = min_size_slider.get()

    image_segments = felzenszwalb(image_array, scale=scale, sigma=sigma, min_size=min_size)
    
    segmented_image_with_boundaries = mark_boundaries(image_array, image_segments)
    
    segmented_image_with_boundaries = (segmented_image_with_boundaries * 255).astype(np.uint8)
    
    segmented_image_rgb = cv.cvtColor(segmented_image_with_boundaries, cv.COLOR_BGR2RGB)
    
    final_img = ImageTk.PhotoImage(Image.fromarray(segmented_image_rgb))

    # Clear the canvas before displaying the new image
    for widget in EditedImgCanvas.winfo_children():
        widget.destroy()

    # Display the image in the Tkinter canvas
    img_label = tk.Label(EditedImgCanvas, image=final_img)
    img_label.image = final_img  
    img_label.pack()




def mark_boundaries_on_canvas(n_segments, compactness):
    from skimage.segmentation import slic, mark_boundaries
    from src.gui.mainUI import get_EditedImgCanvas

    EditedImgCanvas = get_EditedImgCanvas()

    # Get the resized image
    resized_img = get_resized_image()
    if resized_img is None:
        print("No image loaded")
        return

    # Convert image to a NumPy array for segmentation
    image_array = np.array(resized_img)

    # Apply SLIC segmentation with passed arguments
    image_segments = slic(image_array, n_segments=n_segments, compactness=compactness)

    # Mark the boundaries of the segmentation
    image_with_boundaries = mark_boundaries(image_array, image_segments)

    # Convert to uint8 format for Tkinter display
    image_with_boundaries = (image_with_boundaries * 255).astype(np.uint8)

    # Convert to RGB format for Pillow
    image_rgb = cv.cvtColor(image_with_boundaries, cv.COLOR_BGR2RGB)

    # Convert the image to a format compatible with Tkinter
    final_img = ImageTk.PhotoImage(Image.fromarray(image_rgb))

    # Clear the canvas before displaying the new image
    for widget in EditedImgCanvas.winfo_children():
        widget.destroy()

    # Display the image in the Tkinter canvas
    img_label = tk.Label(EditedImgCanvas, image=final_img)
    img_label.image = final_img  
    img_label.pack()
