import tkinter as tk
from src.gui.mainUI import createUI

def main():
    root = tk.Tk()

    # Get screen width and height
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # Calculate window size based on required margins
    window_width = screen_width - 200  # 100px margin on both sides
    window_height = screen_height - 150  # 50px from above, 100px from below

    # Calculate the x and y coordinates to position the window
    x = 100  # 100px from the left
    y = 50   # 50px from the top

    # Set the geometry of the window (widthxheight+x+y)
    root.geometry(f"{window_width}x{window_height}+{x}+{y}")
    root.title("Image Maker Pro")

    createUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
