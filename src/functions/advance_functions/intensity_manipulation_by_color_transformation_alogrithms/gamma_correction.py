import cv2
import numpy as np

def gamma_correction(image_path, gamma_value):
    inv_gamma = 1/gamma_value
    table = [((i / 255) ** inv_gamma) * 255 for i in range(256)]
    table = np.array(table, np.uint8)

    return cv2.LUT(image_path, table)

image = cv2.imread("image.png")
gamma_image = gamma_correction(image, .2)

cv2.imshow('Original image', image)
cv2.imshow('Gamma corrected image', gamma_image)
cv2.waitKey(0)
cv2.destroyAllWindows()