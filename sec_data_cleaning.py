import os
#import pandas as pd
import json
import pprint
from glob import glob

def clean(d):
    dictionary_data = d
    clean_dict = {}
    no_hc = {}
    #new_val = []
    non_element = [" ","","— ","•","    ",",",", ",": ",".","$",")","(a)","(b)", "(",
    "                                           ","◦","■","▪"," — ","—","*","%"]

    #For some odd reason, I could not get rid of %, \xa0
    for cik, value_list in dictionary_data.items():
        #print(cik)
        # We would want to strip empty elements, dash elements, elements that have \xa0, percent elements, dot element and period, etc.
        # "4962" is empty list
        #if cik == "4962":
        #if cik not in clean_dict:
        # Would eventually have to indent this line]
        new_val = []
        temp_val = []
        temp_val2 = []
        temp_val3 = []
        if value_list == []:
            no_hc[cik] = 'There is no Human Capital Disclosure'
        else:
            #break
            #print(cik)
            if cik == "4447": # Would need to comment this out
            #if cik == "3197": # Would need to comment this out
            #if cik == "3453": # Would need to comment this out
                #print(cik)
                #print(type(cik))
                #print(value_list)
                #return value_list
                #########################

                for element in value_list:
                    #if element in non_element:
                    if element not in non_element:
                        temp_val.append(element)
                        #print(temp_val)
                #new_val = temp_val
                for i in temp_val:
                    if '\xa0' in i:
                        temp_val2.append(i.replace('\xa0',''))
                    else:
                        temp_val2.append(i)
                    
                # for i in temp_val:
                #     if u' ' in i:
                #         i_encode = i.encode("ascii","ignore")
                #         i_decode = i_encode.decode()
                #         #new_val.append(i_decode)
                #         temp_val.append(i_decode)
                #         #new_val.append(i.replace(#'\xa0',''))
                #         #new_val.append(i.strip())
                new_val = temp_val2

                    #print(type())
                #print(new_val[11])
                #print(new_val)
                #pprint.pprint(new_val)
                #pprint.pprint(new_val[0])
                #print(type(new_val[0]))
                clean_dict[cik] = new_val
                #print(clean_dict)
                pprint.pprint(clean_dict)
                #########################

    #testing purposes for clean_dict
    # for cik, value_list in clean_dict.items():
    #     if cik == "3197":
    #         pprint.pprint(value_list)
    #     else:
    #         continue





    ### Second cleaning ###
    # clean_dict2 = {}
    # new_val2 = []
    # for cik, value_list in clean_dict.items():
    #     if cik not in clean_dict2:
    #         new_val = []
    #         if 'There is no Human Capital Disclosure' in value_list:
    #             clean_dict2[cik] = 'There is no Human Capital Disclosure'
    #         else:
    #             for element in value_list:# element is a list
    #                 #for element in section:
    #                     #print(type(element))
    #                     #print(element)
    #                 if '\xa0' in element:
    #                     #new_val.append(element.replace("\xa0",""))
    #                     new_val.append(element.remove("\xa0"))
                        
    #                     #new_hc_disc2[key] = new_val
    #                 else:
    #                     new_val.append(element)
    #                     #new_hc_disc2[key] = new_val
    #             clean_dict2[cik] = new_val
    #     else:
    #         continue
    # pprint.pprint(clean_dict2)
    
    #testing purposes for no_hc
    # for cik, value_list in no_hc.items():
    #     if cik == "4962":
    #         pprint.pprint(value_list)
    #     else:
    #         continue
    #print(clean_dict)
    #return clean_dict



#test these cik
# 3197- has \xa0   could think of these as breaking/stopping point
# 3453- has \u200b could think of these as breaking/stopping point
# 4447
# 


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