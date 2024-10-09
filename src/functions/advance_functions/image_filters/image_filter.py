import numpy as np 
import matplotlib.pyplot as plt 
from scipy import signal 
import math 
import cv2

def low_pass_butterworth_filter(img_path, sampling_freq, pass_band, stop_band, band_ripple, stop_attenuation):
    # Convert pass band and stop band frequencies to normalized frequencies (0 to 1)
    wp = pass_band/(sampling_freq/2)
    ws = stop_band/(sampling_freq/2)

    # Butterworth filter design in the digital domain
    N, Wn = signal.buttord(wp, ws, band_ripple, stop_attenuation, analog=False)

    # Printing the values of order & cut-off frequency! 
    print("Order of the Filter=", N)  
    print("Cut-off frequency= {:.3f} (normalized)".format(Wn))  

    # Design a low-pass digital Butterworth filter
    b, a = signal.butter(N, Wn, btype='low', analog=False)

    # Load and convert the image to grayscale
    img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
    if img is None:
        print(f"Error: Cannot load image from path {img_path}")
        return
    
    # Display the original image
    plt.figure(figsize=(6, 6))
    plt.imshow(img, cmap='gray')
    plt.title("Original Image")
    plt.show()

    # 2D Fourier Transform
    f_transform = np.fft.fft2(img)
    f_shift = np.fft.fftshift(f_transform)  # Shift the zero frequency component to the center
    
    # Create a low-pass Butterworth filter in the frequency domain
    rows, cols = img.shape
    crow, ccol = rows // 2, cols // 2  # center of the image

    # Adjust meshgrid to match the image size exactly, considering odd sizes
    U, V = np.meshgrid(np.arange(-ccol, ccol + (cols % 2)), np.arange(-crow, crow + (rows % 2)))
    D = np.sqrt(U**2 + V**2)

    # Apply the Butterworth low-pass filter formula
    D0 = Wn * max(rows, cols) / 2  
    butterworth_filter = 1 / (1 + (D / D0)**(2 * N))

    # Apply the Butterworth filter in the frequency domain
    filtered_shift = f_shift * butterworth_filter

    # Inverse FFT to get the filtered image back
    f_ishift = np.fft.ifftshift(filtered_shift)
    img_back = np.fft.ifft2(f_ishift)
    img_back = np.abs(img_back)  # Take the absolute value (magnitude) of the inverse FFT

    # Normalize the result to fit in [0, 255] for display
    img_back = np.uint8(cv2.normalize(img_back, None, 0, 255, cv2.NORM_MINMAX))

    # Display the filtered image
    plt.figure(figsize=(6, 6))
    plt.imshow(img_back, cmap='gray')
    plt.title("Filtered Image (Butterworth Low-Pass)")
    plt.show()

# Test the function
img_path = "image.png"  
sampling_freq = 40000
pass_band = 4000
stop_band = 8000
band_ripple = 0.5
stop_atten = 40
low_pass_butterworth_filter(img_path, sampling_freq, pass_band, stop_band, band_ripple, stop_atten)


def low_pass_butterworth_filter_color_image(img_path, sampling_freq, pass_band, stop_band, band_ripple, stop_attenuation):
    # Convert pass band and stop band frequencies to normalized frequencies (0 to 1)
    wp = pass_band/(sampling_freq/2)
    ws = stop_band/(sampling_freq/2)

    # Butterworth filter design in the digital domain
    N, Wn = signal.buttord(wp, ws, band_ripple, stop_attenuation, analog=False)

    # Printing the values of order & cut-off frequency
    print("Order of the Filter=", N)  
    print("Cut-off frequency= {:.3f} (normalized)".format(Wn))  

    # Design a low-pass digital Butterworth filter
    b, a = signal.butter(N, Wn, btype='low', analog=False)

    # Load the color image
    img = cv2.imread(img_path)
    if img is None:
        print(f"Error: Cannot load image from path {img_path}")
        return
    
    # Convert the image from BGR (OpenCV format) to RGB for display
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    # Display the original image
    plt.figure(figsize=(6, 6))
    plt.imshow(img)
    plt.title("Original Image")
    plt.show()

    # Split the image into R, G, B channels
    channels = cv2.split(img)
    filtered_channels = []

    # Process each channel separately
    for channel in channels:
        # 2D Fourier Transform
        f_transform = np.fft.fft2(channel)
        f_shift = np.fft.fftshift(f_transform)  # Shift the zero frequency component to the center

        # Create a low-pass Butterworth filter in the frequency domain
        rows, cols = channel.shape
        crow, ccol = rows // 2, cols // 2  # center of the image

        # Adjust meshgrid to match the image size exactly, considering odd sizes
        U, V = np.meshgrid(np.arange(-ccol, ccol + (cols % 2)), np.arange(-crow, crow + (rows % 2)))
        D = np.sqrt(U**2 + V**2)

        # Apply the Butterworth low-pass filter formula
        D0 = Wn * max(rows, cols) / 2  
        butterworth_filter = 1 / (1 + (D / D0)**(2 * N))

        # Apply the Butterworth filter in the frequency domain
        filtered_shift = f_shift * butterworth_filter

        # Inverse FFT to get the filtered image back
        f_ishift = np.fft.ifftshift(filtered_shift)
        img_back = np.fft.ifft2(f_ishift)
        img_back = np.abs(img_back)  # Take the absolute value (magnitude) of the inverse FFT

        # Normalize the result to fit in [0, 255] for display
        img_back = np.uint8(cv2.normalize(img_back, None, 0, 255, cv2.NORM_MINMAX))

        # Append the filtered channel
        filtered_channels.append(img_back)

    # Merge the filtered channels back into a color image
    filtered_img = cv2.merge(filtered_channels)

    # Display the filtered image
    plt.figure(figsize=(6, 6))
    plt.imshow(filtered_img)
    plt.title("Filtered Image (Butterworth Low-Pass)")
    plt.show()

# Example usage (you can change the parameters as per your image and requirements)
img_path = 'image.png'
sampling_freq = 1000  # example value
pass_band = 20  # example value
stop_band = 40  # example value
band_ripple = 0.5  # example value
stop_atten = 40  # example value
low_pass_butterworth_filter_color_image(img_path, sampling_freq, pass_band, stop_band, band_ripple, stop_atten)

def high_pass_butterworth_filter(image_path, sampling_freq, pass_band, stop_band, band_ripple):
    # Load and convert the image to grayscale
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    if img is None:
        print(f"Error: Cannot load image from path {image_path}")
        return
    
    # Display the original image
    plt.figure(figsize=(6, 6))
    plt.imshow(img, cmap='gray')
    plt.title("Original Image")
    plt.show()

    # 2D Fourier Transform of the image
    f_transform = np.fft.fft2(img)
    f_shift = np.fft.fftshift(f_transform)  # Shift zero frequency component to the center
    
    # Get image dimensions
    rows, cols = img.shape
    crow, ccol = rows // 2, cols // 2  # Center of the image
    
    # Create a high-pass Butterworth filter in the frequency domain
    D0 = pass_band  # Set the cutoff frequency
    N = 2  # Butterworth filter order
    
    # Create meshgrid for the filter design, ensuring it matches the image size
    U, V = np.meshgrid(np.arange(-ccol, ccol + (cols % 2)), np.arange(-crow, crow + (rows % 2)))
    D = np.sqrt(U**2 + V**2)
    
    # Avoid division by zero by replacing zeros in D with a small value
    D = np.where(D == 0, 1e-10, D)  # Replace 0s with a small non-zero value

    # Apply the Butterworth high-pass filter formula
    butterworth_filter = 1 / (1 + (D0 / D)**(2 * N))

    # Apply the filter to the frequency domain of the image
    filtered_shift = f_shift * butterworth_filter

    # Inverse FFT to get the filtered image back
    f_ishift = np.fft.ifftshift(filtered_shift)
    img_back = np.fft.ifft2(f_ishift)
    img_back = np.abs(img_back)  # Take the magnitude of the inverse FFT

    # Normalize the result to fit in [0, 255] for display
    img_back = np.uint8(cv2.normalize(img_back, None, 0, 255, cv2.NORM_MINMAX))

    # Display the filtered image
    plt.figure(figsize=(6, 6))
    plt.imshow(img_back, cmap='gray')
    plt.title("Filtered Image (High-Pass Butterworth)")
    plt.show()

# Test the function
image_path = "image.png"  
sampling_freq = 4000  # This is ignored in the context of image processing
pass_band = 30  # Set a cutoff frequency for high-pass filtering
stop_band = 10  # Stopband frequency (not directly used in this example)
band_ripple = 0.5  # Passband ripple (not directly used in this example)

high_pass_butterworth_filter(image_path, sampling_freq, pass_band, stop_band, band_ripple)


def high_pass_butterworth_filter_color_image(image_path, sampling_freq, pass_band, stop_band, band_ripple):
    # Load the color image
    img = cv2.imread(image_path)
    if img is None:
        print(f"Error: Cannot load image from path {image_path}")
        return
    
    # Convert the image from BGR (OpenCV format) to RGB for display
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    # Display the original image
    plt.figure(figsize=(6, 6))
    plt.imshow(img)
    plt.title("Original Image")
    plt.show()

    # Split the image into R, G, B channels
    channels = cv2.split(img)
    filtered_channels = []

    # Process each channel separately
    for channel in channels:
        # 2D Fourier Transform
        f_transform = np.fft.fft2(channel)
        f_shift = np.fft.fftshift(f_transform)  # Shift the zero frequency component to the center

        # Get image dimensions
        rows, cols = channel.shape
        crow, ccol = rows // 2, cols // 2  # Center of the image

        # Create a high-pass Butterworth filter in the frequency domain
        D0 = pass_band  # Set the cutoff frequency
        N = 2  # Butterworth filter order

        # Create meshgrid for the filter design, ensuring it matches the image size
        U, V = np.meshgrid(np.arange(-ccol, ccol + (cols % 2)), np.arange(-crow, crow + (rows % 2)))
        D = np.sqrt(U**2 + V**2)

        # Avoid division by zero by replacing zeros in D with a small value
        D = np.where(D == 0, 1e-10, D)  # Replace 0s with a small non-zero value

        # Apply the Butterworth high-pass filter formula
        butterworth_filter = 1 / (1 + (D0 / D)**(2 * N))

        # Apply the filter to the frequency domain of the image
        filtered_shift = f_shift * butterworth_filter

        # Inverse FFT to get the filtered image back
        f_ishift = np.fft.ifftshift(filtered_shift)
        img_back = np.fft.ifft2(f_ishift)
        img_back = np.abs(img_back)  # Take the magnitude of the inverse FFT

        # Normalize the result to fit in [0, 255] for display
        img_back = np.uint8(cv2.normalize(img_back, None, 0, 255, cv2.NORM_MINMAX))

        # Append the filtered channel
        filtered_channels.append(img_back)

    # Merge the filtered channels back into a color image
    filtered_img = cv2.merge(filtered_channels)

    # Display the filtered image
    plt.figure(figsize=(6, 6))
    plt.imshow(filtered_img)
    plt.title("Filtered Image (High-Pass Butterworth)")
    plt.show()

# Test the function
image_path = "image.png"  
sampling_freq = 4000  # This is ignored in the context of image processing
pass_band = 30  # Set a cutoff frequency for high-pass filtering
stop_band = 10  # Stopband frequency (not directly used in this example)
band_ripple = 0.5  # Passband ripple (not directly used in this example)

high_pass_butterworth_filter_color_image(image_path, sampling_freq, pass_band, stop_band, band_ripple)