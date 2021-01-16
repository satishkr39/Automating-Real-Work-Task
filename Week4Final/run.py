
#!/usr/bin/env python3

import os
import requests
import json


input_path = os.path.expanduser('~') + '/supplier-data/descriptions/'


#print(input_path)

url = "http://173.255.119.13/fruits/"


print(requests.get(url))
#my_list = []
final_json = {}
for item in os.listdir(input_path):
  read_file = input_path+item
  print(read_file)
  print("------")
  with open(read_file) as f:
    my_json = {}
    my_list = []
    for line in f:
     # print(line)
      my_list.append(line.strip())
    #print(my_list)
    my_json["name"] = my_list[0]
    my_json["weight"] = int((my_list[1]).split(" ")[0])
    print(my_json["weight"])
    my_json["description"] = my_list[2]
    print(my_json)
    my_json["image_name"] = item.split(".")[0]+".jpeg"
    print(my_json)
    response = requests.post(url, json=my_json)
    response.raise_for_status()
