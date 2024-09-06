from PIL import Image, ImageEnhance

def enhance_brightness_for_image(image_path, brightness_value):
    image = Image.open(image_path)
    brightness_enhancer = ImageEnhance.Brightness(image)
    outputted_image = brightness_enhancer.enhance(brightness_value)

    outputted_image.save('brightness_image.png')