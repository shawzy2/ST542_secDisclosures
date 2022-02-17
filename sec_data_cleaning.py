import os
#import pandas as pd
import json
import pprint
from glob import glob

# Open json file for reading and print content using json.load
for file_name in glob('*.json'):
    #print(file_name)
    with open(file_name, encoding='utf-8') as content:
        #json_content = content.read()
        #json_data = json.loads(json_content)
        json_data = json.load(content)
        pprint.pprint(json_data)
        #print(json_data)
        #print(file_name)
        #print(json_data)
        #print(type(file_name))
    break
# with open("","r") as content:
#     print(json.l)