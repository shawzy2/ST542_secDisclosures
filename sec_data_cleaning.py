import os
#import pandas as pd
import json
import unicodedata
import pprint
from glob import glob

def clean(d):
    dictionary_data = d
    clean_dict = {}
    no_hc = {}
    #new_val = []
    non_element = [" ","","— ","•","    ",",",", ",": ",".","$",")","(a)","(b)", "(",
    "                                           ","◦","■","▪"," — ","—","*","%", "®", "® ", "X","†","††", "•",", ",")%"]

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
            temp_val3 = []
            temp_val4 = []
            temp_val5 = []
            if value_list == []:
                no_hc[cik] = 'There is no Human Capital Disclosure'
            else:
                #########################

                for element in value_list:
                    #if element in non_element:
                    if element not in non_element:
                        temp_val.append(element)
                for i in temp_val:
                    if '\xa0' in i:
                        temp_val2.append(i.replace('\xa0',''))
                    elif '\u2019' in i:
                        #iencode = i.encode("ascii", "ignore")
                        #idecode = iencode.decode()
                        #idecode = iencode.decode("utf-8", "ignore")
                        #idecode = i.decode("utf-8")
                        #temp_val2.append(idecode)
                        temp_val2.append(i.replace(u'\u2019',''))
                    else:
                        temp_val2.append(i)
                for i in temp_val2:
                    if i=='':
                        temp_val3.append(i)
                    else:
                        temp_val4.append(i)
                        #print(temp_val)
                #new_val = temp_val
                # for i in temp_val:
                #     if i in unicode_element:
                #         temp_val2.append(i.replace(u'{i}',''))
                #     else:
                #         temp_val2.append(i)
                # for i in temp_val2:
                #     if "" not in i:
                #         temp_val3.append(i)
                    # else:
                    #     temp_val2.append(i)
                    # if '\xa0' in i:
                    #     temp_val2.append(i.replace('\xa0',''))
                    # #elif '\u200b' in i: # This worked
                    # for i in unicode_element:
                    # #elif i in unicode_element:
                    #     #temp_val2.append(i.replace('\u200b',''))
                    #     temp_val3.append(i)
                    # else:
                    #     temp_val2.append(i)

                #for i in 
                new_val = temp_val4

                clean_dict[cik] = new_val
                #print(list(clean_dict.keys())[0])
                #########################
        else:
            continue
    #print(list(clean_dict.values())[0])
    #print(len(list(clean_dict.keys())))
    #print(len(list(clean_dict.values())))
    #new_dict = {}
    for i in range(len(list(clean_dict.keys()))):
    #for i in range(2):
        new_dict = {}
        #print(f"Processing: {list(clean_dict.keys())[i]}")
        #print(type(list(clean_dict.keys())[i])) # class is a string
        new_dict[list(clean_dict.keys())[i]] = list(clean_dict.values())[i]
        #print(new_dict)
        with open(f"{list(clean_dict.keys())[i]}.json","w") as new_content:
            json.dump(new_dict,new_content)
            print(f"Creating: {list(clean_dict.keys())[i]}.json file")
        break
        # with open(f"{list(clean_dict.keys())[i]}.json","w") as new_content:
        #     json.dump(list(clean_dict.keys())[i], new_content)
        #     print(f"Creating: {list(clean_dict.keys())[i]}.json file")
        # for cik in clean_dict.keys():
        #     print(f"Processing{cik}")
        # pprint.pprint(clean_dict)
    # for key, value in clean_dict.items():
    #     with open(f"{key}.json","w") as new_content:
    #         json.dump(clean_dict, new_content)
    #         print(f"Creating: {key}.json file")


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