"""
File: fire.py
Name: Jessie
---------------------------------
This file contains a method called
highlight_fires which detects the
pixels that are recognized as fire
and highlights them for better observation.
"""
from simpleimage import SimpleImage


HURDLE_FACTOR = 1.05


def highlight_fires(filename):
    """
    :param filename:str, the file path of the original image (with respect to current directory)
    :return:SimpleImage, the image with highlight fires and make the rest pixel gray.
    """
    highlight_img = SimpleImage(filename)
    for x in range(highlight_img.width):
        for y in range(highlight_img.height):
            pixel = highlight_img.get_pixel(x, y)
            avg = (pixel.red+pixel.blue+pixel.green) // 3
            if pixel.red > avg * HURDLE_FACTOR
                pixel.red = 255
            else:
                pixel.red = avg
                pixel.green = avg
                pixel.blue = avg
    return 0


def main():
    """
    This program will highlight the fire and make the rest pixel gray in original picture.
    """
    original_fire = SimpleImage('images/greenland-fire.png')
    original_fire.show()
    highlighted_fire = highlight_fires('images/greenland-fire.png')
    highlighted_fire.show()


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
