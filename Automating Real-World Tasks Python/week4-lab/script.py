#!/usr/bin/env python3

import tiff_to_jpeg
import emails
import supplier_image_upload
import fruit_dict

emails.generate()
emails.send()
tiff_to_jpeg.ttj()
supplier_image_upload.upload_images()
fruit_dictionary = fruit_dict.process_file()