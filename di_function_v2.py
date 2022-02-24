import os
import json
import pprint
#import sec_data_lists
import sec_data_listv2
#import sec_functions

non_element = sec_data_listv2.non_element
di_keys = sec_data_listv2.di_v2_keys
no_di_keys = sec_data_listv2.no_di_v2_keys
start_word_list = sec_data_listv2.st_word
nt_word_list = sec_data_listv2.nt_word


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
        Scenario 2: D/I stops at the page number
        Scenario 3: D/I is at the end of the list and stops at the end of the list
        Scenario 4: D/I is part of a string
        '''
        for inner_key, inner_value in value.items():
            inner_json = {}
            my_data_list = inner_value
            di_list = []
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
                        #Case1: 766421
                        #Ex: ['D/I', 'D/I Description', '14']
                        # if inner_key == "732834":
                        #     #print(start_index)
                        #     print(inner_list_case2)
                        if len(inner_list) == 1:
                            for ind in range(len(inner_list)):
                                di_list.append(inner_list[ind])
                        # Case 2: 732834
                        #Ex: ['D/I', 'D/I Description']
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
                            # elif initial_end_element not in nt_word_list and initial_end_element.isdigit():
                            #     di_list.append(inner_list)

                            # elif initial_end_element not in nt_word_list: # "732717","732834". most likely take the bottom
                            #     #if inner_key == "732717": # Would have to delete this later
                            # "766421"
                            #         #last_element = inner_value[-1]
                            #         #print(last_element)
                            #         #print("is this working")
                            #     print(inner_key)
                            # elif initial_end_element not in nt_word_list:
                            #     di_list.append("Working in progress")
                            #     break

                            # d/i inside of element:742278

                            else:
                                continue


                        # #print(element)
                        # start_index = my_data_list.index(element)
                        # #print(start_index)
                        # #last_element = inner_value[-1].index
                        # last_index = len(inner_value) - 1 
                        # inner_list = inner_value[start_index+1:last_index]
                        # #new_inner_list = ",".join(inner_list)

                        # #print(start_index)

                        # #break
                        # #for end_element in range(start_index+1,last_index):
                        #     #print(end_element)
                        # #print(inner_list)
                        # #break
                        # for end_element in inner_list:
                        #     if end_element.isdigit() and len(end_element) == 2: # This would break if it kept on talking about diversity
                        #         print(inner_list[1])
                        #         #interest_index = new_inner_list.index(end_element)
                        #         #new_start_index = new_inner_list.index(element)
                        #         # print(new_start_index)
                        #         # print(interest_index)
                        #         #for ind in range(new_start_index,interest_index-2):
                        #         #    print(new_inner_list[ind])
                                    
                        #         # end_index = inner_list.index(end_element)
                        #         # for ind in range(start_index+1,end_index):
                        #         #     di_list.append(inner_list[ind])
                        #     else:
                        #         continue


                        #for ind in range(start_index+1,end_index)


                    # end index could take emtpy strings, other sections, and numbers
                    # the numbers would be harder
                #if inner_key == "722723":

                    # Need to find and stop at first occurance at Diveristy and Inclusion using for loop
                    # Thne it needs to stop at a digit or another section, 
                    # ##if it has no section, then it reads through the end of thfile
                    # like a page bnumber, but it still talked about diversity
                   # break
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