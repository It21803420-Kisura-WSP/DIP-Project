import cv2
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

class PhotoEditor:
    def __init__(self, root):
        self.root = root
        self.root.title("Photo Manipulation Software")
        
        # Image display area
        self.image_label = tk.Label(root)
        self.image_label.pack()

        # Load Image button
        self.load_button = tk.Button(root, text="Load Image", command=self.load_image)
        self.load_button.pack(side=tk.LEFT)

        # Grayscale button
        self.grayscale_button = tk.Button(root, text="Grayscale", command=self.apply_grayscale)
        self.grayscale_button.pack(side=tk.LEFT)

        self.image = None
        self.cv_img = None

    def load_image(self):
        # Open file dialog to load an image
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp")])
        if file_path:
            self.cv_img = cv2.imread(file_path)
            self.display_image(self.cv_img)

    def display_image(self, img):
        # Convert OpenCV image to PIL format
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        pil_img = Image.fromarray(img_rgb)
        tk_img = ImageTk.PhotoImage(image=pil_img)

        # Display the image in the label
        self.image_label.config(image=tk_img)
        self.image_label.image = tk_img

    def apply_grayscale(self):
        if self.cv_img is not None:
            # Apply grayscale filter using OpenCV
            gray_img = cv2.cvtColor(self.cv_img, cv2.COLOR_BGR2GRAY)
            gray_img = cv2.cvtColor(gray_img, cv2.COLOR_GRAY2RGB)  # Convert back to 3 channels for display
            self.display_image(gray_img)

if __name__ == "__main__":
    root = tk.Tk()
    app = PhotoEditor(root)
    root.mainloop()
