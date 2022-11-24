#!/usr/bin/env python3

import os
import sys
# import re

from PIL import Image

def main():
    if not os.path.exists('./fixed/'):
        os.mkdir('./fixed')
    try:
        for file in os.listdir('./images/'):
            # file_name = re.search(r'([\w_]*[0-9]*)', file)
            # print(file_name.group(1))
            
            if not file.endswith('.DS_Store'):
                print(f'Converting: {file}.tiff to {file}.jpeg')
                im = Image.open(f'./images/{file}')
                im.thumbnail((128, 128))
                im.rotate(270).convert('RGB').save(f'./fixed/{file}.jpeg')
                im.close()
            else:
                print('Skipping File')
    except Exception as e:
        print(f'Exception Occured: {e}')

if __name__ == "__main__":
    sys.exit(main())
