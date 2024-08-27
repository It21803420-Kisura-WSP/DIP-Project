import tkinter as tk
from src.gui.mainUI import createUI

def main():
    print("hallo")
    root = tk.Tk()

    screen_width = root.winfo_screenwidth() - 320
    screen_height = root.winfo_screenheight() - 160

    root.geometry(f"{screen_width}x{screen_height}")
    root.title("ABC Image Editor")

    createUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
 