import cv2
import numpy as np

def histogram_equalization(image):
    # Convert to YCrCb color space
    ycrcb = cv2.cvtColor(image, cv2.COLOR_BGR2YCrCb)

    # Apply histogram equalization on the Y channel (luminance)
    ycrcb[:, :, 0] = cv2.equalizeHist(ycrcb[:, :, 0])

    # Convert back to BGR color space
    equalized_image = cv2.cvtColor(ycrcb, cv2.COLOR_YCrCb2BGR)

    return equalized_image

image = cv2.imread('image.png')
histogram_equalization_image = histogram_equalization(image)

cv2.imwrite('histogram_equalization.jpg', histogram_equalization_image)
cv2.imshow('histogram equalized Image', histogram_equalization_image)
cv2.waitKey(0)
cv2.destroyAllWindows()