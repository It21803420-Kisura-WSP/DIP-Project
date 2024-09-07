from PIL import Image, ImageEnhance

def enhance_contrast_for_image(image_path, contrast_value):
    image = Image.open(image_path)
    contrast_enhancer = ImageEnhance.Contrast(image)
    outputted_image = contrast_enhancer.enhance(contrast_value)

    outputted_image.save('contrast_image.png')