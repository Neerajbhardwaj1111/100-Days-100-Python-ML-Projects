from PIL import Image

ASCII_CHARS = "@%#*+=-:. "

def resize_image(image, new_width=100):
    width, height = image.size
    aspect_ratio = height / width
    new_height = int(aspect_ratio * new_width * 0.55)
    return image.resize((new_width, new_height))

def grayify(image):
    return image.convert("L")

def pixels_to_ascii(image):
    pixels = image.getdata()
    scale = len(ASCII_CHARS) - 1
    return ''.join(ASCII_CHARS[min(pixel * scale // 255, scale)] for pixel in pixels)

def image_to_ascii(path, width=100):
    try:
        image = Image.open(path)
    except:
        return "Image not valid!"

    image = resize_image(image, width)
    image = grayify(image)
    ascii_str = pixels_to_ascii(image)
    ascii_image = "\n".join(ascii_str[i:i+width] for i in range(0, len(ascii_str), width))
    return ascii_image
