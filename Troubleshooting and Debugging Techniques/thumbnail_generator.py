#!/usr/bin/env python3

import argparse
import logging
import os
import sys

import PIL
import PIL.Image

from concurrent import futures

def process_options():

    kwargs = {
        'format' : '[%(levelname)s] %(message)s'
    }

    parser = argparse.ArgumentParser(
        description='Thumbnail generator'
        fromfile_prefix_chars='@'
    )
    parser.add_argument('--debug', action='store_true')

def progress_bar(files):
    return tqdm(files, desc='Processing', total=len(files), dynamic_ncols=True)

def main():

    process_options()

    # create the thumbnails directory
    if not os.path.exists('thumbnails'):
        os.mkdir('thumbnails')

    executor = futures.ProcessPoolExecutor()#futures.ThreadPoolExecutor()

    for root, _, files in os.walk('images'):
        for basename in progress_bar(files):
            if not basename.endswith('.jpg'):
                continue
            executor.submit(process_file, root, basename)
    print('Waiting for all threads to finish.')
    executor.shutdown()
    return 0

if __name__ == "__main__":
    sys.exit(main())
