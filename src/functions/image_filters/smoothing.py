import cv2

def image_smoothing(image_path, kernal_size, std_deviation):
    image = cv2.imread(image_path)
    smoothed_image = cv2.GaussianBlur(image, kernal_size, std_deviation)
    cv2.imwrite("smoothed_image.png", smoothed_image)

"""
Tests
- Run this in jupyter notebook (Uncomment This when your running it)

image_smoothing("image.png", (15, 15), 0)
"""