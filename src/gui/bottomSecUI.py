import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import cv2 as cv
from tkinter import messagebox
from src.functions.basic_functions.rotate import rotate
from src.functions.advance_functions.image_segmentation.supervised_segmentation import active_contour
# Destroy all widgets in the frame
def clear_frame4(frame):
    for widget in frame.winfo_children():
        widget.destroy()
 
def rotView(f4):
    clear_frame4(f4)

    rotate_option = tk.StringVar(value="Clockwise")

    def display_selected():
        print("Selected option:", rotate_option.get())

    radio1 = tk.Radiobutton(f4, text="Clockwise", variable=rotate_option, value="Clockwise", command=display_selected)
    radio1.grid(row=0, column=0, sticky='w',padx=20,pady=20)
    f4.grid_rowconfigure(0,minsize=10)

    radio2 = tk.Radiobutton(f4, text="Counter Clockwise", variable=rotate_option, value="Counter Clockwise", command=display_selected)
    radio2.grid(row=1, column=0, sticky='w',padx=20,pady=10)
    f4.grid_rowconfigure(1, minsize=20)

    Deg90btn = tk.Button(f4, text='90°', font=('Arial', 8), relief='flat', highlightthickness=1, borderwidth=1, padx=20,pady=10,command=lambda:rotate())
    Deg90btn.grid(row=0, column=1, sticky='w',padx=20,pady=20)
    f4.grid_columnconfigure(1, minsize=20)

    Deg180btn = tk.Button(f4, text='180°', font=('Arial', 8), relief='flat', highlightthickness=1, borderwidth=1, padx=20,pady=10)
    Deg180btn.grid(row=0, column=2, sticky='w',padx=20,pady=20)
    f4.grid_columnconfigure(2, minsize=20)

    Deg270btn = tk.Button(f4, text='270°', font=('Arial', 8), relief='flat', highlightthickness=1, borderwidth=1, padx=20,pady=10)
    Deg270btn.grid(row=0, column=3, sticky='w',padx=20,pady=20)
    f4.grid_columnconfigure(3, minsize=20)

    Deg360btn = tk.Button(f4, text='360°', font=('Arial', 8), relief='flat', highlightthickness=1, borderwidth=1, padx=20,pady=10)
    Deg360btn.grid(row=0, column=4, sticky='w',padx=20,pady=20)
    f4.grid_columnconfigure(4, minsize=20)

def flipView(f4):
    clear_frame4(f4)

    verticalFlipbtn = tk.Button(f4, text='Vertical Flip', font=('Arial', 8), relief='flat', highlightthickness=1, borderwidth=1, padx=20,pady=10)
    verticalFlipbtn.grid(row=0, column=5, sticky='w',padx=20,pady=20)
    f4.grid_columnconfigure(5, minsize=20)

    horizontalFlipbtn = tk.Button(f4, text='Horizontal Flip', font=('Arial', 8), relief='flat', highlightthickness=1, borderwidth=1, padx=20,pady=10)
    horizontalFlipbtn.grid(row=0, column=6, sticky='w',padx=20,pady=20)
    f4.grid_columnconfigure(6, minsize=20)

def cropView(f4):
    clear_frame4(f4)

    def get_numbers():
        try:
            num1 = float(entry1.get())
            num2 = float(entry2.get())
            num3 = float(entry3.get())
            num4 = float(entry4.get())

            messagebox.showinfo("Numbers Entered", f"You entered: {num1}, {num2}, {num3}, {num4}")
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter valid numbers in all fields.")

    l1 = tk.Label(f4, text="Starting Point(X)", font=('Arial', 8), width=30, height=2,fg ='#063361')
    l1.grid(row=1, column=0, sticky='w')
    f4.grid_columnconfigure(0, minsize=50)

    entry1 = tk.Entry(f4)
    entry1.grid(row=0, column=0, sticky='w',padx=20,pady=20)
    f4.grid_columnconfigure(0, minsize=20)

    l2 = tk.Label(f4, text="End Point(X)", font=('Arial', 8), width=30, height=2,fg ='#063361')
    l2.grid(row=1, column=1, sticky='w')
    f4.grid_columnconfigure(1, minsize=50)

    entry2 = tk.Entry(f4)
    entry2.grid(row=0, column=1, sticky='w',padx=20,pady=20)
    f4.grid_columnconfigure(1, minsize=20)

    l3 = tk.Label(f4, text="Starting Point(Y)", font=('Arial', 8), width=30, height=2,fg ='#063361')
    l3.grid(row=1, column=2, sticky='w')
    f4.grid_columnconfigure(2, minsize=50)
    
    entry3 = tk.Entry(f4)
    entry3.grid(row=0, column=2, sticky='w',padx=20,pady=20)
    f4.grid_columnconfigure(2, minsize=20)

    l4 = tk.Label(f4, text="End Point(Y)", font=('Arial', 8), width=30, height=2,fg ='#063361')
    l4.grid(row=1, column=3, sticky='w')
    f4.grid_columnconfigure(3, minsize=50)

    entry4 = tk.Entry(f4)
    entry4.grid(row=0, column=3, sticky='w',padx=20,pady=20)
    f4.grid_columnconfigure(3, minsize=20)

    submitbtn = tk.Button(f4, text="Crop", command=get_numbers)
    submitbtn.grid(row=0, column=4, sticky='w',padx=20,pady=20)
    f4.grid_columnconfigure(4, minsize=20)


def colorChangeView(f4):
    clear_frame4(f4)

    colorBtn = tk.Button(f4, text="Color", )
    colorBtn.grid(row=0, column=0, sticky='w',padx=20,pady=20)
    f4.grid_columnconfigure(0, minsize=20)

    grayBtn = tk.Button(f4, text="Gray Scale")
    grayBtn.grid(row=0, column=1, sticky='w',padx=20,pady=20)
    f4.grid_columnconfigure(1, minsize=20)

    bwBtn = tk.Button(f4, text="BW")
    bwBtn.grid(row=0, column=2, sticky='w',padx=20,pady=20)
    f4.grid_columnconfigure(2, minsize=20)


# def tonalAdjView(f4):
#     clear_frame4(f4)


def imgSegView(f4):
    clear_frame4(f4)

    l1 = tk.Label(f4, text="Supervised Segmentation", font=('Arial', 8), width=60, height=2,fg ='#063361')
    l1.grid(row=0, column=0, sticky='w')
    f4.grid_columnconfigure(0, minsize=50)

    l2 = tk.Label(f4, text="Unsupervised Segmentation", font=('Arial', 8), width=60, height=2,fg ='#063361')
    l2.grid(row=0, column=1, sticky='w',padx=50)
    f4.grid_columnconfigure(1, minsize=50)

    acsBtn = tk.Button(f4, text="Active Contour Segmentation", command=lambda:active_contour())
    acsBtn.grid(row=1, column=0, sticky='w',padx=20,pady=20)
    f4.grid_rowconfigure(1, minsize=20)

    cvsBtn = tk.Button(f4, text="Chan vese Segmentation", )
    cvsBtn.grid(row=2, column=0, sticky='w',padx=20,pady=20)
    f4.grid_rowconfigure(2, minsize=20)

    sbtmiBtn = tk.Button(f4, text="Segmentation By Threshold manual input", )
    sbtmiBtn.grid(row=1, column=0, sticky='w',padx=200,pady=20)
    f4.grid_rowconfigure(1, minsize=20)

    sbtusmBtn = tk.Button(f4, text="Segmentation By Threshold using skimagefilter module" )
    sbtusmBtn.grid(row=2, column=0, sticky='w',padx=200,pady=20)
    f4.grid_columnconfigure(2, minsize=20)

    fsBtn = tk.Button(f4, text="Felzenszwalbs Segmentation" )
    fsBtn.grid(row=1, column=1, sticky='w',padx=20,pady=20)
    f4.grid_columnconfigure(1, minsize=20)

    mbBtn = tk.Button(f4, text="Mark Boundaries" )
    mbBtn.grid(row=1, column=1, sticky='w',padx=200,pady=20)
    f4.grid_columnconfigure(1, minsize=20)

    slicBtn = tk.Button(f4, text="Simple Linear Iterative Clustering" )
    slicBtn.grid(row=2, column=1, sticky='w',padx=20,pady=20)
    f4.grid_columnconfigure(0, minsize=20)









    
