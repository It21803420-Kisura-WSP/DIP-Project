from PIL import Image, ImageEnhance

def enhance_color_for_image(image_path, color_value):
    image = Image.open(image_path)
    color_enhancer = ImageEnhance.Color(image)
    outputted_image = color_enhancer.enhance(color_value)

    outputted_image.save('color_image.png')