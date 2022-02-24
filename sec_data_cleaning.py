import os
#import pandas as pd
import json
import nltk
import unicodedata
import pprint
import re
import string
import sec_functions
import di_function
import di_analysis
from glob import glob
from collections import Counter
#from nltk.tokenize import word_tokenize

clean = sec_functions.clean
filter_di = di_function.filter_di
di_stat = di_analysis.di_stat


# Open json file for reading and print content using json.load
for file_name in glob('*.json'):
    #print(file_name) # working with allFilings2021_part1.json
    with open(file_name, encoding='utf-8') as content:
        json_data = json.load(content)
        clean_json_data = clean(json_data)

    break # Would need to comment this out for the other json files for part2-6

print(file_name)
# Currently missing 3 json. Not sure which ones
#for file_name in glob('*.json'):
for json_file in os.listdir("../ST542_secDisclosures/yescik/"):
    with open(file_name, encoding='utf-8') as content: #Weird how the file_name works here, now thinking about it
        json_data = json.load(content)
        filter_di_data = filter_di(json_data)
        filter_di_data

    break



# NLP Analysis work
for di_file in os.listdir("../ST542_secDisclosures/yescik/di/"):
    #print(di_file)
    di_file_dic = {}
    new_di_file = f"../ST542_secDisclosures/yescik/di/{di_file}"
    with open(new_di_file, encoding='utf-8') as content:
    #with open(di_file) as content:
        json_data = json.load(content)
        di_stat_data = di_stat(json_data)
        #di_stat_data

        #di_file_dic[f"{di_file}"] = di_stat_data
        di_file_dic[di_file] = di_stat_data
        print(di_file_dic)
        #pprint.pprint(json_data)

    break
