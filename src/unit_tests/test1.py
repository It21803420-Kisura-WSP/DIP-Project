import tkinter as tk
from tkinter import filedialog
import numpy as np
from skimage import color
from skimage.filters import gaussian
from skimage.segmentation import active_contour
from PIL import Image, ImageTk
import matplotlib.pyplot as plt

# Global variable to store the uploaded image
uploaded_image = None

def clear_frame(frame):
    """Clear all widgets from the given frame."""
    for widget in frame.winfo_children():
        widget.destroy()

def upload_image():
    """Open a file dialog to select an image and update the global variable."""
    global uploaded_image
    file_path = filedialog.askopenfilename(title="Select an Image",
                                            filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.bmp")])
    if file_path:
        uploaded_image = Image.open(file_path).convert('RGB')
        print(f"Uploaded image: {file_path}")

def get_resized_image():
    """Return the uploaded image or create a sample image if none is uploaded."""
    global uploaded_image
    if uploaded_image is not None:
        # Resize the uploaded image if needed
        return uploaded_image.resize((200, 200), Image.ANTIALIAS)
    
    # For demonstration, create a sample image
    image = np.zeros((200, 200, 3), dtype=np.uint8)
    image[50:150, 50:150] = [255, 0, 0]  # Red square
    return Image.fromarray(image)

def imgSegView(f4):
    clear_frame(f4)

    l1 = tk.Label(f4, text="Active Contour Segmentation", font=('Arial', 12), bg='white')
    l1.grid(row=0, column=0, sticky='w', padx=20, pady=10)

    # Button to upload an image
    uploadBtn = tk.Button(f4, text="Upload Image", command=upload_image)
    uploadBtn.grid(row=1, column=0, sticky='w', padx=20, pady=10)

    # Slider for Iteration count
    iteration_scale = tk.Scale(f4, from_=1, to=100, label="Number of Iterations", orient='horizontal')
    iteration_scale.set(50)  # Default value
    iteration_scale.grid(row=2, column=0, sticky='w', padx=20)

    # Button to trigger Active Contour Segmentation
    acsBtn = tk.Button(f4, text="Run Active Contour Segmentation",
                       command=lambda: active_contour_segmentation(iteration_scale.get()))
    acsBtn.grid(row=3, column=0, sticky='w', padx=20, pady=20)

def active_contour_segmentation(iterations):
    """Perform active contour segmentation and display results."""
    # Get canvas to display the result
    EditedImgCanvas = get_EditedImgCanvas()

    resized_img = get_resized_image()
    if resized_img is None:
        print("No image loaded")
        return
    
    # Convert RGB image to grayscale
    gray_image = color.rgb2gray(np.array(resized_img))

    # Apply Gaussian filter for smoothing
    gray_image_noiseless = gaussian(gray_image, sigma=1)

    # Create an initial snake (circle)
    s = np.linspace(0, 2 * np.pi, 400)
    x = 100 + 80 * np.cos(s)
    y = 100 + 80 * np.sin(s)
    snake = np.array([x, y]).T

    # Perform active contour segmentation
    image_snake = active_contour(gray_image_noiseless, snake, alpha=0.01, beta=0.1, gamma=0.01, max_iterations=iterations)

    # Create a figure and axes using Matplotlib
    fig, ax = plt.subplots()
    ax.imshow(gray_image_noiseless, cmap='gray')
    ax.plot(snake[:, 0], snake[:, 1], '--r', lw=3, label='Initial Snake')
    ax.plot(image_snake[:, 0], image_snake[:, 1], '-b', lw=3, label='Active Contour')
    ax.legend()

    # Save the output figure
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

def get_EditedImgCanvas():
    """Create a canvas to display images. This should be customized for your GUI."""
    # For demonstration, we will create a new Tkinter window with a canvas
    window = tk.Tk()
    canvas = tk.Frame(window, width=400, height=400, bg='white')
    canvas.pack(fill=tk.BOTH, expand=True)
    return canvas

# Main application to test the Active Contour Segmentation
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Active Contour Segmentation")
    frame = tk.Frame(root)
    frame.pack()

    imgSegView(frame)
    root.mainloop()
