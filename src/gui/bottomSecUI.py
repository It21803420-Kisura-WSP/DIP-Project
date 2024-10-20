import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import cv2 as cv
from tkinter import messagebox
from src.functions.basic_functions.rotate import *
from src.functions.advance_functions.image_segmentation.supervised_segmentation import *
from src.functions.advance_functions.intensity_manipulation_by_color_transformation_alogrithms.brightness_enhancement import *
from src.functions.basic_functions.flip import *
from src.functions.basic_functions.crop import *
from src.functions.basic_functions.color_change import *
from src.functions.advance_functions.image_segmentation.unsupervised_segmentation import *
from src.functions.advance_functions.intensity_manipulation_by_color_transformation_alogrithms.color_balance import *
from src.functions.deep_learning_algorithms.image_enhancement import *
from src.functions.deep_learning_algorithms.style_transfer import *
from src.images import *
from src.functions.advance_functions.intensity_manipulation_by_color_transformation_alogrithms.contrast_enhancement import *
from src.functions.advance_functions.intensity_manipulation_by_color_transformation_alogrithms.gamma_correction import *
from src.functions.advance_functions.image_filters.embossing import *
from src.functions.advance_functions.image_filters.edge_detection import *
from src.functions.advance_functions.image_filters.sharpening import *
from src.functions.advance_functions.image_filters.smoothing import *

btnF = '#0f1112'
btnB = '#b3e6e1'
btnA = '#d5e4eb'
primaryC = '#010d17'
borderC = 'white'

slider_style = {
    'bg': primaryC,
    'fg': borderC,
    'highlightthickness': 0,
    'bd': 0,
    'font': ('Arial', 8),
    'length': 150, 
    'width': 10     
}

button_style = {
        'bg': btnB,
        'fg': btnF,
        'activebackground': btnA,
        'font': ('Arial', 8),
        'relief': 'flat', 
        'borderwidth': 0,
        'highlightthickness': 0,
        'width': 15,
        'height': 2
    }
radio_button_style = {
    'bg': btnB,                
    'fg': btnF,                
    'activebackground': btnA,  
    'font': ('Arial', 8),      
    'indicatoron': 1,          
    'highlightthickness': 0,   
    'borderwidth': 0,          
    'width': 15,               
    'height': 2                
}


def clear_frame4(frame):
    for widget in frame.winfo_children():
        widget.destroy()
 
def rotView(f4):
    clear_frame4(f4)

    rotate_option = tk.StringVar(value="Clockwise")

    def display_selected():
        print("Selected option:", rotate_option.get())

    def perform_rotation(degrees):
        if rotate_option.get() == "Clockwise":
            if degrees == 90:
                rotate_90_cw()
            elif degrees == 180:
                rotate_180_cw()
            elif degrees == 270:
                rotate_270_cw()
            elif degrees == 360:
                rotate_360_cw()
        else:  
            if degrees == 90:
                rotate_90_ccw()
            elif degrees == 180:
                rotate_180_ccw()
            elif degrees == 270:
                rotate_270_ccw()
            elif degrees == 360:
                rotate_360_ccw()

    radio1 = tk.Radiobutton(f4, text="Clockwise", variable=rotate_option, value="Clockwise", command=display_selected,**radio_button_style)
    radio1.grid(row=0, column=0, sticky='w',padx=20,pady=20)
    f4.grid_rowconfigure(0,minsize=10)

    radio2 = tk.Radiobutton(f4, text="Counter Clockwise", variable=rotate_option, value="Counter Clockwise", command=display_selected,**radio_button_style)
    radio2.grid(row=1, column=0, sticky='w',padx=20,pady=10)
    f4.grid_rowconfigure(1, minsize=20)

    Deg90btn = tk.Button(f4, text='90°',**button_style, padx=20,pady=10,command=lambda:perform_rotation(90))
    Deg90btn.grid(row=0, column=1, sticky='w',padx=20,pady=20)
    f4.grid_columnconfigure(1, minsize=20)

    Deg180btn = tk.Button(f4, text='180°',**button_style, padx=20,pady=10,command=lambda:perform_rotation(180))
    Deg180btn.grid(row=0, column=2, sticky='w',padx=20,pady=20)
    f4.grid_columnconfigure(2, minsize=20)

    Deg270btn = tk.Button(f4, text='270°',**button_style, padx=20,pady=10,command=lambda:perform_rotation(270))
    Deg270btn.grid(row=0, column=3, sticky='w',padx=20,pady=20)
    f4.grid_columnconfigure(3, minsize=20)

    Deg360btn = tk.Button(f4, text='360°',**button_style, padx=20,pady=10,command=lambda:perform_rotation(360))
    Deg360btn.grid(row=0, column=4, sticky='w',padx=20,pady=20)
    f4.grid_columnconfigure(4, minsize=20)

def flipView(f4):
    clear_frame4(f4)

    verticalFlipbtn = tk.Button(f4, text='Vertical Flip',**button_style, padx=20,pady=10,command=lambda:vertical_flip())
    verticalFlipbtn.grid(row=0, column=5, sticky='w',padx=20,pady=20)
    f4.grid_columnconfigure(5, minsize=20)

    horizontalFlipbtn = tk.Button(f4, text='Horizontal Flip', **button_style, padx=20,pady=10,command=lambda:horizontal_flip())
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

            
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter valid numbers in all fields.")

        crop(num1,num2,num3,num4)

    l1 = tk.Label(f4, text="Starting Point(X)", font=('Arial', 8), width=30, height=2,fg = borderC,bg=primaryC)
    l1.grid(row=1, column=0, sticky='w')
    f4.grid_columnconfigure(0, minsize=50)

    entry1 = tk.Entry(f4)
    entry1.grid(row=0, column=0, sticky='w',padx=20,pady=20)
    f4.grid_columnconfigure(0, minsize=20)

    l2 = tk.Label(f4, text="End Point(X)", font=('Arial', 8), width=30, height=2,fg = borderC,bg=primaryC)
    l2.grid(row=1, column=1, sticky='w')
    f4.grid_columnconfigure(1, minsize=50)

    entry2 = tk.Entry(f4)
    entry2.grid(row=0, column=1, sticky='w',padx=20,pady=20)
    f4.grid_columnconfigure(1, minsize=20)

    l3 = tk.Label(f4, text="Starting Point(Y)", font=('Arial', 8), width=30, height=2,fg = borderC,bg=primaryC)
    l3.grid(row=1, column=2, sticky='w')
    f4.grid_columnconfigure(2, minsize=50)
    
    entry3 = tk.Entry(f4)
    entry3.grid(row=0, column=2, sticky='w',padx=20,pady=20)
    f4.grid_columnconfigure(2, minsize=20)

    l4 = tk.Label(f4, text="End Point(Y)", font=('Arial', 8), width=30, height=2,fg = borderC,bg=primaryC)
    l4.grid(row=1, column=3, sticky='w')
    f4.grid_columnconfigure(3, minsize=50)

    entry4 = tk.Entry(f4)
    entry4.grid(row=0, column=3, sticky='w',padx=20,pady=20)
    f4.grid_columnconfigure(3, minsize=20)

    submitbtn = tk.Button(f4, text="Crop", command=lambda:get_numbers(),**button_style)
    submitbtn.grid(row=0, column=4, sticky='w',padx=20,pady=20)
    f4.grid_columnconfigure(4, minsize=20)

def on_gray_intensity_change(val):
    convert_image_to_grayscale(val)

def on_bw_intensity_change(val):
    convert_image_to_bw(val)

def colorChangeView(f4):
    print("colorChangeView called")  
    clear_frame4(f4)

    
    colorBtn = tk.Button(f4, text="Color", command=lambda: convert_image_to_color(), **button_style)
    colorBtn.grid(row=0, column=0, sticky='w', padx=50, pady=50)

    
    gray_slider = tk.Scale(f4, from_=0, to=100, orient=tk.HORIZONTAL, label="Gray Intensity")
    gray_slider.set(0)
    gray_slider.grid(row=0, column=1, padx=50, pady=50)
    gray_slider.config(**slider_style, command=on_gray_intensity_change)

    
    bw_slider = tk.Scale(f4, from_=0, to=255, orient=tk.HORIZONTAL, label="BW Intensity")
    bw_slider.set(0)  
    bw_slider.grid(row=0, column=2, padx=50, pady=50)
    bw_slider.config(**slider_style, command=on_bw_intensity_change)

    
    f4.grid_columnconfigure(0, minsize=100)
    f4.grid_columnconfigure(1, minsize=150)
    f4.grid_columnconfigure(2, minsize=150)



def imgSegView(f4):
    clear_frame4(f4)  

    # ------------------ Chan ------------------
    frame_chan = tk.Frame(f4, bd=0, highlightbackground='white', highlightcolor='white', highlightthickness=0)
    frame_chan.grid(row=0, column=0, padx=(50, 50), pady=10)
    frame_chan.config(bg=primaryC)


    l1 = tk.Label(frame_chan, text="Chan-Vese Segmentation", font=('Arial', 8), width=30, height=2, bg=primaryC, fg=borderC)
    l1.grid(row=0, column=0, columnspan=2, sticky='w', padx=5, pady=(5, 10)) 

    iteration_slider = tk.Scale(frame_chan, from_=1, to=250, orient='horizontal', label='Max Iterations',bg=primaryC, fg=borderC)
    iteration_slider.set(0)  
    iteration_slider.grid(row=1, column=0, sticky='ew', padx=5, pady=(0, 5))
   

    cvsBtn = tk.Button(frame_chan, text="Apply", **button_style, 
                       command=lambda: chan_vese_segmentation(iteration_slider.get()))
    cvsBtn.grid(row=2, column=0, columnspan=2, sticky='ew', padx=5, pady=(0, 10))

    # ------------------ Ski ------------------
    frame_ski = tk.Frame(f4, bd=1, highlightbackground='white', highlightcolor='white', highlightthickness=0)
    frame_ski.grid(row=0, column=1, padx=(50, 50), pady=10)
    frame_ski.config(bg=primaryC)

    l2 = tk.Label(frame_ski, text="Threshold using skiimage", font=('Arial', 8), width=30, height=2, bg=primaryC, fg=borderC)
    l2.grid(row=0, column=0, columnspan=2, sticky='w', padx=5, pady=(5, 10))

    
    otsu_slider = tk.Scale(frame_ski, from_=0, to=255, resolution=1, label="Otsu Threshold", 
                        orient=tk.HORIZONTAL, bg=primaryC, fg=borderC)  
    otsu_slider.set(0)  
    otsu_slider.grid(row=1, column=0, sticky='ew', padx=5, pady=(0, 5))

   
    niblack_slider = tk.Scale(frame_ski, from_=0, to=255, resolution=1, label="Niblack Threshold", 
                            orient=tk.HORIZONTAL, bg=primaryC, fg=borderC)  
    niblack_slider.set(0)  
    niblack_slider.grid(row=1, column=1, sticky='ew', padx=5, pady=(0, 5))

    
    sauvola_slider = tk.Scale(frame_ski, from_=0, to=255, resolution=1, label="Sauvola Threshold", 
                            orient=tk.HORIZONTAL, bg=primaryC, fg=borderC) 
    sauvola_slider.set(0) 
    sauvola_slider.grid(row=2, column=0, sticky='ew', padx=5, pady=(0, 5))

    
    apply_button = tk.Button(frame_ski, text="Apply", **button_style,
                            command=lambda: threshold_using_skiimage_filter(otsu_slider.get(), niblack_slider.get(), sauvola_slider.get()))
    apply_button.grid(row=2, column=1, sticky='ew', padx=5, pady=(0, 10))


    # ------------------ Felzen ------------------
    frame_felzen = tk.Frame(f4, bd=1, highlightbackground='white', highlightcolor='white', highlightthickness=0)
    frame_felzen.grid(row=0, column=2, padx=(50, 50), pady=10)
    frame_felzen.config(bg=primaryC)  

    l3 = tk.Label(frame_felzen, text="Felzenszwalbs Segmentation", font=('Arial', 8), width=30, height=2, 
                bg=primaryC, fg=borderC)  
    l3.grid(row=0, column=0, columnspan=2, sticky='w', padx=5, pady=(5, 10))

    
    scale_slider = tk.Scale(frame_felzen, from_=1, to=100, resolution=1, label="Scale", 
                            orient=tk.HORIZONTAL, bg=primaryC, fg=borderC)  
    scale_slider.set(0)  
    scale_slider.grid(row=1, column=0, sticky='ew', padx=5, pady=(0, 5))

    
    sigma_slider = tk.Scale(frame_felzen, from_=0.1, to=10.0, resolution=0.1, label="Sigma", 
                            orient=tk.HORIZONTAL, bg=primaryC, fg=borderC)  
    sigma_slider.set(5.0)  
    sigma_slider.grid(row=1, column=1, sticky='ew', padx=5, pady=(0, 5))

    
    min_size_slider = tk.Scale(frame_felzen, from_=1, to=500, resolution=1, label="Min Size", 
                            orient=tk.HORIZONTAL, bg=primaryC, fg=borderC)  
    min_size_slider.set(100)  
    min_size_slider.grid(row=2, column=0, sticky='ew', padx=5, pady=(0, 5))

    
    fsBtn = tk.Button(frame_felzen, text="Apply",
                    command=lambda: felzenszwalbs(scale_slider, sigma_slider, min_size_slider), **button_style)
    fsBtn.grid(row=2, column=1, sticky='ew', padx=5, pady=(0, 10))


    # ------------------ Mark ------------------
    frame_mark = tk.Frame(f4, bd=1, highlightbackground='white', highlightcolor='white', highlightthickness=0)
    frame_mark.grid(row=0, column=3, padx=(50, 50), pady=10)
    frame_mark.config(bg=primaryC)  

    l4 = tk.Label(frame_mark, text="Mark Boundaries", font=('Arial', 8), width=30, height=2, 
                bg=primaryC, fg=borderC)  
    l4.grid(row=0, column=0, columnspan=2, sticky='w', padx=5, pady=(5, 10))

    
    n_segments_slider = tk.Scale(frame_mark, from_=10, to=500, resolution=1, label="Number of Segments", 
                                orient=tk.HORIZONTAL, bg=primaryC, fg=borderC) 
    n_segments_slider.set(100)  
    n_segments_slider.grid(row=1, column=0, sticky='ew', padx=5, pady=(0, 5))

    
    compactness_slider = tk.Scale(frame_mark, from_=0.1, to=10.0, resolution=0.1, label="Compactness", 
                                orient=tk.HORIZONTAL, bg=primaryC, fg=borderC)  
    compactness_slider.set(1.0)  
    compactness_slider.grid(row=1, column=1, sticky='ew', padx=5, pady=(0, 5))

    
    mbBtn = tk.Button(frame_mark, text="Apply",
                    command=lambda: mark_boundaries_on_canvas(n_segments_slider.get(), compactness_slider.get()), **button_style)
    mbBtn.grid(row=2, column=0, columnspan=2, sticky='ew', padx=5, pady=(0, 10))

# ---------------------------------get values

def on_brightness_change(val):

    brightness_value = float(val)
    enhance_brightness(brightness_value)

def on_contrast_change(val):

    contrast_value = float(val)
    enhance_contrast(contrast_value)

def on_gamma_change(val):

    gamma_value = float(val)
    apply_gamma_correction(gamma_value)

# --------------intensity Manipulation -------

def intensityManipulation(f4):
    clear_frame4(f4)

    
    f4.grid_columnconfigure(0, weight=1)
    f4.grid_columnconfigure(1, weight=1)
    f4.grid_columnconfigure(2, weight=1)

    # ----------- Brightness Slider -----------
    brightness_slider = tk.Scale(f4, from_=0, to=3.0, orient=tk.HORIZONTAL, resolution=0.1, label="Brightness")
    brightness_slider.set(0)
    brightness_slider.grid(row=0, column=0, padx=50, pady=50, sticky='nsew')
    brightness_slider.config(command=on_brightness_change, **slider_style)

    # ----------- Contrast Slider -----------
    contrast_slider = tk.Scale(f4, from_=0, to=3.0, orient=tk.HORIZONTAL, resolution=0.1, label="Contrast")
    contrast_slider.set(0)
    contrast_slider.grid(row=0, column=1, padx=50, pady=50, sticky='nsew')
    contrast_slider.config(command=on_contrast_change, **slider_style)

    # ----------- Gamma Slider -----------
    gamma_slider = tk.Scale(f4, from_=0, to=3.0, orient=tk.HORIZONTAL, resolution=0.1, label="Gamma")
    gamma_slider.set(0)  # Set default gamma value
    gamma_slider.grid(row=0, column=2, padx=50, pady=50, sticky='nsew')
    gamma_slider.config(command=on_gamma_change, **slider_style)

    
    for i in range(3):
        f4.grid_columnconfigure(i, weight=0)  

# -----------------------------------------

def colorCorrectionView(f4):
    clear_frame4(f4)

    
    resized_img = get_resized_image()
    if resized_img is None:
        print("No image loaded")
        return

    
    img_array = np.array(resized_img)

    
    hsv_img = cv2.cvtColor(img_array, cv2.COLOR_RGB2HSV)
    h, s, v = cv2.split(hsv_img)
    
    
    hue_var = tk.DoubleVar(value=0) 
    saturation_var = tk.DoubleVar(value=1)  
    value_var = tk.DoubleVar(value=1)  

    def get_correction_values():
        hue = hue_var.get()
        saturation = saturation_var.get()
        value = value_var.get()
        color_correction(hue, saturation, value)

    
    l_hue = tk.Label(f4, text="Hue Adjustment (-180 to 180)", font=('Arial', 8), fg=borderC, bg=primaryC)
    l_hue.grid(row=1, column=0, sticky='w', padx=(10, 5))
    hue_slider = tk.Scale(f4, from_=-180, to=180, orient='horizontal', variable=hue_var)
    hue_slider.grid(row=1, column=1, sticky='w', padx=(0, 10))
    hue_slider.config(**slider_style)

    
    l_saturation = tk.Label(f4, text="Saturation Adjustment (0-3)", font=('Arial', 8), fg=borderC, bg=primaryC)
    l_saturation.grid(row=1, column=2, sticky='w', padx=(10, 5))
    saturation_slider = tk.Scale(f4, from_=0, to=3, orient='horizontal', resolution=0.1, variable=saturation_var)
    saturation_slider.grid(row=1, column=3, sticky='w', padx=(0, 10))
    saturation_slider.config(**slider_style)

    
    l_value = tk.Label(f4, text="Brightness Adjustment (0-3)", font=('Arial', 8), fg=borderC, bg=primaryC)
    l_value.grid(row=1, column=4, sticky='w', padx=(10, 5))
    value_slider = tk.Scale(f4, from_=0, to=3, orient='horizontal', resolution=0.1, variable=value_var)
    value_slider.grid(row=1, column=5, sticky='w', padx=(0, 10))
    value_slider.config(**slider_style)

    
    submit_btn = tk.Button(f4, text="Apply", command=get_correction_values, **button_style)
    submit_btn.grid(row=1, column=6, columnspan=6, sticky='w', padx=20, pady=20)


def on_noise_intensity_change(val):
    reducing_noise(int(float(val)))

def on_color_noise_intensity_change(val):
    reducing_noise_colored(int(float(val)))

def on_sharpening_intensity_change(val):
    sharpening_image(int(float(val)))


def styleTran(f4):
    clear_frame4(f4)

    monalisa = r"src\images\Styles\Mona_Lisa.jpg"
    starrynight = r"src\images\Styles\Starry_Night.jpg"
    scream = r"src\images\Styles\The_Scream.jpg"
    anime = r"src\images\Styles\anime.jpg"

    
    intensity_scale = tk.Scale(f4, from_=0, to=1, resolution=0.01, orient=tk.HORIZONTAL, label="Style Intensity",**slider_style)
    intensity_scale.set(0)  
    intensity_scale.grid(row=0, column=0, columnspan=4, padx=50, pady=5) 

    
    Style1 = tk.Button(f4, text="Mona Lisa", command=lambda: using_google_arbitary_image_stylization_model(monalisa, intensity_scale.get()),**button_style)
    Style1.grid(row=1, column=0, padx=50, pady=50)

    style2 = tk.Button(f4, text="Starry Night", command=lambda: using_google_arbitary_image_stylization_model(starrynight, intensity_scale.get()),**button_style)
    style2.grid(row=1, column=1, padx=50, pady=50)

    style3 = tk.Button(f4, text="Scream", command=lambda: using_google_arbitary_image_stylization_model(scream, intensity_scale.get()),**button_style)
    style3.grid(row=1, column=2, padx=50, pady=50)

    
    style4 = tk.Button(f4, text="Anime", command=lambda: using_google_arbitary_image_stylization_model(anime, intensity_scale.get()),**button_style)
    style4.grid(row=1, column=3, padx=50, pady=50)



def on_filter_intensity_change(val):

    apply_emboss_filter(val)

def embFilter(f4):
    clear_frame4(f4)

    
    f4.grid_columnconfigure(0, weight=0) 

    # ----------- Emboss Filter Intensity Slider -----------
    intensity_slider = tk.Scale(
        f4,
        from_=0,
        to=5.0,
        orient=tk.HORIZONTAL,
        resolution=0.1,
        label="Emboss Filter Intensity"
    )
    intensity_slider.set(0)
    intensity_slider.grid(row=0, column=0, padx=50, pady=50, sticky='ew')  
    intensity_slider.config(command=on_filter_intensity_change, **slider_style)

    
    f4.grid_rowconfigure(0, weight=0)  



def on_edge_threshold_change(val):
    low_threshold = low_slider.get()
    upper_threshold = upper_slider.get()
    apply_edge_detection(low_threshold, upper_threshold)

def edgeFilter(f4):
    clear_frame4(f4)

    global low_slider, upper_slider

    
    f4.grid_columnconfigure(0, weight=0)  

    # ----------- Low Threshold Slider -----------
    low_slider = tk.Scale(
        f4,
        from_=0,
        to=255,
        orient=tk.HORIZONTAL,
        resolution=1,
        label="Low Threshold"
    )
    low_slider.set(0)
    low_slider.grid(row=0, column=0, padx=50, pady=10, sticky='ew')  
    low_slider.config(**slider_style)
    low_slider.config(command=on_edge_threshold_change)

    # ----------- Upper Threshold Slider -----------
    upper_slider = tk.Scale(
        f4,
        from_=0,
        to=255,
        orient=tk.HORIZONTAL,
        resolution=1,
        label="Upper Threshold"
    )
    upper_slider.set(0)
    upper_slider.grid(row=1, column=0, padx=50, pady=10, sticky='ew')  
    upper_slider.config(**slider_style)
    upper_slider.config(command=on_edge_threshold_change)

    
    f4.grid_rowconfigure(0, weight=0)  
    f4.grid_rowconfigure(1, weight=0)  

def on_sharpening_intensity_change(val):

    apply_image_sharpening(val)

def sharpenFilter(f4):
    clear_frame4(f4)

   
    f4.grid_columnconfigure(0, weight=1)

    # ----------- Sharpening Intensity Slider -----------
    intensity_slider = tk.Scale(f4, from_=0, to=5, orient=tk.HORIZONTAL, resolution=0.1, label="Sharpening Intensity")
    intensity_slider.set(0)
    intensity_slider.grid(row=0, column=0, padx=50, pady=50, sticky='nsew') 

    intensity_slider.config(command=on_sharpening_intensity_change, **slider_style) 

    
    f4.grid_columnconfigure(0, weight=0)  



def on_smoothing_change(val):

    kernel_size = kernel_size_slider.get()
    std_deviation = std_dev_slider.get()
    apply_smoothing(kernel_size, std_deviation)

def smoothingFilter(f4):
    clear_frame4(f4)

    global kernel_size_slider, std_dev_slider

    
    f4.grid_columnconfigure(0, weight=0)  
    f4.grid_columnconfigure(1, weight=0)  

    # ----------- Kernel Size Slider -----------
    kernel_size_slider = tk.Scale(
        f4,
        from_=1,
        to=31,
        orient=tk.HORIZONTAL,
        resolution=2,
        label="Kernel Size"
    )
    kernel_size_slider.set(1)  
    kernel_size_slider.grid(row=0, column=0, padx=50, pady=10, sticky='ew')  

    # ----------- Standard Deviation Slider -----------
    std_dev_slider = tk.Scale(
        f4,
        from_=0,
        to=10,
        orient=tk.HORIZONTAL,
        resolution=0.1,
        label="Standard Deviation"
    )
    std_dev_slider.set(0)  
    std_dev_slider.grid(row=1, column=0, padx=50, pady=10, sticky='ew')  

    
    kernel_size_slider.config(command=on_smoothing_change, **slider_style)
    std_dev_slider.config(command=on_smoothing_change, **slider_style)

    
    f4.grid_rowconfigure(0, weight=0)  
    f4.grid_rowconfigure(1, weight=0)  
    


# def imageEnhancements(f4):
#     clear_frame4(f4)

    
#     noiseSlider = tk.Scale(f4, from_=0, to=10, orient=tk.HORIZONTAL, resolution=1, label="Noise Reduction Intensity",**slider_style)
#     noiseSlider.set(0)  
#     noiseSlider.grid(row=0, column=0, padx=20, pady=20)
    
#     colorNoiseSlider = tk.Scale(f4, from_=0, to=10, orient=tk.HORIZONTAL, resolution=1, label="ColorNoise Reduction Intensity",**slider_style)
#     colorNoiseSlider.set(0)  
#     colorNoiseSlider.grid(row=0, column=1, padx=20, pady=20)
    
#     sharpenSlider = tk.Scale(f4, from_=1, to=10, orient=tk.HORIZONTAL, resolution=1, label="Sharpening Intensity",**slider_style)
#     sharpenSlider.set(0)  
#     sharpenSlider.grid(row=0, column=2, padx=20, pady=20)

#     from src.gui.mainUI import get_EditedImgCanvas
#     # Assuming you have the EditedImgCanvas already defined or available
#     EditedImgCanvas = get_EditedImgCanvas()

#     noise_button = tk.Button(f4, text="Apply", 
#                          command=lambda: reducing_noise(model, int(noiseSlider.get()), EditedImgCanvas), 
#                          **button_style)
#     noise_button.grid(row=1, column=0, padx=20, pady=20)

#     color_noise_button = tk.Button(f4, text="Apply", 
#                                    command=lambda: reducing_noise_colored(int(colorNoiseSlider.get())),**button_style)
#     color_noise_button.grid(row=1, column=1, padx=20, pady=20)

#     sharpen_button = tk.Button(f4, text="Apply", 
#                                command=lambda: sharpening_image(int(sharpenSlider.get())),**button_style)
#     sharpen_button.grid(row=1, column=2, padx=20, pady=20)

    
#     f4.grid_columnconfigure(0, minsize=150)
#     f4.grid_columnconfigure(1, minsize=150)
#     f4.grid_columnconfigure(2, minsize=150)

def imageEnhancements_noSliders(f4):
    clear_frame4(f4)

    # Button creation helper
    def create_button(text, command, row, col):
        button = tk.Button(f4, text=text, command=command, **button_style)
        button.grid(row=row, column=col, padx=20, pady=20)

    # Create Buttons for each enhancement
    create_button("Apply", 
                  lambda: reducing_noise(model), 
                  0, 0)

    # Grid Configuration
    for col in range(3):
        f4.grid_columnconfigure(col, minsize=150)


