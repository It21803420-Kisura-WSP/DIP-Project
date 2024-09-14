from PIL import Image

def vertical_flip(image_path):
    original_image = Image.open(image_path)
    vertical_image = original_image.transpose(method=Image.FLIP_TOP_BOTTOM)

    return vertical_image

def horizontal_flip(image_path):
    original_image = Image.open(image_path)
    horizontal_image = original_image.transpose(method=Image.FLIP_LEFT_RIGHT)

    return horizontal_image