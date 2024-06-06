"""
File: blur.py
Name: Jessie
-------------------------------
This file shows the original image(smiley-face.png)
first, and then its blurred image. The blur algorithm
uses the average RGB values of a pixel's nearest neighbors.
"""

from simpleimage import SimpleImage


def blur(img):
    """
    :param img:SimpleImage, the original image
    :return:SimpleImage, the updated image with all pixels turning blur
    """
    # Todo: create a new blank img that is as big as the original one
    new_img = SimpleImage.blank(new_w, new_h)
    # Loop over the picture
    for x in range(img.width):
        for y in range(img.height):
            img_pixel = img.get_pixel(x, y)


            # Belows are 9 conditions of pixel filling, depending on pixels' x,y orientation.
            
            if x == 0 and y == 0:
                # Get pixel at the top-left corner of the image.


            elif x == img.width-1 and y == 0:
                # Get pixel at the top-right corner of the image.
                pass

            elif x == 0 and y == img.height-1:
                # Get pixel at the bottom-left corner of the image
                pass

            elif x == img.width-1 and y == img.height-1:
                # Get pixel at the bottom-right corner of the image
                pass
 
            elif 0 < x < img.width-1 and y == 0:
                # Get top edge's pixels (without two corners)
                pass

            elif 0 < x < img.width-1 and y == img.height-1:
                # Get bottom edge's pixels (without two corners)
                pass

            elif x == 0 and 0 < y < img.height-1:
                # Get left edge's pixels (without two corners)
                pass

            elif x == img.width-1 and 0 < y < img.height-1:
                # Get right edge's pixels (without two corners)
                pass

            else:
                # Inner pixels.
                pass

    return new_img


def main():
    """
    This program will make the original picture blur.
    """
    old_img = SimpleImage("images/smiley-face.png")
    old_img.show()

    blurred_img = blur(old_img)
    for i in range(5):
        blurred_img = blur(blurred_img)
    blurred_img.show()


if __name__ == '__main__':
    main()
