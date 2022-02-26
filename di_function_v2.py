import os
import json
import pprint
#import sec_data_lists
import sec_data_listv2
#import sec_functions
from nltk.tokenize import word_tokenize

non_element = sec_data_listv2.non_element
di_keys = sec_data_listv2.di_v2_keys
#dib_keys = sec_data_listv2.di_v2b_keys
no_di_keys = sec_data_listv2.no_di_v2_keys
start_word_list = sec_data_listv2.st_word
nt_word_list = sec_data_listv2.nt_word
i_start_word_list = sec_data_listv2.i_start_word_list
i_nxt_word_list = sec_data_listv2.i_nxt_word_list
di_v2_keys_s4 = sec_data_listv2.di_v2_keys_s4
di_v2_keys_s4b = sec_data_listv2.di_v2_keys_s4b
di_v2_keys_s4c = sec_data_listv2.di_v2_keys_s4c
di_v2_keys_s4d = sec_data_listv2.di_v2_keys_s4d

def filter_di_v2(d):
    d_data = d
    output_json = {}
    all_inner_json = {}
    # key would be part 2-6
    for key, value in d_data.items(): # output_json[key] = dicitonary values or inner_json
        # inner_key is the cik; inner_value is the list
        #inner_data = value.items()
        #inner_json = {}
        '''
        Scenario 1: D/I secion goes past the page number ...kind of done
        Scenario 2: D/I stops at the page number   ... kind of done
        --- Scenario 3 and 4 is a bit harder because there are different variations of it
        Scenario 3: D/I is at the end of the list and stops at the end of the list
        Scenario 4: D/I is part of a string
        '''
        for inner_key, inner_value in value.items():
            inner_json = {}
            my_data_list = inner_value
            di_list = []
            inner_combined_data = ",".join(my_data_list)
            word_list = word_tokenize(inner_combined_data)
            #sub_list =[]
            test_word_list = word_list
            if inner_key in di_keys:
            #if inner_key == "722723": # testing purposes
                for element in inner_value:
                    # By creating the initial_ variables, this should hopefully resolve if more than one element appears in sec_Data_listv2
                    initial_start_index = inner_value.index(element)
                    start_element = inner_value[initial_start_index]
                    if start_element in start_word_list: 
                        start_index = my_data_list.index(element)
                        #print(initial_start_index)
                        #print(start_index)
                        last_index = len(inner_value) - 1 
                        last_index_case2 = len(inner_value)
                        inner_list = inner_value[start_index+1:last_index]
                        inner_list_case2 = inner_value[start_index+1:last_index_case2]
                        inner_list_case3 = inner_value[start_index+1:last_index_case2+1]
                        #print(inner_list_case2)
                        #print(inner_list_case3)
                        #print(len(inner_list_case3))
                        #print(len(inner_list))          #inner_list[last_index]
                        # if inner_key == "860731":
                        #     print(inner_list_case2)
                        #     print(len(inner_list_case2))

                        if len(inner_list) ==0:# 732834, 850460
                            #print(inner_key)
                            for ind in range(len(inner_list_case2)):
                                di_list.append(inner_list_case2[ind])
                        elif len(inner_list) == 1:#766421, 860731
                            #print(inner_key)
                            if inner_key in di_v2_keys_s4c:
                                last_index = len(inner_value) 
                                inner_list = inner_value[start_index+1:last_index]
                                #print(inner_list)
                                for ind in range(len(inner_list)):
                                    di_list.append(inner_list[ind])
                            else:
                                for ind in range(len(inner_list)):
                                    di_list.append(inner_list[ind])
                        # elif len(inner_list) == 2: # 823768, 831259
                        #     #print(inner_key)
                        elif len(inner_list) >=1: # 
                            #print(len(inner_list))
                            # Maybe right a condition based off if the last element is a digit
                            #print(inner_key)
                            if inner_key not in di_v2_keys_s4 and inner_key not in di_v2_keys_s4b :#and inner_key not in di_v2_keys_s4c:
                                #print(inner_key)
                                if inner_key in di_v2_keys_s4d: #867773
                                    #print(inner_key)
                                    #print(inner_list)
                                    sub_list =[]
                                    #print(len(inner_list)) # 12
                                    #print(inner_list[11])
                                    for i in inner_list:
                                        if i.isdigit() and len(i) <= 2:
                                            continue
                                        sub_list.append(i)
                                    #print(sub_list)
                                    new_sub_list = []
                                    nt_word_sub_list = []
                                    for j in sub_list:
                                        if j in nt_word_list: # This broke because I added a new term in nt_word_list
                                            nt_word_sub_list.append(j)
                                            new_sub_list.append(j)
                                            #for k in nt_word_sub_list:
                                        elif j not in nt_word_list:
                                            new_sub_list.append(j)
                                        else:
                                            continue
                                    print(new_sub_list)
                                    #print(nt_word_sub_list[-1])
                                    new_sub_list2 = []
                                    for k in new_sub_list:
                                        if k == nt_word_sub_list[-1]:
                                            new_sub_list2.append(k)
                                        elif k not in nt_word_sub_list:
                                            new_sub_list2.append(k)
                                        else:
                                            continue
                                    #print(new_sub_list2)
                                    # if j in nt_word_sub_list[-1]:
                                    #         new_sub_list.append(j)
                                    #         print(j)
                                    #     else:
                                    #         continue
                                    #print(new_sub_list)

                                    for z in new_sub_list2:
                                        initial_end_index = inner_value.index(z)
                                        initial_end_element = inner_value[initial_end_index]
                                        if z in nt_word_list:
                                            #print(z)
                                            end_index = my_data_list.index(initial_end_element)
                                            for ind in range(start_index+1,end_index):
                                                if my_data_list[ind].isdigit() and len(my_data_list[ind]) <= 2:
                                                    continue # This will get rid of the page number
                                                elif my_data_list[ind] in nt_word_list:
                                                    continue
                                                elif my_data_list[ind] in non_element: # for 867773, it got rid of table of contents
                                                    continue
                                                else:
                                                    di_list.append(my_data_list[ind])
                                            break
                                    print(di_list)

                                else:
                                    for end_element in inner_list:
                                        initial_end_index = inner_value.index(end_element)
                                        initial_end_element = inner_value[initial_end_index]
                                        if end_element.isdigit() and len(end_element) <= 2: # this could break if the digit is part of the table
                                            continue # skipping page number, does not mean getting rid of it yet
                                        elif end_element in nt_word_list: 
                                            end_index = my_data_list.index(initial_end_element)
                                            for ind in range(start_index+1,end_index):
                                                if my_data_list[ind].isdigit() and len(my_data_list[ind]) <= 2:
                                                    continue # This will get rid of the page number
                                                elif my_data_list[ind] in non_element:
                                                    continue
                                                else:
                                                    di_list.append(my_data_list[ind])
                                            break # This break statement is necessary once initial_end_element is found in nt_word_list
                            elif inner_key in di_v2_keys_s4b:# and inner_key not in di_v2_keys_s4:# and inner_key not in di_v2_keys_s4c:
                                #print(inner_key)
                                for end_element in inner_list:
                                    initial_end_index = inner_value.index(end_element)
                                    initial_end_element = inner_value[initial_end_index]
                                    if end_element.isdigit() and len(end_element) == 3: # this could break if the digit is part of the table
                                        continue # skipping page number, does not mean getting rid of it yet
                                    elif end_element in nt_word_list: 
                                        end_index = my_data_list.index(initial_end_element)
                                        for ind in range(start_index+1,end_index):
                                            if my_data_list[ind].isdigit() and len(my_data_list[ind]) == 3:
                                                continue # This will get rid of the page number
                                            elif my_data_list[ind] in non_element:
                                                continue
                                            else:
                                                di_list.append(my_data_list[ind])
                                        break # This break statement is necessary once initial_end_element is found in nt_word_list  
                            #elif inner_key in di_v2_keys_s4c and inner_key not in di_v2_keys_s4b and inner_key not in di_v2_keys_s4:
                                #print(inner_key)
                                # last_index_case = len(inner_value)
                                # inner_list = inner_value[start_index+1:last_index]
                                # for ind in range(len(inner_list_case2)):
                                #     di_list.append(inner_list_case2[ind])
                                # break
                                # for end_element in inner_list_case2:
                                #     initial_end_index = inner_value.index(end_element)
                                #     initial_end_element = inner_value[initial_end_index]
                                #     if end_element.isdigit() and len(end_element) <=2: # this could break if the digit is part of the table
                                #         continue # skipping page number, does not mean getting rid of it yet
                                #     elif end_element not in nt_word_list: 
                                #         end_index = my_data_list.index(initial_end_element)
                                #         for ind in range(start_index+1,end_index+1):
                                #             if my_data_list[ind].isdigit() and len(my_data_list[ind]) <=2:
                                #                 continue # This will get rid of the page number
                                #             elif my_data_list[ind] in non_element:
                                #                 continue
                                #             else:
                                #                 di_list.append(my_data_list[ind])
                                #         break # This break statement is necessary once initial_end_element is found in nt_word_list                          
                            else:
                                #print(inner_key)
                                # This is for '811156'
                                #print(inner_list[-1])
                                end_element = inner_list[-1]
                                initial_end_index = inner_list.index(inner_list[-1])
                                initial_end_element = inner_list[initial_end_index]
                                if end_element.isdigit() and len(end_element) <= 2: # this could break if the digit is part of the table
                                    continue # skipping page number, does not mean getting rid of it yet
                                elif end_element not in nt_word_list: 
                                    end_index = my_data_list.index(initial_end_element)
                                    for ind in range(start_index+1,end_index+1):
                                        if my_data_list[ind].isdigit() and len(my_data_list[ind]) <= 2:
                                            continue # This will get rid of the page number
                                        elif my_data_list[ind] in non_element:
                                            continue
                                        else:
                                            di_list.append(my_data_list[ind])
                                    break # This break statement is necessary once initial_end_element is found in nt_word_list

                                else:
                                    continue
                

                                    

            #elif inner_key in no_di_keys:
            elif inner_key not in di_keys: # This could be for testing purposes, would be more efficient
                #di_list.append("No D+I")
                continue
            else:
                if inner_value == "There is no Human Capital Disclosure":
                    #print(inner_value)
                    #di_list.append(inner_value)
                    
                    
                    continue
                else:
                    #di_list.append("Working on it")
                    continue
            inner_json[inner_key] = di_list
            #pprint.pprint(inner_json)
            all_inner_json.update(inner_json)

        break
    output_json[key] = all_inner_json
    with open(f"../ST542_secDisclosures/cik_v2/dioutput.json","w", encoding='utf8') as new_content:
        new_content.write(json.dump(output_json, new_content,ensure_ascii=False, indent=4))
