import cv2
import numpy as np

def color_balance(image):
    # Step 1: Convert the image to float32 to avoid clipping during calculations
    img_float = image.astype(np.float32)
    
    # Step 2: Calculate the average value of each channel (R, G, B)
    avg_b = np.mean(img_float[:, :, 0])  # Blue channel
    avg_g = np.mean(img_float[:, :, 1])  # Green channel
    avg_r = np.mean(img_float[:, :, 2])  # Red channel

    # Step 3: Compute the global average
    avg_global = (avg_b + avg_g + avg_r) / 3

    # Step 4: Scale each channel based on the global average and the channel average
    scale_b = avg_global / avg_b
    scale_g = avg_global / avg_g
    scale_r = avg_global / avg_r

    # Step 5: Apply scaling to each channel
    img_float[:, :, 0] = img_float[:, :, 0] * scale_b  # Blue
    img_float[:, :, 1] = img_float[:, :, 1] * scale_g  # Green
    img_float[:, :, 2] = img_float[:, :, 2] * scale_r  # Red

    # Step 6: Clip the values to be within valid RGB range [0, 255]
    img_balanced = np.clip(img_float, 0, 255).astype(np.uint8)

    return img_balanced

# Load the image
image = cv2.imread('image.png')

# Apply color balancing
color_balance_image = color_balance(image)

# Save or display the balanced image
cv2.imwrite('color_balance_image.jpg', color_balance_image)
cv2.imshow('color_balance Image', color_balance_image)
cv2.waitKey(0)
cv2.destroyAllWindows()