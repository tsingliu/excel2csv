#!/usr/bin/env python
#-* coding: utf-8 -*

import threading
import datetime
import pyexcel as pe
import glob
import config


files = []
dest_file = config.data['dest_file']

for src_file in config.data['files']:
   src_files = glob.glob(src_file)
   for src_file in src_files: files.append(src_file)
print(files)

records = []

for file in files:
   record = pe.iget_records(file_name=file)
   records.append(record)  


def merge_row(records):
   for record in records:
      for row in record:
         yield row 

def replace_commas(row):
   for element in row:
        if isinstance(element,str):
           element = element.replace(',','')
        yield element

pe.isave_as(records=merge_row(records),row_renderer=replace_commas,encoding='utf-8-sig',dest_file_name=dest_file)
