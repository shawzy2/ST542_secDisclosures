import os
import json
import pprint
#import sec_data_lists
import sec_data_listv2
#import sec_functions
from nltk.tokenize import word_tokenize

non_element = sec_data_listv2.non_element
di_keys = sec_data_listv2.di_v2_keys
dib_keys = sec_data_listv2.di_v2b_keys
no_di_keys = sec_data_listv2.no_di_v2_keys
start_word_list = sec_data_listv2.st_word
nt_word_list = sec_data_listv2.nt_word
i_start_word_list = sec_data_listv2.i_start_word_list
i_nxt_word_list = sec_data_listv2.i_nxt_word_list

def filter_di_v2(d):
    d_data = d
    output_json = {}
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

                        # This should take care of the number at the end or d/is that end with a number
                        # Case1: 766421
                        # Ex: ['D/I', 'D/I Description', '14']
                        if len(inner_list) == 1:
                            for ind in range(len(inner_list)):
                                di_list.append(inner_list[ind])
                        # Case 2: 732834
                        # Ex: ['D/I', 'D/I Description']
                        if len(inner_list_case2) == 1:
                            for ind in range(len(inner_list_case2)):
                                di_list.append(inner_list_case2[ind])
                        
                        for end_element in inner_list:
                            initial_end_index = inner_value.index(end_element)
                            initial_end_element = inner_value[initial_end_index]
                            #print(start_element)
                            #print(end_element)
                            # print(initial_end_element)
                            # print(initial_end_index)
                            if end_element.isdigit() and len(end_element) <= 2: # this could break if the digit is part of the table
                                #print(end_element)
                                #print(initial_end_index)
                                continue # skipping page number, does not mean getting rid of it yet
                            elif initial_end_element in nt_word_list: 
                                end_index = my_data_list.index(initial_end_element)
                                #print(initial_end_index)
                                #print(end_index)

                                # print(end_element)
                                # print(start_index)
                                # print(end_index)
                                # break
                                for ind in range(start_index+1,end_index):
                                    if my_data_list[ind].isdigit() and len(my_data_list[ind]) <= 2:
                                        continue # This will get rid of the page number
                                    else:
                                        #print(my_data_list[ind])
                                        di_list.append(my_data_list[ind])
                                        #print(di_list)
                                        #continue
                                break # This break statement is necessary once initial_end_element is found in nt_word_list

                            # d/i inside of element:742278
                            # Need to take a look at again
                            # 732717, 742278


                            else:
                                continue
                
                # This ocde chunk below should take of Scenario 3 and 4
                # 732717, 742278
            # elif inner_key in dib_keys:
            #     print(inner_key)
            #     for i_element in word_list:
            #         if i_element in i_start_word_list:
            #             i_start_index = test_word_list.index(i_element)
            #             i_last_index = len(word_list) - 1 
            #             i_inner_list = word_list[i_start_index+1:i_last_index]
            #             print(i_inner_list)
            #             for i_end_element in i_inner_list:
            #                 i_initial_end_index = word_list.index(i_end_element)
            #                 i_initial_end_element = word_list[i_initial_end_index]
            #                 if i_initial_end_element in i_nxt_word_list: 
            #                     i_end_index = test_word_list.index(i_initial_end_element)
            #                     #print(initial_end_index)
            #                     #print(end_index)

            #                     # print(end_element)
            #                     # print(start_index)
            #                     # print(end_index)
            #                     for ind in range(i_start_index+1,i_end_index):
            #                         di_list.append(test_word_list[ind])
            #                     break # This break statement is necessary once initial_end_element is found in nt_word_list

                                    

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
            pprint.pprint(inner_json)
           # print(inner_json)
            output_json[key] = inner_json
            #print(output_json)
        break
        # output_json[key] = inner_json
        # print(output_json)