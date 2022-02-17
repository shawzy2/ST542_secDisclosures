import os
#import pandas as pd
import json
import pprint
from glob import glob

def clean(d):
    dictionary_data = d
    clean_dict = {}
    no_hc = {}
    new_val = []
    non_element = [" ","","— ","•","    ",",",", ",": ",".","$",")","(a)","(b)", "(",
    "                                           ","◦","■","▪"," — ","—","*","%"]
    for cik, value_list in dictionary_data.items():
        #print(cik)
        # We would want to strip empty elements, dash elements, elements that have \xa0, percent elements, dot element and period, etc.
        # "4962" is empty list
        if cik == "4962":
            if value_list == []:
                no_hc[cik] = 'There is no Human Capital Disclosure'
            else:
                #break
                #print(cik)
                #if cik == "4447": # Would need to comment this out
                #if cik == "3197": # Would need to comment this out
                #if cik == "3197": # Would need to comment this out
                    #print(cik)
                    #print(type(cik))
                    #print(value_list)
                    #return value_list
                    #########################

                    for element in value_list:
                        if element in non_element:
                        #if element in list(non_element):
                        #while non_element.count(element):
                            # Need to remove element from the value_list
                            value_list.remove(element)
                            new_val.append(value_list)
                            clean_dict[cik] = new_val
                        # elif element.strip('%'):
                        #     new_val.append(value_list)
                        #     clean_dict[cik] = new_val
                        else:
                            new_val.append(value_list)
                            clean_dict[cik] = new_val
                    #print(clean_dict)
                    #########################
                # else:
                #     continue
        else:
            continue


    #testing purposes for no_hc
    # for cik, value_list in no_hc.items():
    #     if cik == "4962":
    #         pprint.pprint(value_list)
    #     else:
    #         continue
    #print(clean_dict)
    #return clean_dict



#test these cik
# 3197
# 3453
# 4447
# 



            # if k == '1800':
            #     print(element)
            #     print("\n")
            # else:
            #     break
        # if k == '1800':
        #     #print(k)
        #     print(v)
        # else:
        #     break


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