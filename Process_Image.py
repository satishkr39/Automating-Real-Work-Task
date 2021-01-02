#!/usr/bin/env python3
from PIL import Image
import os

#to get all the image of directory
input_path = os.path.expanduser('~') + '/images/'
output_path = "/opt/icons/"
all_tems = os.listdir(input_path)
print(len(all_tems))

for items in os.listdir(input_path):
    image_path = input_path+items
    print(image_path)
    if ".DS_Store" in image_path:
        continue
    im = Image.open(image_path).convert("RGB")
    new_image = im.resize((128,128))
    new_image = new_image.rotate(-90)
    file_name = (items.split("."))[0]
    new_image.save(output_path+file_name+".jpeg","jpeg")
    im.close()
