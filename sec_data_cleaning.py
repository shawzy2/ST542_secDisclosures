import os
#import pandas as pd
import json
import unicodedata
import pprint
import re
import string
import sec_data_lists
from glob import glob

# non_element = [" ","","— ","•","    ",",",", ",": ",".","$",")","(a)","(b)", "(",
# "                                           ","◦","■","▪"," — ","—","*","%", "®", "® ", "X","†","††", "•",", ",")%",
# ". ","​", " ", " (1)","﻿ "]
non_element = sec_data_lists.non_element
allFilings2021_part1_di_keywords = sec_data_lists.allFilings2021_part1_di_keywords
allFilings2021_part1_di_next_section_keywords = sec_data_lists.allFilings2021_part1_di_next_section_keywords


def clean(d):
    dictionary_data = d
    clean_dict = {}
    #no_hc = {}
    yes_hc = {}
    #new_val = []
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
            new_temp_val3 = []
            temp_val4 = []
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
                    #print(f"Creating: ../ST542_secDisclosures/nocik/{list(no_hc.keys())[i]}.json file") 
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
                    #elif i.strip("%,. ").isdigit():
                    # elif i[0].isdigit() or i[1].isdigit():
                    #     temp_val3.append(i)
                    else:
                        #temp_val2.append(i.strip())
                        temp_val2.append(i)


                # Getting rid of duplicate elements
                for i in temp_val2:
                    if i not in temp_val3:
                        temp_val3.append(i)
                    else:
                        continue

                # for element in temp_val3:
                #     di_list = 
                #     if element in allFilings2021_part1_di_keywords:
                #         print

                        
                # # This will get rid of all numbers
                # for i in temp_val2:
                #     if set(i.lower()) & set(string.ascii_lowercase): 
                #         temp_val3.append(i.strip(" •. :  , ).\n\n; "))
                #     else:
                #         temp_val4.append(i)
                
                # # Getting rid of duplicate elements
                # # The code below for getting rid of duplicate element is not the most efficient
                # # I did try using set, but it would not return the same order
                # for i in temp_val3:
                #     if i not in new_temp_val3:
                #         new_temp_val3.append(i)
                #     else:
                #         continue

                #myset = set(temp_val3)
                #new_temp_val3 = list(myset)
                #print(myset)

                #new_val = new_temp_val3
                new_val = temp_val3
                #no_hc[cik] = no_hc_list
                clean_dict[cik] = new_val
                yes_hc[cik] = "There is Human Capital"

                #di_list = []
                # di_dic = {}
                # di_path = '../ST542_secDisclosures/di'
                # for k,v in clean_dict.items():
                #     for element in v:
                #         #di_list.append(k)
                #         if element in allFilings2021_part1_di_keywords:
                #             di_dic[k] = 'There is a D+I section'
                #             if not os.path.exists(di_path):
                #                 os.makedirs(di_path)
                #             with open(f"../ST542_secDisclosures/di/dic_dic.json","w", encoding='utf8') as new_content:
                #                 json.dump(di_dic, new_content,ensure_ascii=False, indent=4)
                #         #di_list.append(k)
                # #print(di_list)


                for i in range(len(list(clean_dict.keys()))):
                    new_dict = {}
                    new_dict[list(clean_dict.keys())[i]] = list(clean_dict.values())[i]
                    yes_hc_path = '../ST542_secDisclosures/yescik'
                    # di_dic = {}
                    # di_list = []
                    # di_path = '../ST542_secDisclosures/di'
                    for k, v in new_dict.items():
                        if k in list(yes_hc.keys()): 
                            if not os.path.exists(yes_hc_path):
                                os.makedirs(yes_hc_path)
                            with open(f"../ST542_secDisclosures/yescik/{list(clean_dict.keys())[i]}.json","w", encoding='utf8') as new_content:
                                json.dump(new_dict, new_content,ensure_ascii=False, indent=4)


                # Not the best way, but start hard coding
                # my_data_1800_list = clean_dict["1800"]
                # start_index = my_data_1800_list.index("Diversity and Inclusion ")
                # end_index = my_data_1800_list.index("Compensation and Benefits")
                # di_dic = {}
                # di_list = []
                # di_path = '../ST542_secDisclosures/di'
                # for ind in range(start_index+1,end_index):
                #     cik_1800 = my_data_1800_list[ind]
                #     di_list.append(cik_1800)
                #     #print(my_data_1800_list[ind])
                # di_dic["1800"] = di_list
                # if not os.path.exists(di_path):
                #         os.makedirs(di_path)
                # with open(f"../ST542_secDisclosures/di/1800.json","w", encoding='utf8') as new_content:
                #         json.dump(di_dic, new_content,ensure_ascii=False, indent=4)
                # break
                    

                    
                    # for ind in range(start_index+1, end_index):
                    #     print(my_data_list[ind])
                        #for element in v:
                        #for i, element in enumerate(v):
                        #    if element in allFilings2021_part1_di_keywords and element[i+1] in 
                        # n = 1
                        # for i in range(len(v)):
                        #     if v[i] in allFilings2021_part1_di_keywords:
                        #         if v[i+n] in allFilings2021_part1_di_next_section_keywords:
                        #             di_list.append(v[i:i+n])
                        #             di_dic[k] = di_list
                        #             n += 1
                        #         else:
                        #             continue
                                    #di_dic[k] = "Not in the list"
                                    #continue
                            
                        #di_list.append(k)
                            #if element in allFilings2021_part1_di_keywords:

                                #di_dic[k] = 'There is a D+I section'
                                # if not os.path.exists(di_path):
                                #     os.makedirs(di_path)
                                # with open(f"../ST542_secDisclosures/di/{k}.json","w", encoding='utf8') as new_content:
                                #     json.dump(di_dic, new_content,ensure_ascii=False, indent=4)
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
    break # Would need to comment this out for the other json files for part2-6