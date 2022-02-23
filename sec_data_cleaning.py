import os
#import pandas as pd
import json
import unicodedata
import pprint
import re
import string
#import sec_data_lists
import sec_functions
import dipart1_functions
from glob import glob

clean = sec_functions.clean
filter_di = dipart1_functions.filter_di


# Open json file for reading and print content using json.load
for file_name in glob('*.json'):
    #print(file_name) # working with allFilings2021_part1.json
    with open(file_name, encoding='utf-8') as content:
        json_data = json.load(content)
        clean_json_data = clean(json_data)

    break # Would need to comment this out for the other json files for part2-6


# Currently missing 3 json. Not sure which ones
#for file_name in glob('*.json'):
for json_file in os.listdir("../ST542_secDisclosures/yescik/"):
    with open(file_name, encoding='utf-8') as content: #Weird how the file_name works here, now thinking about it
        json_data = json.load(content)
        filter_di_data = filter_di(json_data)
        filter_di_data

    break
