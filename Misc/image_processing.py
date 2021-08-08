import os, sys, base64
from PIL import Image, ImageFilter
import time

IMAGE_01 = 'image01.jpg'
size = (128, 128)

try:
    convert_start = time.time()

    with Image.open(IMAGE_01) as im:
        im.thumbnail(size)
        out = im.filter(ImageFilter.DETAIL)
        out.save(IMAGE_01, "JPEG")
    
    convert_end = time.time()
    print("Time to convert img")
    print((convert_end - convert_start))

    # Turn image to string response
    with open(IMAGE_01, "rb") as im:
        img_bytes = base64.b64encode(im.read())
        print(img_bytes)


except OSError:
    print('Error creating thumbnail')
