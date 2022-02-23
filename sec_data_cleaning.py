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
                            else:
                               # if f"../ST542_secDisclosures/nocik/{list(no_hc.keys())[i]}.json" in no_hc_path:
                                if os.path.isfile(f"../ST542_secDisclosures/nocik/{list(no_hc.keys())[i]}.json"):
                                    #print("skipping")
                                    continue
                                else:
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
                            else:
                                if os.path.isfile(f"../ST542_secDisclosures/yescik/{list(clean_dict.keys())[i]}.json"):
                                #f"../ST542_secDisclosures/yescik/{list(clean_dict.keys())[i]}.json" in yes_hc_path:
                                    #print("skipping")
                                    # for json_file in os.listdir("../ST542_secDisclosures/yescik/"):
                                    #     print(json_file)
                                        
                                    continue
                                else:
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
        #clean_json_data

        #print(clean_json_data)
        #clean_json_data
        #filter_di_data
        #print(type(json_data)) class is a dict
        #pprint.pprint(json_data)
    break # Would need to comment this out for the other json files for part2-6

# This will look into the yescik directory:

di_keys = ["1800","2488","3453",
"3570","4281","4447",
"701288",
"701374","702165","702513",
"704415","708821","708955",
"712034","712534","713676",
"714310","717423","718877"]
no_di_keys= ["2098","2178","3197",
"701347","703604","704440",
"704532","706129","707179",
"708781","709005","709337",
"711669","711772","712537",
"714395","715072","715787",
"715957","716006","716634",
"717538","717605","717806",
"718937","719220","719413"]
def filter_di(d):
    dictionary_data = d
    di_path = "../ST542_secDisclosures/yescik/di/"
    no_di_path = "../ST542_secDisclosures/yescik/nodi/"
    #new_json = {}
    for key, value in dictionary_data.items():
        new_json = {}
        new_no_di_json = {}
        my_data_list = dictionary_data[key]
        di_list = []
        temp_val = []
        #no_di_list = []
        if key in di_keys:
            if key == "1800":
                start_index = my_data_list.index("Diversity and Inclusion ")
                end_index = my_data_list.index("5")
                for ind in range(start_index+1,end_index):
                    di_list.append(my_data_list[ind])
            elif key == "2488":
                start_index = my_data_list.index("Belonging and Inclusion")
                end_index = my_data_list.index("Total Rewards")
                for ind in range(start_index+1,end_index):
                    di_list.append(my_data_list[ind])
            elif key == "3453":
                start_index = my_data_list.index("Diversity, Equity and Inclusion:")
                end_index = my_data_list.index("Total Rewards Programs:")
                for ind in range(start_index+1,end_index):
                    di_list.append(my_data_list[ind])
            elif key == "3570":
                start_index = my_data_list.index("Diversity and Inclusion")
                end_index = my_data_list.index("Development and Training")
                for ind in range(start_index+1,end_index):
                    di_list.append(my_data_list[ind])
            elif key == "4281":
                start_index = my_data_list.index("Diversity, Equity and Inclusion")
                end_index = my_data_list.index("Health and Safety")
                for ind in range(start_index+1,end_index):
                    di_list.append(my_data_list[ind])
            elif key == "4447":
                start_index = my_data_list.index("Inclusion, Diversity and Equity")
                end_index = my_data_list.index("Reward Programs")
                for ind in range(start_index+1,end_index):
                    di_list.append(my_data_list[ind])
            elif key == "701288": # Similar to 702165
                di_list.append(my_data_list[13:14])
            elif key == "701374":
                start_index = my_data_list.index("Diversity and Inclusion")
                end_index = my_data_list.index("Employee Development")
                for ind in range(start_index+1,end_index+1):
                    di_list.append(my_data_list[ind])
            elif key == "702165": # similar to 708955"; Not sure why this has a dash element
                start_index = my_data_list.index("Diversity, Equity and Inclusion")
                end_index = my_data_list.index( "To underscore our commitment to cultivating a workplace experience where the unique experiences, perspectives, and contributions of all our people are valued, our senior management team recently signed a pledge reaffirming our commitment to diversity, equity, and inclusion.  To advance that commitment, senior leaders from across the company serve on an Inclusion Leadership Council, which is accountable for setting our enterprise inclusion strategy and articulating measurable goals and actions needed to achieve them.  ")
                for ind in range(start_index+1,end_index+1):
                    di_list.append(my_data_list[ind])
            elif key == "702513":
                start_index = my_data_list.index("Diversity and Inclusion")
                end_index = my_data_list.index("Fair Wages and Benefits")
                for ind in range(start_index+1,end_index):
                    di_list.append(my_data_list[ind])
            elif key == "704415":
                start_index = my_data_list.index("Diversity and Inclusion")
                end_index = my_data_list.index("Employee Engagement")
                for ind in range(start_index+1,end_index):
                    di_list.append(my_data_list[ind])
            elif key == "708821":
                start_index = my_data_list.index("Diversity and Inclusion")
                end_index = my_data_list.index("Employee Engagement: ")
                for ind in range(start_index+1,end_index):
                    di_list.append(my_data_list[ind])
            elif key == "708955": #Note: This had it at the end and the section was included inside of the elemnt
                start_index = my_data_list.index( "Employee Engagement. First Financial launched its engagement initiative in 2020, partnering with a third party to measure associate engagement and develop action plans for continued improvement.  In 2020, we hosted virtual town hall meetings for all associates, opening the lines of communications and answering associate concerns. In conjunction with the town hall meetings, pulse surveys were completed with themes around wellbeing, return to work, diversity and inclusion, and career coaching and development.  These surveys provided insight into our associates’ needs and desires, which we can use in future program development. ")
                end_index = my_data_list.index("Diversity, Equity and Inclusion. First Financial prioritizes diversity, equity and inclusion (DEI) as an employer, a financial institution and as a member of the communities in which we operate.  The DEI Committee of the Board provides guidance and oversight to First Financial’s executive committee, the Manager of Diversity, Equity and Inclusion, and the First Financial Diversity Council, which is comprised of 10 associates from across our footprint.  First Financial supports several associate-led business resource groups designed to facilitate networking and leadership development.  First Financial is in the process of building its DEI strategy which includes establishing goals for increased associate and management diversity.  During 2020, First Financial’s CEO held a series of listening sessions with diverse associates as part of our goal to foster a more inclusive environment.  ")
                for ind in range(start_index+1,end_index+1):
                    di_list.append(my_data_list[ind])
            elif key == "712034":
                start_index = my_data_list.index("Diversity and Inclusion")
                end_index = my_data_list.index("5")
                for ind in range(start_index+1,end_index):
                    di_list.append(my_data_list[ind])
            elif key == "712534":
                start_index = my_data_list.index("Diversity Equity and Inclusion")
                end_index = my_data_list.index("Talent Assessment, Succession Planning and Career Path")
                for ind in range(start_index+1,end_index):
                    di_list.append(my_data_list[ind])
            elif key == "713676":
                start_index = my_data_list.index("Diversity, equity and inclusion")
                end_index = my_data_list.index("Total rewards")
                for ind in range(start_index+1,end_index):
                    di_list.append(my_data_list[ind])
            elif key == "714310":
                start_index = my_data_list.index("Diversity, Equity and Inclusion.")
                end_index = my_data_list.index("Total Rewards.")
                for ind in range(start_index+1,end_index):
                    di_list.append(my_data_list[ind])
            elif key == "717423": 
                start_index = my_data_list.index("Diversity, Equity and Inclusion")
                end_index = my_data_list.index("13")
                for ind in range(start_index+1,end_index):
                    di_list.append(my_data_list[ind])
            elif key == "718877":
                start_index = my_data_list.index("Diversity, Equity, and Inclusion (“DE&I”)")
                end_index = my_data_list.index("Compensation and Benefits")
                for ind in range(start_index+1,end_index):
                    di_list.append(my_data_list[ind])

            for element in di_list:
                if element not in non_element:
                    temp_val.append(element)
            new_json[key] = temp_val
            if not os.path.exists(di_path):
                os.makedirs(di_path)
            else:
                if os.path.isfile(f"../ST542_secDisclosures/yescik/di/{key}.json"):                      
                    continue
                else:
                    with open(f"../ST542_secDisclosures/yescik/di/{key}.json","w", encoding='utf8') as new_content:
                        json.dump(new_json, new_content,ensure_ascii=False, indent=4)

        elif key in no_di_keys:
            #no_di_list.append("No D+I")
            new_no_di_json[key] = "No D+I"

            if not os.path.exists(no_di_path):
                os.makedirs(no_di_path)
            else:
                if os.path.isfile(f"../ST542_secDisclosures/yescik/nodi/{key}.json"):                      
                        continue
                else:
                        with open(f"../ST542_secDisclosures/yescik/nodi/{key}.json","w", encoding='utf8') as new_content:
                            json.dump(new_no_di_json, new_content,ensure_ascii=False, indent=4)
        else:
            continue

            #     for ind in range(new_start_index+1, new_end_index):
            # print(my_data_list[ind])

    #print(dictionary_data)


                    # my_data_1800_list = clean_dict["1800"]
                # start_index = my_data_1800_list.index("Diversity and Inclusion ")
                # end_index = my_data_1800_list.index("Compensation and Benefits")


for json_file in os.listdir("../ST542_secDisclosures/yescik/"):
    with open(file_name, encoding='utf-8') as content:
        json_data = json.load(content)
        filter_di_data = filter_di(json_data)
        filter_di_data

                                    # for json_file in os.listdir("../ST542_secDisclosures/yescik/"):
                                    #     print(json_file)
#for file_name in 