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
                        #print(len(inner_list))

                        # for end_element in inner_list:
                        #     initial_end_index = inner_value.index(end_element)
                        #     initial_end_element = inner_value[initial_end_index]
                        #     #print(start_element)
                        #     #print(end_element)
                        #     # print(initial_end_element)
                        #     # print(initial_end_index)
                        #     if end_element.isdigit() and len(end_element) <= 2: # this could break if the digit is part of the table
                        #         #print(end_element)
                        #         #print(initial_end_index)
                        #         continue # skipping page number, does not mean getting rid of it yet
                        #     elif initial_end_element in nt_word_list: 
                        #         end_index = my_data_list.index(initial_end_element)
                        #         #print(initial_end_index)
                        #         #print(end_index)

                        #         # print(end_element)
                        #         # print(start_index)
                        #         # print(end_index)
                        #         # break
                        #         for ind in range(start_index+1,end_index):
                        #             if my_data_list[ind].isdigit() and len(my_data_list[ind]) <= 2:
                        #                 continue # This will get rid of the page number
                        #             elif my_data_list[ind] in non_element:
                        #                 continue
                        #             else:
                        #                 #print(my_data_list[ind])
                        #                 di_list.append(my_data_list[ind])
                        #                 #print(di_list)
                        #                 #continue
                        #         break # This break statement is necessary once initial_end_element is found in nt_word_list
                        #     # d/i inside of element:742278
                        #     # Need to take a look at again
                        #     # 732717, 742278
                        #     #print()
                        #     else:
                        #         continue
                                    #print(inner_list_case2)


                        # This should take care of the number at the end or d/is that end with a number
                        # Case1: 766421
                        # Ex: ['D/I', 'D/I Description', '14']
                        # if inner_key == "732834":
                        #     print(inner_list)
                        if len(inner_list) ==0:# 732834
                            for ind in range(len(inner_list_case2)):
                                di_list.append(inner_list_case2[ind])
                        elif len(inner_list) == 1:
                            for ind in range(len(inner_list)):
                                di_list.append(inner_list[ind])
                        elif len(inner_list) !=1: # 732834, 811156'
                            #print(len(inner_list))
                            # Maybe right a condition based off if the last element is a digit
                            if inner_key not in di_v2_keys_s4:
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
                            else:
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

                                # elif initial_end_element not in nt_word_list: 
                                #     end_index = my_data_list.index(initial_end_elementb)
                                #     for ind in range(start_index+1,end_index):
                                #         if my_data_list[ind].isdigit() and len(my_data_list[ind]) <= 2:
                                #             continue # This will get rid of the page number
                                #         elif my_data_list[ind] in non_element:
                                #             continue
                                #         else:
                                #             di_list.append(my_data_list[ind])
                                #     break
                                    #print(initial_end_element)
                                #     end_index = my_data_list.index(initial_end_element)
                                #     for ind in range(start_index+1,end_index):
                                #         if my_data_list[ind].isdigit() and len(my_data_list[ind]) <= 2:
                                #             continue # This will get rid of the page number
                                #         elif my_data_list[ind] in non_element:
                                #             continue
                                #         else:
                                #             di_list.append(my_data_list[ind])
                                #     break # This break statement is necessary once initial_end_element is found in nt_word_list
                                else:
                                    continue


                            
                            # for ind in range(len(inner_list)):
                            #     if inner_list[ind].isdigit() and len(inner_list[ind]) <=2:
                            #         continue
                            #     elif inner_list[ind] in non_element:
                            #         continue
                            #     else:
                            #         di_list.append(inner_list[ind])
                        # Case 2: 732834
                        # Ex: ['D/I', 'D/I Description']
                        # elif len(inner_list_case2) == 1:
                        #     for ind in range(len(inner_list_case2)):
                        #         # if inner_list_case2[ind].isdigit() and len(inner_list_case2[ind]) <=2:
                        #         #     continue
                        #         # elif inner_list_case2[ind] in non_element:
                        #         #     continue
                        #         # else:
                        #         di_list.append(inner_list_case2[ind])
                        #inner_list does print out everyhtin I need
                        #print(inner_list_case2)
                        # Case 3: 811156
                        # elif len(inner_list_case3) != 1:
                        #     for ind in range(len(inner_list_case3)):
                        #         if inner_list_case3[ind].isdigit() and len(inner_list_case3[ind]) <=2:
                        #             continue
                        #         elif inner_list_case3[ind] in non_element:
                        #             continue
                        #         else:
                        #             di_list.append(inner_list_case3[ind])
                        
                        # # Case 3: 811156
                        # if len(inner_list_case3) != 1:
                        #     for ind in range(len(inner_list_case3)):
                        #         if inner_list_case3[ind].isdigit() and len(inner_list_case3[ind]) <=2:
                        #             continue
                        #         elif inner_list_case3[ind] in non_element:
                        #             continue
                        #         else:
                        #             di_list.append(inner_list_case3[ind])
                        #     break
                

                                    

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
                #print(inner_value)
                #continue
            #break # stopping after first iterationr
            inner_json[inner_key] = di_list
            #pprint.pprint(inner_json)
            all_inner_json.update(inner_json)
            #pprint.pprint(all_inner_json)
           # print(inner_json)
            #output_json[key] = all_inner_json
            #pprint.pprint(output_json)
            #print(output_json)
        break
    output_json[key] = all_inner_json
    with open(f"../ST542_secDisclosures/cik_v2/dioutput.json","w", encoding='utf8') as new_content:
        json.dump(output_json, new_content,ensure_ascii=False, indent=4)
        # output_json[key] = inner_json
        # print(output_json)
    #output_json[key] = inner_json
    #pprint.pprint(output_json)

    # key: key_value dict