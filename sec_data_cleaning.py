import os
#import pandas as pd
import json
import nltk
import unicodedata
import pprint
import re
import string
import sec_functions
import sec_data_cleanv2
import di_function
import di_function_v2
import di_analysis
from glob import glob
from collections import Counter
#from nltk.tokenize import word_tokenize

clean = sec_functions.clean
filter_di = di_function.filter_di
di_stat = di_analysis.di_stat
clean_v2 = sec_data_cleanv2.clean_v2
filter_di_v2 = di_function_v2.filter_di_v2
#combine_json = sec_data_cleanv2.combine_json


# Open json file for reading and print content using json.load
for file_name in glob('*.json'):
    #print(file_name) # working with allFilings2021_part1.json
    with open(file_name, encoding='utf-8') as content:
        json_data = json.load(content)
        clean_json_data = clean(json_data)

    break # Would need to comment this out for the other json files for part2-6


#print(file_name)
# Currently missing 3 json. Not sure which ones
#for file_name in glob('*.json'):
for json_file in os.listdir("../ST542_secDisclosures/yescik/"):
    with open(file_name, encoding='utf-8') as content: #Weird how the file_name works here, now thinking about it, currently assuming filename is allFilings2021_part1.json
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
        #print(di_file_dic)
        #pprint.pprint(json_data)

    break


# V2 format
# Testing purposes
files = ['allFilings2021_part2.json','allFilings2021_part3.json','allFilings2021_part4.json','allFilings2021_part5.json','allFilings2021_part6.json']
output_dic = {}
for file in files:
    file_dic = {}
    with open(file, encoding = 'utf-8') as content:
        json_data = json.load(content)
        clean_json_data = clean_v2(json_data)
        file_dic[file] = clean_json_data
        output_dic.update(file_dic)
        #combine_json(file,clean_json_data)
        #print(json_data)

    #break
if not os.path.exists(f"../ST542_secDisclosures/cik_v2/"):
    os.makedirs(f"../ST542_secDisclosures/cik_v2/")
with open(f"../ST542_secDisclosures/cik_v2/cikv2output.json","w", encoding='utf8') as new_content:
    json.dump(output_dic, new_content,ensure_ascii=False, indent=4)

#all_outer_json = {}
# This for loop logic is now wrong
json_file = "cikv2output.json"
#for json_file in os.listdir("../ST542_secDisclosures/cik_v2/"):
if json_file in os.listdir("../ST542_secDisclosures/cik_v2/"):
    new_name = f"../ST542_secDisclosures/cik_v2/{json_file}"
    #new_name = json_file
    file_dic = {}
    with open(new_name,encoding = 'utf-8') as content:
        json_data = json.load(content)
        filter_di_data2 = filter_di_v2(json_data)
        filter_di_data2
        # all_outer_json[json_file] = filter_di_data2
        # all_outer_json.update(file_dic)
        #filter_di_data2
# with open(f"../ST542_secDisclosures/cik_v2/dioutput.json","w", encoding='utf8') as new_content:
#     new_content.write(json.dump(all_outer_json, new_content,ensure_ascii=False, indent=4))