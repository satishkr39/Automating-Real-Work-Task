#!/usr/bin/env python3
import requests
import os
# This example shows how a file can be uploaded using
# The Python Requests module


input_path = os.path.expanduser('~') + '/supplier-data/images/'
url = "http://localhost/upload/"

for item in os.listdir(input_path):
  if ".tiff" in item or "README" in item or "LICENSE" in item:
    continue
  print(item)
  with open(input_path+item, 'rb') as opened:
    r = requests.post(url, files={'file': opened})
