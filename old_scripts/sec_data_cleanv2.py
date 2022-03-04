import os
import json
import sec_data_lists
import pprint
#import sec_functions

non_element = sec_data_lists.non_element
allFilings2021_part1_di_keywords = sec_data_lists.allFilings2021_part1_di_keywords
allFilings2021_part1_di_next_section_keywords = sec_data_lists.allFilings2021_part1_di_next_section_keywords
di_keys = sec_data_lists.di_keys
no_di_keys = sec_data_lists.no_di_keys

def clean_v2(d):
    dictionary_data = d
    clean_dict = {}
    no_hc = {}
    #yes_hc = {}
    hc_path2 = '../ST542_secDisclosures/cik_v2'
    for cik, value_list in dictionary_data.items():
        if cik not in clean_dict:
            new_val = []
            temp_val = []
            temp_val2 = []
            temp_val3 = []
            new_temp_val3 = []
            temp_val4 = []
            if value_list == []:
                nohc = 'There is no Human Capital Disclosure'
                clean_dict[cik] = nohc
            else:
                #########################
                #continue
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

                #new_val = new_temp_val3
                new_val = temp_val3
                #no_hc[cik] = no_hc_list
                clean_dict[cik] = new_val
                #yes_hc[cik] = "There is Human Capital"


                # for i in range(len(list(clean_dict.keys()))):
                #     new_dict = {}
                #     new_dict[list(clean_dict.keys())[i]] = list(clean_dict.values())[i]
                #     yes_hc_path = '../ST542_secDisclosures/yescik_v2'
                #     # di_dic = {}
                #     # di_list = []
                #     # di_path = '../ST542_secDisclosures/di'
                #     for k, v in new_dict.items():
                #         if k in list(yes_hc.keys()): 
                #             if not os.path.exists(yes_hc_path):
                #                 os.makedirs(yes_hc_path)
                #             else:
                #                 #if os.path.isfile(f"../ST542_secDisclosures/yescik_v2/{list(clean_dict.keys())[i]}.json"):
                #                 if os.path.isfile(f"../ST542_secDisclosures/yescik_v2/v2.json"):                                     
                #                     continue
                #                 else:
                #                     with open(f"../ST542_secDisclosures/yescik_v2/v2.json","w", encoding='utf8') as new_content:
                #                         json.dump(clean_dict, new_content,ensure_ascii=False, indent=4)
                                    #print(yes_hc)
        else:
            continue

    return(clean_dict)# This would need to change