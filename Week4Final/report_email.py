#!/usr/bin/env python3

import os
import datetime
from Week4Final import report

input_path = os.path.expanduser('~')+'/supplier-data/descriptions/'


def generate_pdf():
  pdf_text = ""
  for item in os.listdir(input_path):
    input_file = input_path+item
    my_list = []
    with open(input_file) as f:
      count=0
      for line in f:
        #count=0
        if count<2:
          my_list.append(line.strip())
        count = count+1
      print(my_list)
      pdf_text += "name: " + my_list[0] + "<br/>" + "weight: " +my_list[1] + "<br/><br/>"
  print(pdf_text)
  return pdf_text


if __name__ == "__main__":
  current_date = datetime.datetime.now().strftime('%Y-%m-%d')
  #path = "supplier-data/descriptions/"
  title = "Process Updated on " + current_date
  #generate the package for pdf body
  package = generate_pdf()
  report.generate_report("/tmp/processed.pdf", title, package)
