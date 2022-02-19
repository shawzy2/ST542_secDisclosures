import os
#import pandas as pd
import json
import unicodedata
import pprint
import re
from glob import glob

def clean(d):
    dictionary_data = d
    clean_dict = {}
    #no_hc = {}
    yes_hc = {}
    #new_val = []
    non_element = [" ","","— ","•","    ",",",", ",": ",".","$",")","(a)","(b)", "(",
    "                                           ","◦","■","▪"," — ","—","*","%", "®", "® ", "X","†","††", "•",", ",")%",
    ". ","​"]

    #unicode_element = ['\xa0','\u200b','\u2019','']
    #unicode_element = ['\u200b','\u2019','\u201c','\u201d','\u00a0']

    #For some odd reason, I could not get rid of %, \xa0
    for cik, value_list in dictionary_data.items():
        #print(cik)
        # We would want to strip empty elements, dash elements, elements that have \xa0, percent elements, dot element and period, etc.
        # "4962" is empty list
        #if cik == "4962":
        if cik not in clean_dict:
        # Would eventually have to indent this line]
            new_val = []
            temp_val = []
            temp_val2 = []
            no_hc = {}
            no_hc_list = []
            if value_list == []:
                nohc = 'There is no Human Capital Disclosure'
                no_hc_list.append(nohc)
                no_hc[cik] = no_hc_list
                #pprint.pprint(no_hc)
                for i in range(len(list(no_hc.keys()))):
                    new_dict2 = {}
                    new_dict2[list(no_hc.keys())[i]] = list(no_hc.values())[i]
                    no_hc_path = '../ST542_secDisclosures/nocik'
                    #print(list(no_hc.values())[i])
                    for k, v in new_dict2.items():
                        if k in list(no_hc.keys()):
                            if not os.path.exists(no_hc_path):
                                os.makedirs(no_hc_path)
                            with open(f"../ST542_secDisclosures/nocik/{list(no_hc.keys())[i]}.json","w", encoding='utf8') as new_content:
                                json.dump(new_dict2, new_content,ensure_ascii=False, indent=4)
                                print(f"Creating: ../ST542_secDisclosures/nocik/{list(no_hc.keys())[i]}.json file") 
                #temp_val.append(element)
            else:
                #########################

                for element in value_list:
                    #if element in non_element:
                    if element not in non_element:
                        temp_val.append(element)

                for i in temp_val:
                    if '\xa0' in i:
                        temp_val2.append(i.replace('\xa0',''))
                    # elif "​" in i:
                    #     temp_val
                    else:
                        temp_val2.append(i)

                new_val = temp_val2
                #no_hc[cik] = no_hc_list
                clean_dict[cik] = new_val
                yes_hc[cik] = "There is Human Capital"
                for i in range(len(list(clean_dict.keys()))):
                    new_dict = {}
                    new_dict[list(clean_dict.keys())[i]] = list(clean_dict.values())[i]
                    yes_hc_path = '../ST542_secDisclosures/yescik'
                    for k, v in new_dict.items():
                        if k in list(yes_hc.keys()): # This is causing the error
                            if not os.path.exists(yes_hc_path):
                                os.makedirs(yes_hc_path)
                            with open(f"../ST542_secDisclosures/yescik/{list(clean_dict.keys())[i]}.json","w", encoding='utf8') as new_content:
                                json.dump(new_dict, new_content,ensure_ascii=False, indent=4)
                                print(f"Creating: ../ST542_secDisclosures/yescik/{list(clean_dict.keys())[i]}.json file")
        else:
            continue
 


# Open json file for reading and print content using json.load
for file_name in glob('*.json'):
    #print(file_name) # working with allFilings2021_part1.json
    with open(file_name, encoding='utf-8') as content:
        json_data = json.load(content)
        clean_json_data = clean(json_data)
        #print(clean_json_data)
        clean_json_data
        #print(type(json_data)) class is a dict
        #pprint.pprint(json_data)
    break