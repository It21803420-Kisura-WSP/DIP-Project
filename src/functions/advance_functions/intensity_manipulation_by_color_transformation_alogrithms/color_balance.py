import cv2
import numpy as np

def color_balance(image):
    
    img_float = image.astype(np.float32)
    
    
    avg_b = np.mean(img_float[:, :, 0])  
    avg_g = np.mean(img_float[:, :, 1])  
    avg_r = np.mean(img_float[:, :, 2])  

    
    avg_global = (avg_b + avg_g + avg_r) / 3

   
    scale_b = avg_global / avg_b
    scale_g = avg_global / avg_g
    scale_r = avg_global / avg_r

 
    img_float[:, :, 0] = img_float[:, :, 0] * scale_b  
    img_float[:, :, 1] = img_float[:, :, 1] * scale_g  
    img_float[:, :, 2] = img_float[:, :, 2] * scale_r  

   
    img_balanced = np.clip(img_float, 0, 255).astype(np.uint8)

    return img_balanced


image = cv2.imread('image.png')

color_balance_image = color_balance(image)


cv2.imwrite('color_balance_image.jpg', color_balance_image)
cv2.imshow('color_balance Image', color_balance_image)
cv2.waitKey(0)
cv2.destroyAllWindows()