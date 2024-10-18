import tkinter as tk
from src.gui.bottomSecUI import *
from src.util.fileUtil import upload_image

from src.functions.advance_functions.image_filters.edge_detection import *
from src.functions.advance_functions.image_filters.embossing import *

f3 = None
EditedImgCanvas = None

btnF = '#0f1112'
btnB = '#b3e6e1'
btnA = '#d5e4eb'
primaryC = '#010d17'
borderC = 'white'

def createUI(root):
    root.configure(bg=primaryC)

    
    
    # Grid setup
    global f3
    f1 = tk.LabelFrame(root, bg=primaryC, bd=0)
    f2 = tk.LabelFrame(root, bg=primaryC, bd=0, highlightthickness=1, relief='solid', highlightbackground= borderC)
    f3 = tk.LabelFrame(root, bg=primaryC, bd=0, highlightthickness=1, relief='solid', highlightbackground= borderC)
    f4 = tk.LabelFrame(root, bg=primaryC, bd=0, highlightthickness=1, relief='solid', highlightbackground= borderC)

    # Allow frames to resize
    f1.grid_propagate(False)
    f2.grid_propagate(False)
    f3.grid_propagate(False)
    f4.grid_propagate(False)

    root.columnconfigure(0, weight=1)
    root.columnconfigure(1, weight=3)
    root.columnconfigure(2, weight=3)
    root.rowconfigure(0, weight=3)
    root.rowconfigure(1, weight=1)

    f1.grid(row=0, column=0, sticky='nsew', rowspan=2, padx=10, pady=10)
    f2.grid(row=0, column=1, sticky='nsew', padx=10, pady=10)
    f3.grid(row=0, column=2, sticky='nsew', padx=10, pady=10)
    f4.grid(row=1, column=1, sticky='nsew', columnspan=2, padx=10, pady=10)

    button_style = {
        'bg': btnB,
        'fg': btnF,
        'activebackground': btnA,
        'font': ('Arial', 8),
        'relief': 'flat',  # Use flat to avoid borders
        'borderwidth': 0,
        'highlightthickness': 0,
        'width': 20,
        'height': 2
    }

    # Main canvas setup
    mainCanvas = tk.Canvas(f2, bg=primaryC, height=600, width=600, highlightthickness=0)
    mainCanvas.grid(row=0, column=0, sticky='nsew')
    f2.grid_rowconfigure(0, weight=1)
    f2.grid_columnconfigure(0, weight=1)

    global EditedImgCanvas
    EditedImgCanvas = tk.Canvas(f3, bg=primaryC, height=600, width=600, highlightthickness=0)
    EditedImgCanvas.grid(row=0, column=0, sticky='nsew')
    f3.grid_rowconfigure(0, weight=1)
    f3.grid_columnconfigure(0, weight=1)

    # Set rows to weight to distribute space evenly
    for i in range(18):  # 18 rows for buttons and labels
        f1.grid_rowconfigure(i, weight=1)

    # Define a function for button placement with consistent padding
    def place_button(row, text, command):
        btn = tk.Button(f1, text=text, **button_style, command=command)
        btn.grid(row=row, column=0, sticky='ew', pady=5, padx=(10, 10))  # Add horizontal padding
        f1.grid_columnconfigure(0, weight=1)  # Make the column stretch

    uploadBtn = place_button(0, 'Upload an image', lambda: upload_image(mainCanvas))

    # Translation section
    l1 = tk.Label(f1, text="Translations", font=('Arial', 8),fg='white', bg=primaryC)
    l1.grid(row=1, column=0, sticky='nsew', pady=5)

    place_button(2, 'Rotate', lambda: rotView(f4))
    place_button(3, 'Flip', lambda: flipView(f4))
    place_button(4, 'Crop', lambda: cropView(f4))

    # Color Change section
    l2 = tk.Label(f1, text="Colors", font=('Arial', 8),fg='white', bg=primaryC)
    l2.grid(row=5, column=0, sticky='nsew', pady=5)

    place_button(6, 'Color Change', lambda: colorChangeView(f4))
    place_button(7, 'Tonal Adjustments', lambda: intensityManipulation(f4))
    place_button(8, 'Color Balance', lambda: colorCorrectionView(f4))

    # Filter section
    l3 = tk.Label(f1, text="Filters", font=('Arial', 8),fg='white', bg=primaryC)
    l3.grid(row=9, column=0, sticky='nsew', pady=5)

    place_button(10, 'Sharpening', lambda: sharpenFilter(f4))
    place_button(11, 'Smooth', lambda: smoothingFilter(f4))
    place_button(12, 'Edge Detection', lambda: edgeFilter(f4))
    place_button(13, 'Embossing', lambda: embFilter(f4))

    # Other section
    l4 = tk.Label(f1, text="Other", font=('Arial', 8),fg='white', bg=primaryC)
    l4.grid(row=14, column=0, sticky='nsew', pady=5)

    place_button(15, 'Image Segmentation', lambda: imgSegView(f4))
    place_button(16, 'Image Enhancement', lambda: imageEnhancements(f4))
    place_button(17, 'Style Transfer', lambda: styleTran(f4))

def get_f3():
    global f3
    return f3

def get_EditedImgCanvas():
    global EditedImgCanvas
    return EditedImgCanvas
