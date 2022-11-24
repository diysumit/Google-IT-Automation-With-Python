#!/usr/bin/env python3

import os

"""Convert TIFF to JPEG"""

from PIL import Image

def ttj(file_path='/home/diysumit/supplier-data/images', save_path='/home/diysumit/supplier-data/images', size=(600, 400)):
    """
        Converts tiff pictures into smaller jpeg pictures, takes location of files, save location and size

        def ttj(file_path, save_path, size=(600, 400)):
            if not os.path.exists(save_path):
                os.mkdir(save_path)
            try:
                for file in os.listdir(file_path):
            
                if not file.endswith('.DS_Store'):
                    print(f'Converting: {file}.tiff to {file}.jpeg')
                    im = Image.open(f'{file_path}/{file}')
                    im.thumbnail((128, 128))
                    im.rotate(270).convert('RGB').save(f'{save_path}/{file}.jpeg')
                    im.close()
                else:
                    print('Skipping File')
            except Exception as e:
                print(f'Exception Occured: {e}')
    """
    if not os.path.exists(save_path):
        os.mkdir(save_path)
    try:
        for file in os.listdir(file_path):
            # file_name = re.search(r'([\w_]*[0-9]*)', file)
            # print(file_name.group(1))
            
            if not file.endswith('.DS_Store') and not file.endswith('.jpeg'):
                print(f'Converting: {file}.tiff to {file}.jpeg')
                im = Image.open(f'{file_path}/{file}')
                im.convert('RGB').resize(size).save(f'{save_path}/{file}.jpeg')
                im.close()
            else:
                print('Skipping File')
    except Exception as e:
        print(f'Exception Occured: {e}')
