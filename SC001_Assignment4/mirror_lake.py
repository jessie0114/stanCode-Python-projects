"""
File: mirror_lake.py
Name: Jessie
----------------------------------
This file reads in mt-rainier.jpg and
makes a new image that creates a mirror
lake vibe by placing an inverse image of
mt-rainier.jpg below the original one.
"""
from simpleimage import SimpleImage


def reflect(filename):
    """
    :param filename: str, Import image path
    :return new_img: SimpleImage, Export Mirror image
    Function: Mirror the original picture downward
    Principle: Symmetrically copy the RGB value of the original picture to achieve the mirror effect
    """
    original_mt = SimpleImage('images/mt-rainier.jpg')
    original_mt.show()

    b_img = SimpleImage.blank(original_mt.width, original_mt.height*2)
    b_img.show()

    for x in range(original_mt.width):
        for y in range(original_mt.height):
            original_mt_pixel = original_mt.get_pixel(x, y)

            b_img_pixel = b_img.get_pixel(x, y)
            b_img_pixel.red = original_mt_pixel.red
            b_img_pixel.green = original_mt_pixel.green
            b_img_pixel.blue = original_mt_pixel.blue

            reflected_pixel = b_img.get_pixel(x, b_img.height-1-y)
            reflected_pixel.red = original_mt_pixel.red
            reflected_pixel.green = original_mt_pixel.green
            reflected_pixel.blue = original_mt_pixel.blue
    b_img.show()
    return 0


def main():
    """
    Function: Mirror the original picture downward
    Principle: Display the original picture and the mirror picture
    """
    original_mt = SimpleImage('images/mt-rainier.jpg')
    original_mt.show()
    reflected = reflect('images/mt-rainier.jpg')
    reflected.show()


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
