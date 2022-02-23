'''
This file will produce json files in another directory that will have using the yescik:
cik:
... start_index
... end_index

Also, maybe what this script will do is go into the yescik directory since it is clean,
it will produce another direcory called yescikdi, with json files that have the diversity and section section only
'''
import os
#import pandas as pd
import json
import sec_data_lists

yes_hc_path = '../ST542_secDisclosures/yescik'
for file in yes_hc_path:
    with open(file, encoding='utf-8') as content:
        json_data = json.load(content)
    break
