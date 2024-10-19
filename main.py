import tkinter as tk
from src.gui.mainUI import createUI

def main():
    root = tk.Tk()

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    window_width = screen_width - 200 
    window_height = screen_height - 150 


    x = 100 
    y = 50


    root.geometry(f"{window_width}x{window_height}+{x}+{y}")
    root.title("Digital Image Manipulation App")

    createUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
