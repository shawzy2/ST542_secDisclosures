import os
import json
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
        for inner_key, inner_value in value.items():
            inner_json = {}
            my_data_list = inner_value
            di_list = []
            if inner_key in di_keys:
            #if inner_key == "722723": # testing purposes
                for element in inner_value:
                    if element in start_word_list:
                        start_index = my_data_list.index(element)
                        last_index = len(inner_value) - 1 
                        inner_list = inner_value[start_index+1:last_index]
                        for end_element in inner_list:
                            if end_element.isdigit() and len(end_element) == 2:
                                continue # skipping page number, does not mean getting rid of it yet
                            elif end_element in nt_word_list:
                                end_index = my_data_list.index(end_element)
                                #print(end_element)
                                # print(start_index)
                                # print(end_index)
                                for ind in range(start_index+1,end_index):
                                    if my_data_list[ind].isdigit() and len(my_data_list[ind]) == 2:
                                        continue # This will get rid of the page number
                                    else:
                                        print(my_data_list[ind])
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
            elif inner_key in no_di_keys:
                continue
            else:
                continue
            #break # stopping after first iterationr
            inner_json[inner_key] = di_list
           # print(inner_json)
            output_json[key] = inner_json
            #print(output_json)
        break
        # output_json[key] = inner_json
        # print(output_json)