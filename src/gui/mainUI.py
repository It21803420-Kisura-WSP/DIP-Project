import tkinter as tk
from src.gui.bottomSecUI import *
from src.util.fileUtil import upload_image
from src.functions.advance_functions.image_filters.sharpening import image_sharpening
from src.functions.advance_functions.image_filters.smoothing import smoothing
from src.functions.advance_functions.image_filters.edge_detection import edge_detection

f3 = None
EditedImgCanvas = None

def createUI(root):

    # Grid setup
    global f3
    f1 = tk.LabelFrame(root)
    f2 = tk.LabelFrame(root)
    f3 = tk.LabelFrame(root)
    f4 = tk.LabelFrame(root)

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
    f2.grid(row=0, column=1, sticky='nsew', padx=10, pady=10, ipadx=0, ipady=0)
    f3.grid(row=0, column=2, sticky='nsew', padx=10, pady=10)
    f4.grid(row=1, column=1, sticky='nsew', columnspan=2, padx=10, pady=10)

    

    mainCanvas = tk.Canvas(f2, bg='white', height=600, width=600)
    mainCanvas.grid(row=0, column=0, sticky='nsew')
    f2.grid_rowconfigure(0, weight=1)
    f2.grid_columnconfigure(0, weight=1) 

    global EditedImgCanvas

    EditedImgCanvas = tk.Canvas(f3, bg='white', height=600, width=600)
    EditedImgCanvas.grid(row=0, column=0, sticky='nsew')
    f3.grid_rowconfigure(0, weight=1)
    f3.grid_columnconfigure(0, weight=1) 

    uploadBtn = tk.Button(f1, text='Upload an image', font=('Arial', 8), relief='flat', highlightthickness=0, command=lambda:upload_image(mainCanvas),height=2,width=25)
    uploadBtn.grid(row=0, column=0, sticky='n', pady=10,padx=10)
    f1.grid_rowconfigure(0, minsize=150)


    #Translation section ------------------------

    l1 = tk.Label(f1, text="Translations", font=('Arial', 8), width=30, height=2,fg ='#063361')
    l1.grid(row=1, column=0, sticky='n')
    f1.grid_rowconfigure(1, minsize=50)

    RotateBtn = tk.Button(f1, text='Rotate', font=('Arial', 8), relief='flat', highlightthickness=1, borderwidth=1, width=10, height=1,command=lambda: rotView(f4))
    RotateBtn.grid(row=2, column=0, sticky='n')
    f1.grid_rowconfigure(2, minsize=20)

    flipBtn = tk.Button(f1, text='Flip', font=('Arial', 8), relief='flat', highlightthickness=1, borderwidth=1, width=10, height=1,command=lambda:flipView(f4))
    flipBtn.grid(row=3, column=0, sticky='n')
    f1.grid_rowconfigure(3, minsize=20)

    cropBtn = tk.Button(f1, text='Crop', font=('Arial', 8), relief='flat', highlightthickness=1, borderwidth=1, width=10, height=1,command=lambda:cropView(f4))
    cropBtn.grid(row=4, column=0, sticky='n')
    f1.grid_rowconfigure(4, minsize=20)

    #Color Change section ------------------------

    l2 = tk.Label(f1, text="Colors", font=('Arial', 8), width=30, height=2,fg='#063361')
    l2.grid(row=5, column=0, sticky='n',pady=(2,10))
    f1.grid_rowconfigure(4, minsize=50)


    colorChangeBtn = tk.Button(f1, text='Color Change', font=('Arial', 8), relief='flat', highlightthickness=1, borderwidth=1, width=10, height=1,command=lambda:colorChangeView(f4))
    colorChangeBtn.grid(row=6, column=0, sticky='n')
    f1.grid_rowconfigure(6, minsize=20)

    tonalBtn = tk.Button(f1, text='Tonal Adjustments', font=('Arial', 8), relief='flat', highlightthickness=1, borderwidth=1, width=20, height=1,command=lambda:intensityManipulation(f4))
    tonalBtn.grid(row=7, column=0, sticky='n')
    f1.grid_rowconfigure(7, minsize=20)

    colorBalBtn = tk.Button(f1, text='Color Balance', font=('Arial', 8), relief='flat', highlightthickness=1, borderwidth=1, width=10, height=1)
    colorBalBtn.grid(row=8, column=0, sticky='n')
    f1.grid_rowconfigure(8, minsize=20)

    #Filter section ------------------------

    l3 = tk.Label(f1, text="Filters", font=('Arial', 8), width=30, height=2,fg='#063361')
    l3.grid(row=9, column=0, sticky='n',pady=(10,2))
    f1.grid_rowconfigure(9, minsize=50)


    sharpFilterBtn = tk.Button(f1, text='Sharpening', font=('Arial', 8), relief='flat', highlightthickness=1, borderwidth=1, width=10, height=1,command=lambda:image_sharpening())
    sharpFilterBtn.grid(row=10, column=0, sticky='n')
    f1.grid_rowconfigure(10, minsize=20)

    smoothFilterBtn = tk.Button(f1, text='Smooth', font=('Arial', 8), relief='flat', highlightthickness=1, borderwidth=1, width=20, height=1,command=lambda:smoothing())
    smoothFilterBtn.grid(row=11, column=0, sticky='n')
    f1.grid_rowconfigure(11, minsize=20)

    EdgeFilterBtn = tk.Button(f1, text='Edge Detection', font=('Arial', 8), relief='flat', highlightthickness=1, borderwidth=1, width=20, height=1,command=lambda:edge_detection())
    EdgeFilterBtn.grid(row=12, column=0, sticky='n')
    f1.grid_rowconfigure(12, minsize=20)

    #Other section ------------------------

    l4 = tk.Label(f1, text="Other", font=('Arial', 8), width=30, height=2,fg='#063361')
    l4.grid(row=13, column=0, sticky='n',pady=(10,2))
    f1.grid_rowconfigure(13, minsize=50)


    imgSegmentBtn = tk.Button(f1, text='Image Segmentation', font=('Arial', 8), relief='flat', highlightthickness=1, borderwidth=1, width=20, height=1,command=lambda:imgSegView(f4))
    imgSegmentBtn.grid(row=14, column=0, sticky='n')
    f1.grid_rowconfigure(14, minsize=20)

    imgEnhanceBtn = tk.Button(f1, text='Image Enhancement', font=('Arial', 8), relief='flat', highlightthickness=1, borderwidth=1, width=20, height=1)
    imgEnhanceBtn.grid(row=15, column=0, sticky='n')
    f1.grid_rowconfigure(15, minsize=20)

    styleTranBtn = tk.Button(f1, text='Style Transfer', font=('Arial', 8), relief='flat', highlightthickness=1, borderwidth=1, width=20, height=1)
    styleTranBtn.grid(row=16, column=0, sticky='n')
    f1.grid_rowconfigure(16, minsize=20)

def get_f3():
    global f3
    return f3

def get_EditedImgCanvas():
    global EditedImgCanvas
    return EditedImgCanvas
