#!/usr/bin/env python3

import os
import requests

#response = requests.get("http://34.68.1.204/")
#print(response.status_code)

input_path =  '/data/feedback/'
all_files = os.listdir(input_path)
print(len(all_files))
for item in all_files:
  print(item)
  read_file = '/data/feedback/'+item
  my_dict = {}
  my_list = []
  print(read_file)
  print("----Printing LInes---")
  with open(read_file) as f:
    for line in f:
      my_list.append(line)
    my_dict["title"] = my_list[0].strip()
    my_dict["name"] = my_list[1].strip()
    my_dict["date"] = my_list[2].strip()
    my_dict["feedback"] = my_list[3].strip()
    f.close()
  print(my_dict)
  respone = requests.post("http://34.68.1.204/feedback/",data=my_dict )
