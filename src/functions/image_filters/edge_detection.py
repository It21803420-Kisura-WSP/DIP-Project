import cv2


def edge_detection(image_path, low_threshold, upper_threshold):
    image = cv2.imread(image_path)
    edged_image = cv2.Canny(image, low_threshold, upper_threshold)
    cv2.imwrite("edged_image.png", edged_image)

"""
Tests
- Run this in jupyter notebook (Uncomment This when your running it)

edge_detection("image.png", 200, 100)
"""