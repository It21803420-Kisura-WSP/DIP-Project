from PIL import Image

def crop(image_path, startx, endx, starty, endy):
    image = Image.open(image_path)
    cropped_image = image.crop(startx, starty, endx, endy)
    return cropped_image