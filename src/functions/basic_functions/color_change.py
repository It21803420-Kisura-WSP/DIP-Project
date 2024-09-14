import cv2

def convert_image_to_grayscale(image_path):
    original_image = cv2.imread(image_path)
    gray_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)
    return gray_image

def convert_image_to_bw(image_path):
    original_image = cv2.imread(image_path)
    gray_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)
    (thresh, black_n_white_image) = cv2.threshold(gray_image, 127, 255, cv2.THRESH_BINARY)
    return black_n_white_image