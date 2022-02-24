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
    yes_hc = {}
    no_hc_path2 = '../ST542_secDisclosures/nocik_v2'
    hc_path2 = '../ST542_secDisclosures/cik_v2'
    #new_val = []
    for cik, value_list in dictionary_data.items():
        if cik not in clean_dict:
            new_val = []
            temp_val = []
            temp_val2 = []
            temp_val3 = []
            new_temp_val3 = []
            temp_val4 = []
            #no_hc = {}
            #no_hc_list = []
            if value_list == []:
                nohc = 'There is no Human Capital Disclosure'
                #no_hc_list.append(nohc)
                #no_hc[cik] = no_hc_list
                no_hc[cik] = nohc
                #no_hc_path2 = '../ST542_secDisclosures/nocik_v2'

                # for i in range(len(list(no_hc.keys()))):
                #     #new_dict2 = {}
                #     new_dict2[list(no_hc.keys())[i]] = list(no_hc.values())[i]
                #     if not os.path.exists(no_hc_path2):
                #         os.makedirs(no_hc_path2)
                #     else:
                #         # if f"../ST542_secDisclosures/nocik/{list(no_hc.keys())[i]}.json" in no_hc_path:
                #         #if os.path.isfile(f"../ST542_secDisclosures/nocik_v2/{list(no_hc.keys())[i]}.json"):
                #         if os.path.isfile(f"../ST542_secDisclosures/nocik_v2/{list(no_hc.keys())[i]}.json"):
                #         #if os.path.isfile(f"../ST542_secDisclosures/nocik_v2/v2.json"):
                #             #print("skipping")
                #             continue
                #         else:
                #             with open(f"../ST542_secDisclosures/nocik_v2/{list(no_hc.keys())[i]}.json","w", encoding='utf8') as new_content:
                #                 json.dump(new_dict2, new_content,ensure_ascii=False, indent=4)
                #pprint.pprint(no_hc)
                #pprint.pprint(no_hc)
                # for i in range(len(list(no_hc.keys()))):
                #     new_dict2 = {}
                #     new_dict2[list(no_hc.keys())[i]] = list(no_hc.values())[i]
                #     no_hc_path2 = '../ST542_secDisclosures/nocik_v2'


                #     if not os.path.exists(no_hc_path2):
                #         os.makedirs(no_hc_path2)
                #     else:
                #         # if f"../ST542_secDisclosures/nocik/{list(no_hc.keys())[i]}.json" in no_hc_path:
                #         #if os.path.isfile(f"../ST542_secDisclosures/nocik_v2/{list(no_hc.keys())[i]}.json"):
                #         #if os.path.isfile(f"../ST542_secDisclosures/nocik_v2/{list(no_hc.keys())[i]}.json"):
                #         if os.path.isfile(f"../ST542_secDisclosures/nocik_v2/v2.json"):
                #             #print("skipping")
                #             continue
                #         else:
                #             with open(f"../ST542_secDisclosures/nocik_v2/v2.json","w", encoding='utf8') as new_content:
                #                 json.dump(no_hc, new_content,ensure_ascii=False, indent=4)

                    # #print(list(no_hc.values())[i])
                    # for k, v in new_dict2.items():
                    #     if k in list(no_hc.keys()):
                    #         if not os.path.exists(no_hc_path2):
                    #             os.makedirs(no_hc_path2)
                    #         else:
                    #            # if f"../ST542_secDisclosures/nocik/{list(no_hc.keys())[i]}.json" in no_hc_path:
                    #             #if os.path.isfile(f"../ST542_secDisclosures/nocik_v2/{list(no_hc.keys())[i]}.json"):
                    #             #if os.path.isfile(f"../ST542_secDisclosures/nocik_v2/{list(no_hc.keys())[i]}.json"):
                    #             if os.path.isfile(f"../ST542_secDisclosures/nocik_v2/v2.json"):
                    #                 #print("skipping")
                    #                 continue
                    #             else:
                    #                 with open(f"../ST542_secDisclosures/nocik_v2/v2.json","w", encoding='utf8') as new_content:
                    #                     json.dump(no_hc, new_content,ensure_ascii=False, indent=4)
                    #                 #print(no_hc)
            else:
                #########################
                continue
                #print("NOt yet")
                # for element in value_list:
                #     #if element in non_element:
                #     if element not in non_element:
                #         temp_val.append(element)

                # for i in temp_val:
                #     if '\xa0' in i:
                #         temp_val2.append(i.replace('\xa0',''))
                #     # elif "​" in i:
                #     #     temp_val
                #     #elif i.strip("%,. ").isdigit():
                #     # elif i[0].isdigit() or i[1].isdigit():
                #     #     temp_val3.append(i)
                #     else:
                #         #temp_val2.append(i.strip())
                #         temp_val2.append(i)


                # # Getting rid of duplicate elements
                # for i in temp_val2:
                #     if i not in temp_val3:
                #         temp_val3.append(i)
                #     else:
                #         continue

                # # for element in temp_val3:
                # #     di_list = 
                # #     if element in allFilings2021_part1_di_keywords:
                # #         print

                # #new_val = new_temp_val3
                # new_val = temp_val3
                # #no_hc[cik] = no_hc_list
                # clean_dict[cik] = new_val
                # yes_hc[cik] = "There is Human Capital"


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
                #                     #print(yes_hc)
        else:
            continue
    #pprint.pprint(no_hc)
    # if not os.path.exists(hc_path2):
    #     os.makedirs(hc_path2)
    # with open(f"../ST542_secDisclosures/cik_v2/v2.json","w", encoding='utf8') as new_content:
    #     json.dump(no_hc, new_content,ensure_ascii=False, indent=4)

    return(no_hc)


# def combine_json(json_name,d):
#     combine_data = {}
#     combine_data[json_name] = d
#     #combine_data

#     hc_path2 = '../ST542_secDisclosures/cik_v2'

#     if not os.path.exists(hc_path2):
#         os.makedirs(hc_path2)
#     with open(f"../ST542_secDisclosures/cik_v2/v2.json","w", encoding='utf8') as new_content:
#         json.dump(combine_data, new_content,ensure_ascii=False, indent=4)