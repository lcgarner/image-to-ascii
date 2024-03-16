import sys
from PIL import Image

ASCII_CHARS = "@%#*+=-:. "

def load_image(image_path):
    return Image.open(image_path)

def grayscale_image(image):
    return image.convert("L")

def resize_image(image, new_width=100):
    width, height = image.size
    ratio = height / width / 1.65
    new_height = int(new_width * ratio)
    resized_image = image.resize((new_width, new_height))
    return resized_image

def map_pixels_to_ascii(image, range_width=25):
    pixels = image.getdata()
    ascii_str = ''
    for pixel_value in pixels:
        ascii_str += ASCII_CHARS[pixel_value // range_width]
    return ascii_str

def convert_image_to_ascii(image, new_width=100):
    image = resize_image(image, new_width)
    image = grayscale_image(image)

    ascii_str = map_pixels_to_ascii(image)
    img_width = image.width
    ascii_str_len = len(ascii_str)
    ascii_img=""

    for i in range(0, ascii_str_len, img_width):
        ascii_img += ascii_str[i:i+img_width] + "\n"

    return ascii_img

def main():
    if len(sys.argv) > 1:
        image_path = sys.argv[1]  
    else:
        image_path = input("Enter the path to the image file: ")  

    try:
        width = int(input("Enter the desired width of the ASCII Art (e.g., 100): "))
    except ValueError:
        print("Invalid width. Using default width of 100.")
        width = 100

    try:
        image = load_image(image_path)
    except Exception as e:
        print("Unable to open image file:", image_path)
        print(e)
        return
    
    ascii_img = convert_image_to_ascii(image, width)
    print(ascii_img)

if __name__ == '__main__':
    main()
