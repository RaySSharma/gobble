from PIL import Image
from os import path
from glob import glob
from sys import exit
from random import choice

from . import assets


def gobble(image_number=None):
    """Displays a gobble image

    Pulls a gobble image from the ./assets/ directory and displays the image. If given an integer argument, attempts to
    pull the corresponding image, otherwise pulls a random image.

    Args:
        image_number (int, optional): Image number to show, defaults to None.
    """
    assets_dir = path.dirname(assets.__file__)
    all_images = glob(path.join(assets_dir, '*.png'))
    if image_number is None:
        image_name = choice(all_images)
    else:
        image_name = None
        try:
            image_name = all_images[image_number]
        except (TypeError, IndexError) as err:
            print(err)
            exit()

    im_file = path.join(assets_dir, image_name)
    Image.open(im_file).show()
    print('gobble')
