#!/usr/bin/env python3
from PIL import Image
import os

#to get all the image of directory
input_path = os.path.expanduser('~') + '/supplier-data/images/'
output_path = os.path.expanduser('~')+  "/supplier-data/images/"
all_tems = os.listdir(input_path)
print(len(all_tems))

for items in os.listdir(input_path):
    image_path = input_path+items
    if "README" in image_path or "LICENSE" in image_path:
      continue
    print("Image Path ",image_path)
    im = Image.open(image_path).convert("RGB")
    new_image = im.resize((600,400))
    #new_image = new_image.rotate(-90)
    file_name = (items.split("."))[0]
    print("Output Path", output_path+file_name)
    new_image.save(output_path+file_name+".jpeg","jpeg")
    im.close()
