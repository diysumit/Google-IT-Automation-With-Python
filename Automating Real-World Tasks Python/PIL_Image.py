#!/usr/bin/env python3

import PIL
import sys

from PIL import Image

def main():
    im = Image.open('/home/diysumit/pic.png')
    new_im_resized = im.resize((640, 480))
    new_im_resized.save('/home/diysumit/resized_img_640X480.png')
    new_im_rotated = im.rotate(35)
    new_im_rotated.save('/home/diysumit/rotated_img_35.png')
    im.rotate(35).resize((640, 480)).save('/home/diysumit/img_rotatedAndResized.png')
    im.new('L', (128, 128), color=10)

if __name__ == "__main__":
    sys.exit(main())
