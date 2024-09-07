import cv2
import numpy as np

def clahe_color_balance(image):
    
    lab = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)

   
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    lab[:, :, 0] = clahe.apply(lab[:, :, 0])

   
    clahe_image = cv2.cvtColor(lab, cv2.COLOR_LAB2BGR)

    return clahe_image

image = cv2.imread('image.png')
clahe_color_balance_image = clahe_color_balance(image)

cv2.imwrite('clahe_color_balance.jpg', clahe_color_balance_image)
cv2.imshow('clahe balanced', clahe_color_balance_image)
cv2.waitKey(0)
cv2.destroyAllWindows()