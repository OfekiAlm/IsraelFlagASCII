import os
import time
from PIL import Image

ASCII_CHARS = ['@', '#', 'S', '%', '?', '*', '+', ';', ':', ',', '.']

def image_to_ascii(image_path, output_width=100):
    img = Image.open(image_path)
    width, height = img.size
    aspect_ratio = height / float(width)
    output_height = int(output_width * aspect_ratio)
    img = img.resize((output_width, output_height))
    img = img.convert('L')  # Convert to grayscale
    pixels = img.getdata()
    ascii_str = ''
    for pixel_value in pixels:
        ascii_str += ASCII_CHARS[pixel_value * len(ASCII_CHARS) // 256]
    img_ascii = [ascii_str[index: index + output_width] for index in range(0, len(ascii_str), output_width)]
    return img_ascii

def fade_in_ascii(ascii_img):
    for alpha in range(1, 11):
        os.system('cls' if os.name == 'nt' else 'clear')
        faded_frame = ''
        for row in ascii_img:
            faded_row = ''.join([char if char in ' .' else chr(97 + ((ord(char) - 97) * alpha) // 10) for char in row])
            faded_frame += faded_row + "\n"
        print(faded_frame)
        time.sleep(0.1)

if __name__ == '__main__':
    ascii_img = image_to_ascii("flag.png", 50)
    while True:  # Infinite loop
        fade_in_ascii(ascii_img)