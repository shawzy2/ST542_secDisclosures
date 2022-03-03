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
di_v2_keys_s4d = sec_data_listv2.di_v2_keys_s4d # Asssuming nt_word of the lement is last
di_v2_keys_s4e = sec_data_listv2.di_v2_keys_s4e # Asssuming nt_word of the lement is second to last
di_v2_keys_s4f = sec_data_listv2.di_v2_keys_s4f
di_v2_keys_s4_1 = sec_data_listv2.di_v2_keys_s4_1
di_v2_keys_s4b_1 = sec_data_listv2.di_v2_keys_s4b_1
di_v2_keys_s4_2 = sec_data_listv2.di_v2_keys_s4_2
di_v2_keys_s4_3 = sec_data_listv2.di_v2_keys_s4_3
# all_outer_json = {}
# output_json = {}
#print(di_keys)
def filter_di_v2(d):
    d_data = d
    all_outer_json = {}
    #all_outer_json = {}
    output_json = {}
    #output_json = {}
    #all_inner_json = {}
    # key would be part 2-6
    for key, value in d_data.items(): # output_json[key] = dicitonary values or inner_json
        # inner_key is the cik; inner_value is the list
        #inner_data = value.items()
        #inner_json = {}
        all_inner_json = {}
        #print(key)
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
                #print(inner_key)
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
                        # if inner_key ==  "877212":
                        #     #print(inner_list)
                        #     print(len(inner_list))
                        #     print(len(inner_list_case2))
                        
                        #     print(inner_list_case2)
                        #     print(len(inner_list_case2))
                        #print(inner_key)
                        # if inner_key == "920522":
                        #     print("testing")

                        if len(inner_list) ==0:# 732834, 850460
                            #print(inner_key)
                            for ind in range(len(inner_list_case2)):
                                di_list.append(inner_list_case2[ind])
                        elif len(inner_list) == 1:#766421, 860731
                            #print(inner_key)
                            if inner_key in di_v2_keys_s4c: # "877212"
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
                            if inner_key not in di_v2_keys_s4 and inner_key not in di_v2_keys_s4b and inner_key not in di_v2_keys_s4c:
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
                                    #print(new_sub_list)
                                    #print(nt_word_sub_list[-1])
                                    new_sub_list2 = []
                                    for k in new_sub_list:
                                        if inner_key  not in di_v2_keys_s4e:
                                            if k == nt_word_sub_list[-1]:
                                                new_sub_list2.append(k)
                                            elif k not in nt_word_sub_list:
                                                new_sub_list2.append(k)
                                            else:
                                                continue
                                        else:
                                            #print(inner_key)
                                            # if inner_key == "1060391":
                                            #     print(nt_word_sub_list)
                                            if k == nt_word_sub_list[-2]:
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
                                    if inner_key == "1284812":
                                        #print(inner_key)
                                        last_index = len(inner_value)
                                        inner_list = inner_value[start_index+1:last_index]
                                        #print(inner_list)
                                        end_element = inner_list[6]
                                        #print(inner_list[5])
                                        for z in new_sub_list2:
                                            initial_end_index = inner_list.index(inner_list[6])
                                            initial_end_element = inner_list[initial_end_index]
                                            # initial_end_index = inner_value.index(z)
                                            # initial_end_element = inner_value[initial_end_index]
                                            if z in nt_word_list:  
                                                #print(z)
                                                end_index = my_data_list.index(initial_end_element)
                                                for ind in range(start_index+1,end_index):
                                                    if my_data_list[ind].isdigit() and len(my_data_list[ind]) <= 2:
                                                        continue # This will get rid of the page number
                                                    elif my_data_list[ind] in nt_word_list:
                                                        di_list.append(my_data_list[ind])
                                                        #continue
                                                    elif my_data_list[ind] in non_element: # for 867773, it got rid of table of contents
                                                        continue
                                                    else:
                                                        di_list.append(my_data_list[ind])
                                                #print(di_list)
                                                break
                                    elif inner_key == "923571":
                                        #print(nt_word_sub_list)
                                        for k in new_sub_list:
                                                if k == nt_word_sub_list[-2]:
                                                    new_sub_list2.append(k)
                                                elif k not in nt_word_sub_list:
                                                    new_sub_list2.append(k)
                                                else:
                                                    continue 
                                        # for k in new_sub_list:
                                        #         if k == nt_word_sub_list[-2]:
                                        #             new_sub_list2.append(k)
                                        #         elif k not in nt_word_sub_list:
                                        #             new_sub_list2.append(k)
                                        #         else:
                                        #             continue  
                                    # elif inner_key == "51644":
                                    #     print(nt_word_sub_list)
                                        # for k in new_sub_list:
                                        #         if k == nt_word_sub_list[-2]:
                                        #             new_sub_list2.append(k)
                                        #         elif k not in nt_word_sub_list:
                                        #             new_sub_list2.append(k)
                                        #         else:
                                        #             continue 

                                        last_index = len(inner_value)
                                        inner_list = inner_value[start_index+1:last_index]
                                        #print(inner_list[5])
                                        end_element = inner_list[5]
                                        initial_end_index = inner_list.index(inner_list[5])
                                        initial_end_element = inner_list[initial_end_index]
                                        for z in new_sub_list2:
                                            # initial_end_index = inner_value.index(z)
                                            # initial_end_element = inner_value[initial_end_index]
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
                                    # elif inner_key == "732717":
                                    #     #print(nt_word_sub_list)
                                    #     start_word = "Diversity and Inclusion"
                                    #     start_index = my_data_list.index(start_word)
                                    # elif inner_key == "1514991":
                                    #     print(nt_word_sub_list)
                                        # for k in new_sub_list:
                                        #         if k == nt_word_sub_list[-2]:
                                        #             new_sub_list2.append(k)
                                        #         elif k not in nt_word_sub_list:
                                        #             new_sub_list2.append(k)
                                        #         else:
                                        #             continue  

                                        # last_index = len(inner_value)
                                        # inner_list = inner_value[start_index+1:last_index]
                                        # #print(inner_list[5])
                                        # end_element = inner_list[5]
                                        # initial_end_index = inner_list.index(inner_list[5])
                                        # initial_end_element = inner_list[initial_end_index]
                                        # for z in new_sub_list2:
                                        #     # initial_end_index = inner_value.index(z)
                                        #     # initial_end_element = inner_value[initial_end_index]
                                        #     if z in nt_word_list:
                                        #         #print(z)
                                        #         end_index = my_data_list.index(initial_end_element)
                                        #         for ind in range(start_index+1,end_index):
                                        #             if my_data_list[ind].isdigit() and len(my_data_list[ind]) <= 2:
                                        #                 continue # This will get rid of the page number
                                        #             elif my_data_list[ind] in nt_word_list:
                                        #                 continue
                                        #             elif my_data_list[ind] in non_element: # for 867773, it got rid of table of contents
                                        #                 continue
                                        #             else:
                                        #                 di_list.append(my_data_list[ind])
                                        #         break
                                    else:
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
                                    #print(di_list)
                                elif inner_key == "732717":
                                        #print(nt_word_sub_list)
                                    start_word = "Diversity and Inclusion"
                                    start_index = my_data_list.index(start_word)
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
                                                    #print(f"Processing: {my_data_list[ind]}")
                                                    di_list.append(my_data_list[ind])      
                                            break                                           
                                elif inner_key ==  "1026214":
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
                                                elif my_data_list[ind] in ["Directors, Corporate Governance, and Executive Officers ","– ","Directors –"," Director Criteria, Diversity, Qualifications, Experience, and Tenure"]:
                                                    continue
                                                else:
                                                    #print(f"Processing: {my_data_list[ind]}")
                                                    di_list.append(my_data_list[ind])
                                            break # This break statement is necessary once initial_end_element is found in nt_word_list
                                elif inner_key == "1318568":
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
                                                elif my_data_list[ind] in ["We develop our employees through a variety of means, both internally and externally. We offer a leadership program to provide employees training and related resources in a wide variety of managerial skills topics, such as: conflict management, delegation, talent acquisition, eliminating bias behaviors, employee relations and compliance. In addition, we encourage employees to pursue external education and certification opportunities, many of which are eligible for cost and tuition reimbursement by the Company, to supplement their career development goals."]:
                                                    continue
                                                else:
                                                    #print(f"Processing: {my_data_list[ind]}")
                                                    di_list.append(my_data_list[ind])
                                            break # This break statement is necessary once initial_end_element is found in nt_word_list 
                                elif inner_key == "1437578":
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
                                                elif my_data_list[ind] in [" (2)","(1)", "(2)"]:
                                                    continue
                                                else:
                                                    #print(f"Processing: {my_data_list[ind]}")
                                                    di_list.append(my_data_list[ind])
                                            break # This break statement is necessary once initial_end_element is found in nt_word_list  
                                elif inner_key == "1463172":
                                     for end_element in inner_list:
                                        initial_end_index = inner_value.index(end_element)
                                        initial_end_element = inner_value[initial_end_index]
                                        if end_element.isdigit() and len(end_element) <= 2: # this could break if the digit is part of the table
                                            continue # skipping page number, does not mean getting rid of it yet
                                        elif end_element in nt_word_list: 
                                            end_index = my_data_list.index(initial_end_element)
                                            for ind in range(start_index+1,end_index):
                                                # if my_data_list[ind].isdigit() and len(my_data_list[ind]) <= 2:
                                                #     continue # This will get rid of the page number
                                                if my_data_list[ind] in non_element:
                                                    continue
                                                elif my_data_list[ind] in ["12"]:
                                                    continue
                                                else:
                                                    #print(f"Processing: {my_data_list[ind]}")
                                                    di_list.append(my_data_list[ind])
                                            break # This break statement is necessary once initial_end_element is found in nt_word_list   
                                elif inner_key == "1493225":
                                    end_element = "Training and Development."
                                    #print(inner_key)
                                    
                                     #for end_element in inner_list:
                                    initial_end_index = inner_value.index(end_element)
                                    initial_end_element = inner_value[initial_end_index]
                                    #print(inner_value[:initial_end_index])
                                    #print(my_data_list[start_index:initial_end_index+1])
                                    # if end_element.isdigit() and len(end_element) <= 2: # this could break if the digit is part of the table
                                    #     continue # skipping page number, does not mean getting rid of it yet
                                    if end_element in nt_word_list: 
                                        end_index = my_data_list.index(initial_end_element)
                                        for ind in range(start_index+1,end_index+1):
                                            #print(my_data_list[ind])
                                            if my_data_list[ind].isdigit() and len(my_data_list[ind]) <= 2:
                                                continue # This will get rid of the page number
                                            elif my_data_list[ind] in non_element:
                                                continue
                                            elif my_data_list[ind] in nt_word_list:
                                                continue
                                            # elif my_data_list[ind] in ["12"]:
                                            #     continue
                                            else:
                                                #print(f"Processing: {my_data_list[ind]}")
                                                di_list.append(my_data_list[ind])
                                        #print(di_list)
                                        break # This break statement is necessary once initial_end_element is found in nt_word_list    
                                elif inner_key == "1595974":
                                    end_element = "Talent Retention"
                                    #print(inner_key)
                                    
                                     #for end_element in inner_list:
                                    initial_end_index = inner_value.index(end_element)
                                    initial_end_element = inner_value[initial_end_index]
                                    #print(inner_value[:initial_end_index])
                                    #print(my_data_list[start_index:initial_end_index+1])
                                    # if end_element.isdigit() and len(end_element) <= 2: # this could break if the digit is part of the table
                                    #     continue # skipping page number, does not mean getting rid of it yet
                                    if end_element in nt_word_list: 
                                        end_index = my_data_list.index(initial_end_element)
                                        for ind in range(start_index+1,end_index+1):
                                            #print(my_data_list[ind])
                                            if my_data_list[ind].isdigit() and len(my_data_list[ind]) <= 2:
                                                continue # This will get rid of the page number
                                            elif my_data_list[ind] in non_element:
                                                continue
                                            elif my_data_list[ind] ==  " Equity and Inclusion":
                                                continue
                                            elif my_data_list[ind] in nt_word_list:
                                                continue
                                            # elif my_data_list[ind] in ["12"]:
                                            #     continue
                                            else:
                                                #print(f"Processing: {my_data_list[ind]}")
                                                di_list.append(my_data_list[ind])
                                        #print(di_list)
                                        break # This break statement is necessary once initial_end_element is found in nt_word_list   
                                elif inner_key == "1770450":
                                    end_element = "Talent Management and Workforce Development"
                                    initial_end_index = inner_value.index(end_element)
                                    initial_end_element = inner_value[initial_end_index]
                                    if end_element in nt_word_list: 
                                        end_index = my_data_list.index(initial_end_element)
                                        for ind in range(start_index+1,end_index+1):
                                            #print(my_data_list[ind])
                                            if my_data_list[ind].isdigit() and len(my_data_list[ind]) <= 2:
                                                continue # This will get rid of the page number
                                            elif my_data_list[ind] in non_element:
                                                continue
                                            elif my_data_list[ind] ==  "Community Outreach":
                                                di_list.append(my_data_list[ind])
                                            elif my_data_list[ind] == "Talent Management and Workforce Development":
                                                continue
                                            # elif my_data_list[ind] in ["12"]:
                                            #     continue
                                            else:
                                                #print(f"Processing: {my_data_list[ind]}")
                                                di_list.append(my_data_list[ind])
                                        #print(di_list)
                                        break # This break statement is necessary once initial_end_element is found in nt_word_list                                  
                                # elif inner_key == "1636286":
                                #     end_element = "Compensation, Benefits, Wellness"
                                #     #print(inner_key)
                                    
                                #      #for end_element in inner_list:
                                #     initial_end_index = inner_value.index(end_element)
                                #     initial_end_element = inner_value[initial_end_index]
                                #     #print(inner_value[:initial_end_index])
                                #     #print(my_data_list[start_index:initial_end_index+1])
                                #     # if end_element.isdigit() and len(end_element) <= 2: # this could break if the digit is part of the table
                                #     #     continue # skipping page number, does not mean getting rid of it yet
                                #     if end_element in nt_word_list: 
                                #         end_index = my_data_list.index(initial_end_element)
                                #         for ind in range(start_index+1,end_index+1):
                                #             #print(my_data_list[ind])
                                #             if my_data_list[ind].isdigit() and len(my_data_list[ind]) <= 2:
                                #                 continue # This will get rid of the page number
                                #             elif my_data_list[ind] in non_element:
                                #                 continue
                                #             elif my_data_list[ind] ==  "Core Values":
                                #                 di_list.append(my_data_list[ind])
                                #             elif my_data_list[ind] == "Compensation, Benefits, Wellness":
                                #                 continue
                                #             # elif my_data_list[ind] in nt_word_list:
                                #             #     continue
                                #             # elif my_data_list[ind] in ["12"]:
                                #             #     continue
                                #             else:
                                #                 #print(f"Processing: {my_data_list[ind]}")
                                #                 di_list.append(my_data_list[ind])
                                #         #print(di_list)
                                #         break # This break statement is necessary once initial_end_element is found in nt_word_list                                                             
                                # elif inner_key == "1333986":
                                #     start_word = "Diversity and Inclusion"
                                #     start_index = my_data_list.index(start_word)
                                #     initial_end_index = inner_value.index(3)
                                #     initial_end_element = inner_value[3]
                                #     for end_element in inner_list:
                                #         if end_element.isdigit() and len(end_element) <= 2: # this could break if the digit is part of the table
                                #             continue # skipping page number, does not mean getting rid of it yet
                                #         elif end_element in nt_word_list: 
                                #             end_index = my_data_list.index(initial_end_element)
                                #             for ind in range(start_index+1,end_index):
                                #                 if my_data_list[ind].isdigit() and len(my_data_list[ind]) <= 2:
                                #                     continue # This will get rid of the page number
                                #                 elif my_data_list[ind] in non_element:
                                #                     continue
                                #                 else:
                                #                     #print(f"Processing: {my_data_list[ind]}")
                                #                     di_list.append(my_data_list[ind])
                                #             break # This break statement is necessary once initial_end_element is found in nt_word_list                                                                  

                                else:
                                    if inner_key not in di_v2_keys_s4e:
                                        # if inner_key == "917520":
                                        #     print(inner_key)
                                        if inner_key in di_v2_keys_s4_2:
                                            #print(inner_key)
                                            last_index = len(inner_value)
                                            inner_list = inner_value[start_index+1:last_index]
                                            #print(inner_list)
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
                                                    elif my_data_list[ind] in nt_word_list:
                                                        continue
                                                    else:
                                                        di_list.append(my_data_list[ind])
                                                break # This break statement is necessary once initial_end_element is found in nt_word_list
                                        elif inner_key in di_v2_keys_s4_3: # This should be like its own separate key
                                            #print(inner_key)
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
                                            z = sub_list[-1]
                                            #for z in sub_list:
                                            initial_end_index = inner_value.index(z)
                                            initial_end_element = inner_value[initial_end_index]
                                            # if z in nt_word_list:
                                            #     #print(z)
                                            end_index = my_data_list.index(initial_end_element)
                                            for ind in range(start_index+1,end_index+1):
                                                if my_data_list[ind].isdigit() and len(my_data_list[ind]) <= 2:
                                                    continue # This will get rid of the page number
                                                elif my_data_list[ind] in nt_word_list:
                                                    di_list.append(my_data_list[ind])
                                                elif my_data_list[ind] in non_element: # for 867773, it got rid of table of contents
                                                    continue
                                                else:
                                                    di_list.append(my_data_list[ind])
                                            #print(di_list)
                                            break

                                            # new_sub_list = []
                                            # nt_word_sub_list = []
                                            # for j in sub_list:
                                            #     if j in nt_word_list: # This broke because I added a new term in nt_word_list
                                            #         nt_word_sub_list.append(j)
                                            #         new_sub_list.append(j)
                                            #         #for k in nt_word_sub_list:
                                            #     elif j not in nt_word_list:
                                            #         new_sub_list.append(j)
                                            #     else:
                                            #         continue
                                            # print(new_sub_list)
                                            #print(nt_word_sub_list[-1])
                                            #print(nt_word_sub_list)
                                            # new_sub_list2 = []
                                            # for k in new_sub_list:
                                            #     #if inner_key  not in di_v2_keys_s4e:
                                            #     if k == nt_word_sub_list[-1]:
                                            #         new_sub_list2.append(k)
                                            #     elif k not in nt_word_sub_list:
                                            #         new_sub_list2.append(k)
                                            #     else:
                                            #         continue
                                                # else:
                                                #     #print(inner_key)
                                                #     # if inner_key == "1060391":
                                                #     #     print(nt_word_sub_list)
                                                #     if k == nt_word_sub_list[-2]:
                                                #         new_sub_list2.append(k)
                                                #     elif k not in nt_word_sub_list:
                                                #         new_sub_list2.append(k)
                                                #     else:
                                                #         continue        
                                            #print(new_sub_list2)
                                            # if j in nt_word_sub_list[-1]:
                                            #         new_sub_list.append(j)
                                            #         print(j)
                                            #     else:
                                            #         continue
                                            #print(new_sub_list)
                                        else:
                                            #print(inner_key)
                                            if inner_key == "1333986":
                                                #print(inner_key)
                                                start_word = "Diversity and Inclusion"
                                                start_index = my_data_list.index(start_word)
                                                #print(my_data_list[start_index])
                                                #print(inner_value[15:18])
                                                #end_word = ""
                                                # initial_end_index = inner_value.index(end_element)
                                                # initial_end_element = inner_value[initial_end_index]
                                                # #testing_index = inner_value.index(initial_end_element)
                                                # testing_element = inner_value[17]
                                                # #print(testing_index)
                                                # print(testing_element)
                                                #print(inner_list[12])
                                                end_word = "Equitable Foundation"
                                                end_index =  my_data_list.index(end_word)
                                                # for end_element in inner_list[9:12]:
                                                #     initial_end_index = inner_value.index(end_element)
                                                #     initial_end_element = inner_value[initial_end_index]
                                                if end_word.isdigit() and len(end_word) <= 2: # this could break if the digit is part of the table
                                                    continue # skipping page number, does not mean getting rid of it yet
                                                # elif end_word in nt_word_list: 
                                                #     end_index = my_data_list.index(initial_end_element)
                                                for ind in range(start_index+1,end_index):
                                                    if my_data_list[ind].isdigit() and len(my_data_list[ind]) <= 2:
                                                        continue # This will get rid of the page number
                                                    elif my_data_list[ind] in non_element:
                                                        continue
                                                    elif my_data_list[ind] in nt_word_list:
                                                        continue
                                                    else:
                                                        #print(f"Processing: {my_data_list[ind]}")
                                                        di_list.append(my_data_list[ind])
                                                #print(di_list)
                                                break # This break statement is necessary once initial_end_element is found in nt_word_list


                                            elif inner_key == "1361658":
                                                start_word =  "Inclusion and Diversity"
                                                start_index = my_data_list.index(start_word) 
                                                end_word = "Competitive Pay/Benefits"
                                                end_index =  my_data_list.index(end_word)

                                                if end_word.isdigit() and len(end_word) <= 2: # this could break if the digit is part of the table
                                                    continue # skipping page number, does not mean getting rid of it yet
                                                # elif end_word in nt_word_list: 
                                                #     end_index = my_data_list.index(initial_end_element)
                                                for ind in range(start_index+1,end_index):
                                                    if my_data_list[ind].isdigit() and len(my_data_list[ind]) <= 2:
                                                        continue # This will get rid of the page number
                                                    elif my_data_list[ind] in non_element:
                                                        continue
                                                    elif my_data_list[ind] in nt_word_list:
                                                        continue
                                                    else:
                                                        #print(f"Processing: {my_data_list[ind]}")
                                                        di_list.append(my_data_list[ind])
                                                #print(di_list)
                                                break # This break statement is necessary once initial_end_element is found in nt_word_list
                                            elif inner_key == "1580608":
                                                start_word =  "Diversity, Equity and Inclusion "
                                                start_index = my_data_list.index(start_word) 
                                                end_word = "Compensation and Benefits"
                                                end_index =  my_data_list.index(end_word)

                                                if end_word.isdigit() and len(end_word) <= 2: # this could break if the digit is part of the table
                                                    continue # skipping page number, does not mean getting rid of it yet
                                                # elif end_word in nt_word_list: 
                                                #     end_index = my_data_list.index(initial_end_element)
                                                for ind in range(start_index+1,end_index):
                                                    if my_data_list[ind].isdigit() and len(my_data_list[ind]) <= 2:
                                                        continue # This will get rid of the page number
                                                    elif my_data_list[ind] in non_element:
                                                        continue
                                                    elif my_data_list[ind] in nt_word_list:
                                                        continue
                                                    else:
                                                        #print(f"Processing: {my_data_list[ind]}")
                                                        di_list.append(my_data_list[ind])
                                                #print(di_list)
                                                break # This break statement is necessary once initial_end_element is found in nt_word_list                                           
                                            else:
                                                for end_element in inner_list:
                                                    initial_end_index = inner_value.index(end_element)
                                                    initial_end_element = inner_value[initial_end_index]
                                                    if end_element.isdigit() and len(end_element) <= 2: # this could break if the digit is part of the table
                                                        continue # skipping page number, does not mean getting rid of it yet
                                                    elif end_element in nt_word_list: 
                                                        end_index = my_data_list.index(initial_end_element)
                                                        #print(end_element)
                                                        for ind in range(start_index+1,end_index):
                                                            if my_data_list[ind].isdigit() and len(my_data_list[ind]) <= 2:
                                                                continue # This will get rid of the page number
                                                            # elif my_data_list[ind] in nt_word_list:
                                                            #     continue
                                                            elif my_data_list[ind] in non_element:
                                                                continue
                                                            else:
                                                                di_list.append(my_data_list[ind])
                                                        break # This break statement is necessary once initial_end_element is found in nt_word_list
                                        # elif inner_key in di_v2_keys_s4_3:
                                        #     print(inner_key)
                                            #print(inner_list)
                                            # sub_list =[]
                                            # #print(len(inner_list)) # 12
                                            # #print(inner_list[11])
                                            # for i in inner_list:
                                            #     if i.isdigit() and len(i) <= 2:
                                            #         continue
                                            #     sub_list.append(i)
                                            # #print(sub_list)
                                            # new_sub_list = []
                                            # nt_word_sub_list = []
                                            # for j in sub_list:
                                            #     if j in nt_word_list: # This broke because I added a new term in nt_word_list
                                            #         nt_word_sub_list.append(j)
                                            #         new_sub_list.append(j)
                                            #         #for k in nt_word_sub_list:
                                            #     elif j not in nt_word_list:
                                            #         new_sub_list.append(j)
                                            #     else:
                                            #         continue
                                            # #print(new_sub_list)
                                            # #print(nt_word_sub_list[-1])
                                            # new_sub_list2 = []
                                            # for k in new_sub_list:
                                            #     #if inner_key  not in di_v2_keys_s4e:
                                            #     if k == nt_word_sub_list[-1]:
                                            #         new_sub_list2.append(k)
                                            #     elif k not in nt_word_sub_list:
                                            #         new_sub_list2.append(k)
                                            #     else:
                                            #         continue
                                            #     # else:
                                            #     #     #print(inner_key)
                                            #     #     # if inner_key == "1060391":
                                            #     #     #     print(nt_word_sub_list)
                                            #     #     if k == nt_word_sub_list[-2]:
                                            #     #         new_sub_list2.append(k)
                                            #     #     elif k not in nt_word_sub_list:
                                            #     #         new_sub_list2.append(k)
                                            #     #     else:
                                            #     #         continue        
                                            # #print(new_sub_list2)
                                            # # if j in nt_word_sub_list[-1]:
                                            # #         new_sub_list.append(j)
                                            # #         print(j)
                                            # #     else:
                                            # #         continue
                                            # print(new_sub_list)

                                            # for z in new_sub_list2:
                                            #     initial_end_index = inner_value.index(z)
                                            #     initial_end_element = inner_value[initial_end_index]
                                            #     if z in nt_word_list:
                                            #         #print(z)
                                            #         end_index = my_data_list.index(initial_end_element)
                                            #         for ind in range(start_index+1,end_index):
                                            #             if my_data_list[ind].isdigit() and len(my_data_list[ind]) <= 2:
                                            #                 continue # This will get rid of the page number
                                            #             elif my_data_list[ind] in nt_word_list:
                                            #                 continue
                                            #             elif my_data_list[ind] in non_element: # for 867773, it got rid of table of contents
                                            #                 continue
                                            #             else:
                                            #                 di_list.append(my_data_list[ind])
                                            #         break
                                            #     else:
                                            #         for end_element in inner_list:
                                            #             initial_end_index = inner_value.index(end_element)
                                            #             initial_end_element = inner_value[initial_end_index]
                                            #             if end_element.isdigit() and len(end_element) <= 2: # this could break if the digit is part of the table
                                            #                 continue # skipping page number, does not mean getting rid of it yet
                                            #             elif end_element in nt_word_list: 
                                            #                 end_index = my_data_list.index(initial_end_element)
                                            #                 #print(end_element)
                                            #                 for ind in range(start_index+1,end_index):
                                            #                     if my_data_list[ind].isdigit() and len(my_data_list[ind]) <= 2:
                                            #                         continue # This will get rid of the page number
                                            #                     # elif my_data_list[ind] in nt_word_list:
                                            #                     #     continue
                                            #                     elif my_data_list[ind] in non_element:
                                            #                         continue
                                            #                     else:
                                            #                         di_list.append(my_data_list[ind])
                                            #                 break # This break statement is necessary once initial_end_element is found in nt_word_list
                                    else:
                                        #print(inner_key)
                                        sub_list =[]
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
                                        #print(new_sub_list)
                                        # if inner_key == "872589":
                                        #     print(nt_word_sub_list)
                                        #     #print(nt_word_sub_list[-1])
                                        new_sub_list2 = []
                                        for k in new_sub_list:
                                            if inner_key  not in di_v2_keys_s4e:
                                                if k == nt_word_sub_list[-1]:
                                                    new_sub_list2.append(k)
                                                elif k not in nt_word_sub_list:
                                                    new_sub_list2.append(k)
                                                else:
                                                    continue
                                            else:
                                                #print(inner_key)
                                                # if inner_key == "1278027":
                                                #     print(nt_word_sub_list)
                                                if inner_key == "872589" or inner_key == "1067701" or inner_key == "1082554" or inner_key == "1084961" or inner_key == "1090012" or inner_key == "1109546" or inner_key == "1158324" or inner_key =="1163739" or inner_key == "1212545" or inner_key == "1232524" or inner_key == "1278027" or inner_key == "1281761" or inner_key == "1298675" or inner_key == "1310114" or inner_key == "1324404" or inner_key == "1324424" or inner_key == "1337619" or inner_key == "1355096" or inner_key == "1370450" or inner_key == "1373715" or inner_key == "1388658" or inner_key == "1401521" or inner_key == "1411494" or inner_key == "1418135" or inner_key == "1437402" or inner_key == "1459417" or inner_key == "1467858" or inner_key == "1475841" or inner_key == "1513761" or inner_key == "1519061" or inner_key == "1521036" or inner_key == "1521332" or inner_key == "1535929" or inner_key == "1560327" or inner_key == "1576940" or inner_key == "1587523" or inner_key == "1669779" or inner_key == "1679688" or inner_key == "1699150" or inner_key == "1718512" or inner_key == "1739445" or inner_key == "1792044" or inner_key == "6201" or inner_key == "790051" or inner_key == "813672" or inner_key == "816761" or inner_key == "875045" or inner_key == "887596":
                                                    if k == nt_word_sub_list[1]:
                                                        new_sub_list2.append(k)
                                                    elif k not in nt_word_sub_list:
                                                        new_sub_list2.append(k)
                                                    else:
                                                        continue 
                                                # elif inner_key == "1437402":
                                                #     if k == nt_word_sub_list[1]:
                                                #         new_sub_list2.append(k)
                                                #     elif k not in nt_word_sub_list and k!="Fostering and maintaining a strong, healthy culture is a key strategic focus. Our core values reflect who we are and the way our employees interact with one another, our partners and our stockholders. We are dedicated to our core values, recognizing that this dedication will foster an environment where we will be able to realize our vision of creating a healthier tomorrow for patients with kidney and cardiovascular disease. We are Passionate, aware that with integrity and determination, we make a difference for patients. We are Fearless, aware that by challenging convention, we truly innovate. We are Dedicated, aware that working tirelessly together, we are greater than the sum of our parts. We are Inclusive, aware that with respect, grace and humor, we are family. We encourage our employees to live out our core values and to discuss our core values with potential candidates looking to join our team. We believe that this is an important step in helping our culture stay strong and unique. ":
                                                #         new_sub_list2.append(k)
                                                #     # elif k == "Fostering and maintaining a strong, healthy culture is a key strategic focus. Our core values reflect who we are and the way our employees interact with one another, our partners and our stockholders. We are dedicated to our core values, recognizing that this dedication will foster an environment where we will be able to realize our vision of creating a healthier tomorrow for patients with kidney and cardiovascular disease. We are Passionate, aware that with integrity and determination, we make a difference for patients. We are Fearless, aware that by challenging convention, we truly innovate. We are Dedicated, aware that working tirelessly together, we are greater than the sum of our parts. We are Inclusive, aware that with respect, grace and humor, we are family. We encourage our employees to live out our core values and to discuss our core values with potential candidates looking to join our team. We believe that this is an important step in helping our culture stay strong and unique. ":
                                                #     #     new_sub_list2.append(k)
                                                #     else:
                                                #         continue                                                    
                                                elif inner_key == "1424929":
                                                    #print(nt_word_sub_list)
                                                    if k == nt_word_sub_list[0]:
                                                        new_sub_list2.append(k)
                                                    elif k not in nt_word_sub_list:
                                                        new_sub_list2.append(k)
                                                    else:
                                                        continue 
                                                elif inner_key == "1603923":
                                                    if k == nt_word_sub_list[1]:
                                                        new_sub_list2.append(k)
                                                    elif k not in nt_word_sub_list:
                                                        new_sub_list2.append(k)
                                                    else:
                                                        continue 
                                                    #print(nt_word_sub_list)
                                                elif inner_key == "1497770":
                                                    #print(nt_word_sub_list)
                                                    if k == nt_word_sub_list[-1]:
                                                        new_sub_list2.append(k)
                                                    elif k not in nt_word_sub_list:
                                                        new_sub_list2.append(k)
                                                    else:
                                                        continue
                                                elif inner_key == "1514705":
                                                    #print(nt_word_sub_list)
                                                    if k == nt_word_sub_list[1]:
                                                        new_sub_list2.append(k)
                                                    elif k not in nt_word_sub_list:
                                                        new_sub_list2.append(k)
                                                    else:
                                                        continue                                                                            
                                                # elif inner_key == "1082554":
                                                #     print(nt_word_sub_list)
                                                # elif inner_key ==  "1067701":
                                                #     #print(nt_word_sub_list)
                                                #     if k == nt_word_sub_list[0]:
                                                #         new_sub_list2.append(k)
                                                #     elif k not in nt_word_sub_list:
                                                #         new_sub_list2.append(k)
                                                #     else:
                                                #         continue                                                   
                                                else:
                                                    if k == nt_word_sub_list[-2]: # this code is flawed
                                                        new_sub_list2.append(k)
                                                    elif k not in nt_word_sub_list:
                                                        new_sub_list2.append(k)
                                                    else:
                                                        continue 

                                        if inner_key == "1437402":
                                            #new_sub_list2.remove("Fostering and maintaining a strong, healthy culture is a key strategic focus. Our core values reflect who we are and the way our employees interact with one another, our partners and our stockholders. We are dedicated to our core values, recognizing that this dedication will foster an environment where we will be able to realize our vision of creating a healthier tomorrow for patients with kidney and cardiovascular disease. We are Passionate, aware that with integrity and determination, we make a difference for patients. We are Fearless, aware that by challenging convention, we truly innovate. We are Dedicated, aware that working tirelessly together, we are greater than the sum of our parts. We are Inclusive, aware that with respect, grace and humor, we are family. We encourage our employees to live out our core values and to discuss our core values with potential candidates looking to join our team. We believe that this is an important step in helping our culture stay strong and unique. ")
                                            #print(new_sub_list2[0:2])
                                            new_sub_list2b = new_sub_list2[0:4] # this only works for 1437402
                                            for z in new_sub_list2b:
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
                                                        elif my_data_list[ind] == "Fostering and maintaining a strong, healthy culture is a key strategic focus. Our core values reflect who we are and the way our employees interact with one another, our partners and our stockholders. We are dedicated to our core values, recognizing that this dedication will foster an environment where we will be able to realize our vision of creating a healthier tomorrow for patients with kidney and cardiovascular disease. We are Passionate, aware that with integrity and determination, we make a difference for patients. We are Fearless, aware that by challenging convention, we truly innovate. We are Dedicated, aware that working tirelessly together, we are greater than the sum of our parts. We are Inclusive, aware that with respect, grace and humor, we are family. We encourage our employees to live out our core values and to discuss our core values with potential candidates looking to join our team. We believe that this is an important step in helping our culture stay strong and unique. ":
                                                            continue
                                                        elif my_data_list[ind] in non_element: # for 867773, it got rid of table of contents
                                                            continue
                                                        else:
                                                            di_list.append(my_data_list[ind])
                                                    #print(di_list)
                                                    break
                                        elif inner_key == "1514705":
                                             for z in new_sub_list2:
                                                initial_end_index = inner_value.index(z)
                                                initial_end_element = inner_value[initial_end_index]
                                                if z in nt_word_list:
                                                    #print(z)
                                                    end_index = my_data_list.index(initial_end_element)
                                                    for ind in range(start_index+1,end_index):
                                                        # if my_data_list[ind].isdigit() and len(my_data_list[ind]) <= 2:
                                                        #     continue # This will get rid of the page number
                                                        if my_data_list[ind] in nt_word_list:
                                                            continue
                                                        elif my_data_list[ind] in non_element: # for 867773, it got rid of table of contents
                                                            continue
                                                        elif my_data_list[ind] in ["6","7"]:
                                                            continue
                                                        else:
                                                            di_list.append(my_data_list[ind])
                                                    break                                                                    
                                        else:
                                            # if inner_key == "1497770":
                                            #     print(new_sub_list2)
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
                                        # if inner_key == "1278027":
                                        #     print(di_list)


                            elif inner_key in di_v2_keys_s4b:# and inner_key not in di_v2_keys_s4:# and inner_key not in di_v2_keys_s4c:
                                #print(inner_key)
                                if inner_key not in di_v2_keys_s4b_1:
                                    #print(inner_key)
                                    if inner_key == "827052":
                                        sub_list =[]
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
                                        #print(new_sub_list)
                                        # if inner_key == "872589":
                                        #     print(nt_word_sub_list)
                                        #     #print(nt_word_sub_list[-1])
                                        # if inner_key ==  "827052":
                                        #print(nt_word_sub_list)
                                        new_sub_list2 = []
                                        for k in new_sub_list:
                                            #if inner_key  not in di_v2_keys_s4e:
                                            if k == nt_word_sub_list[-1]:
                                                new_sub_list2.append(k)
                                            # elif k == nt_word_sub_list[0]:
                                            #     continue
                                            elif k not in nt_word_sub_list:
                                                new_sub_list2.append(k)
                                            else:
                                                continue
                                        #print(new_sub_list2)
                                        for z in new_sub_list2:
                                            if z in nt_word_list:
                                                #print(z)
                                                initial_end_index = inner_value.index(z)
                                                initial_end_element = inner_value[initial_end_index]
                                                end_index = my_data_list.index(initial_end_element)
                                                for ind in range(start_index+1,end_index):
                                                    if my_data_list[ind].isdigit() and len(my_data_list[ind]) <= 3:
                                                        continue # This will get rid of the page number
                                                    elif my_data_list[ind] in nt_word_list:
                                                        continue
                                                    elif my_data_list[ind] in non_element: # for 867773, it got rid of table of contents
                                                        continue
                                                    else:
                                                        di_list.append(my_data_list[ind])
                                                break   
                                        #print(di_list)

                                        # for end_element in inner_list:
                                        #     initial_end_index = inner_value.index(end_element)
                                        #     initial_end_element = inner_value[initial_end_index]
                                        #     if end_element.isdigit() and len(end_element) == 3: # this could break if the digit is part of the table
                                        #         continue # skipping page number, does not mean getting rid of it yet
                                        #     elif end_element in nt_word_list: 
                                        #         end_index = my_data_list.index(initial_end_element)
                                        #         for ind in range(start_index+1,end_index):
                                        #             if my_data_list[ind].isdigit() and len(my_data_list[ind]) == 3:
                                        #                 continue # This will get rid of the page number
                                        #             elif my_data_list[ind] in non_element:
                                        #                 continue
                                        #             else:
                                        #                 di_list.append(my_data_list[ind])
                                        #         break # This break statement is necessary once initial_end_element is found in nt_word_list 
                                    # elif inner_key == "1552033":
                                    #     print(inner_key)
                                    elif inner_key == "1552033":
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
                                                    elif my_data_list[ind] == "18":
                                                        continue
                                                    elif my_data_list[ind] in non_element:
                                                        continue
                                                    else:
                                                        di_list.append(my_data_list[ind])
                                                break # This break statement is necessary once initial_end_element is found in nt_word_list
                                    elif inner_key == "1562401":
                                        #for end_element in inner_list[:-4]:
                                        #end_element = inner_value[:-4]
                                        end_element = inner_list[-4]
                                        initial_end_index = inner_value.index(end_element)
                                        initial_end_element = inner_value[initial_end_index]
                                        #print(initial_end_element)
                                        #print(inner_value[:-4])
                                        #print(inner_list[-4])
                                        if end_element.isdigit() and len(end_element) == 3: # this could break if the digit is part of the table
                                            continue # skipping page number, does not mean getting rid of it yet
                                        elif end_element in nt_word_list: 
                                            end_index = my_data_list.index(initial_end_element)
                                            for ind in range(start_index+1,end_index+1):
                                                if my_data_list[ind].isdigit() and len(my_data_list[ind]) == 3:
                                                    continue # This will get rid of the page number
                                                elif my_data_list[ind] == "Employees":
                                                    di_list.append(my_data_list[ind])
                                                elif my_data_list[ind] in ["6", "Training and Development"]:
                                                    continue
                                                elif my_data_list[ind] in non_element:
                                                    continue
                                                else:
                                                    di_list.append(my_data_list[ind])
                                            #print(di_list)
                                                #print(my_data_list[ind])
                                            break # This break statement is necessary once initial_end_element is found in nt_word_list  
                                    elif inner_key == "1614184":
                                        #for end_element in inner_list[:-4]:
                                        #end_element = inner_value[:-4]
                                        #print(inner_list[76])
                                        end_element = inner_list[76]
                                        initial_end_index = inner_value.index(end_element)
                                        initial_end_element = inner_value[initial_end_index]
                                        # #print(initial_end_element)
                                        # #print(inner_value[:-4])
                                        # #print(inner_list[-4])
                                        if end_element.isdigit() and len(end_element) == 3: # this could break if the digit is part of the table
                                            continue # skipping page number, does not mean getting rid of it yet
                                        elif end_element in nt_word_list: 
                                            end_index = my_data_list.index(initial_end_element)
                                            for ind in range(start_index+1,end_index+1):
                                                if my_data_list[ind].isdigit() and len(my_data_list[ind]) > 3:
                                                    continue # This will get rid of the page number
                                                # elif my_data_list[ind] == "Employees":
                                                #     di_list.append(my_data_list[ind])
                                                # elif my_data_list[ind] in ["6", "Training and Development"]:
                                                #     continue
                                                elif my_data_list[ind] in non_element:
                                                    continue
                                                elif my_data_list[ind]=="17":
                                                    continue
                                                else:
                                                    di_list.append(my_data_list[ind])
                                            #print(di_list)
                                                #print(my_data_list[ind])
                                            break # This break statement is necessary once initial_end_element is found in nt_word_list 
                                    elif inner_key == "1681459":
                                        #print(inner_list[49])
                                        end_element = inner_list[49]
                                        initial_end_index = inner_value.index(end_element)
                                        initial_end_element = inner_value[initial_end_index]
                                        if end_element.isdigit() and len(end_element) == 3: # this could break if the digit is part of the table
                                            continue # skipping page number, does not mean getting rid of it yet
                                        elif end_element in nt_word_list: 
                                            end_index = my_data_list.index(initial_end_element)
                                            for ind in range(start_index+1,end_index+1):
                                                if my_data_list[ind].isdigit() and len(my_data_list[ind]) > 3:
                                                    continue # This will get rid of the page number
                                                # elif my_data_list[ind] == "Employees":
                                                #     di_list.append(my_data_list[ind])
                                                # elif my_data_list[ind] in ["6", "Training and Development"]:
                                                #     continue
                                                elif my_data_list[ind] in non_element:
                                                    continue
                                                elif my_data_list[ind]=="23" or my_data_list[ind] == "Employee and Social Matters":
                                                    continue
                                                else:
                                                    di_list.append(my_data_list[ind])
                                            #print(di_list)
                                                #print(my_data_list[ind])
                                            break # This break statement is necessary once initial_end_element is found in nt_word_list 
                                    else:
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
                                else:
                                #     print("testing")
                                    #print(inner_key)
                                    sub_list =[]
                                    #print(len(inner_list)) # 12
                                    #print(inner_list[11])
                                    for i in inner_list:
                                        if i.isdigit() and len(i) == 1:
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
                                    #print(new_sub_list)
                                    #print(nt_word_sub_list)
                                    #print(nt_word_sub_list[-1])
                                    new_sub_list2 = []
                                    for k in new_sub_list:
                                        #if inner_key  not in di_v2_keys_s4e: # THis mihgth have to change later
                                        if k == nt_word_sub_list[1]: # This code wiill break if for a new cik, the position is different
                                            new_sub_list2.append(k)
                                        elif k not in nt_word_sub_list:
                                            new_sub_list2.append(k)
                                        else:
                                            continue

                                    for z in new_sub_list2:
                                        initial_end_index = inner_value.index(z)
                                        initial_end_element = inner_value[initial_end_index]
                                        if z in nt_word_list:
                                            #print(z)
                                            end_index = my_data_list.index(initial_end_element)
                                            for ind in range(start_index+1,end_index):
                                                if my_data_list[ind].isdigit() and len(my_data_list[ind]) == 1:
                                                    continue # This will get rid of the page number
                                                elif my_data_list[ind] in nt_word_list:
                                                    continue
                                                elif my_data_list[ind] in non_element: # for 867773, it got rid of table of contents
                                                    continue
                                                else:
                                                    di_list.append(my_data_list[ind])
                                            break

                            # elif inner_key in di_v2_keys_s4c:
                            #     print(inner_key)
                            # elif inner_key in di_v2_keys_s4f:
                            #     print(inner_key)
                         
                            else:
                                #print(inner_key)
                                # This is for '811156'
                                #print(inner_list[-1])
                                # if inner_key == "877212":
                                #     print(inner_value)
                                if inner_key not in di_v2_keys_s4f:
                                    #print(inner_key)
                                    if inner_key not in di_v2_keys_s4_1:
                                        end_element = inner_list[-1]
                                        initial_end_index = inner_list.index(inner_list[-1])
                                        initial_end_element = inner_list[initial_end_index]
                                        if end_element.isdigit() and len(end_element) <= 2: # this could break if the digit is part of the table
                                            continue # skipping page number, does not mean getting rid of it yet
                                        elif end_element not in nt_word_list: 
                                            end_index = my_data_list.index(initial_end_element)
                                            for ind in range(start_index+1,end_index+1):
                                                # if inner_key == "1163165":
                                                #     if my_data_list[ind].isdigit() and len(my_data_list[ind]) <= 2:
                                                #         continue # This will get rid of the page number
                                                #     elif my_data_list[ind] in non_element:
                                                #         continue
                                                #     elif my_data_list[ind] == "20 ":
                                                #         continue
                                                #     elif my_data_list[ind] in nt_word_list:
                                                #         continue
                                                #     else:
                                                #         di_list.append(my_data_list[ind])
                                                # else:
                                                if my_data_list[ind].isdigit() and len(my_data_list[ind]) <= 2:
                                                    continue # This will get rid of the page number
                                                elif my_data_list[ind] in non_element:
                                                    continue
                                                elif my_data_list[ind] in nt_word_list:
                                                    continue
                                                else:
                                                    di_list.append(my_data_list[ind])
                                            break # This break statement is necessary once initial_end_element is found in nt_word_list
                                    else:
                                        #print(inner_key)
                                        #print(inner_list)
                                        if inner_key == "1733998":
                                            start_word =  "Diversity, Equity and Inclusion"
                                            start_index = inner_value.index(start_word) 
                                            last_index = len(inner_value)
                                            inner_list = inner_value[start_index+1:last_index]
                                            #print(inner_list)
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
                                                    elif my_data_list[ind] in nt_word_list:
                                                        continue
                                                    else:
                                                        di_list.append(my_data_list[ind])
                                                break # This break statement is necessary once initial_end_element is found in nt_word_list
                                        else:
                                            last_index = len(inner_value)
                                            inner_list = inner_value[start_index+1:last_index]
                                            #print(inner_list)
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
                                                    elif my_data_list[ind] in nt_word_list:
                                                        continue
                                                    else:
                                                        di_list.append(my_data_list[ind])
                                                break # This break statement is necessary once initial_end_element is found in nt_word_list
                                else:
                                    #print(inner_key)
                                    sub_list =[]
                                    for i in inner_value:
                                        if i.isdigit() and len(i) <= 2:
                                            continue
                                        sub_list.append(i)
                                    new_sub_list = []
                                    nt_word_sub_list = []
                                    # if inner_key == "906107":
                                    #     print(inner_value)
                                    for j in sub_list:
                                        if j in nt_word_list: # This broke because I added a new term in nt_word_list
                                            nt_word_sub_list.append(j)
                                            new_sub_list.append(j)
                                            #for k in nt_word_sub_list:
                                        elif j not in nt_word_list:
                                            new_sub_list.append(j)
                                        else:
                                            continue
                                    #print(new_sub_list)
                                    #print(nt_word_sub_list[-2])
                                    #print(nt_word_sub_list)
                                    new_sub_list2 = []
                                    for k in new_sub_list:
                                        #if inner_key  not in di_v2_keys_s4e:
                                        if inner_key not in di_v2_keys_s4f: # this if might need ot be fixed later
                                            if k == nt_word_sub_list[-1]:
                                                new_sub_list2.append(k)
                                            elif k not in nt_word_sub_list:
                                                new_sub_list2.append(k)
                                            else:
                                                continue
                                        elif inner_key == "1467623":
                                            if k == nt_word_sub_list[0]:
                                                new_sub_list2.append(k)
                                            elif k not in nt_word_sub_list:
                                                new_sub_list2.append(k)
                                            else:
                                                continue                                    
                                        else:
                                            if k == nt_word_sub_list[-2] or k ==nt_word_sub_list[-1]: # this is the problem, and could be a problem if more elemnts get added
                                                new_sub_list2.append(k)
                                            elif k not in nt_word_sub_list:
                                                new_sub_list2.append(k)
                                            else:
                                                continue   
                                    #print(new_sub_list2)

                                    #print(len(new_sub_list2))
                                    #print(new_sub_list[20])
                                    #print(inner_value[-1])
                                    # if inner_key == "1467623":
                                    #     print(inner_value)
                                    initial_end_index = inner_value.index(inner_value[-1])
                                    initial_end_element = inner_value[initial_end_index]
                                    end_index = my_data_list.index(initial_end_element)
                                    for z in new_sub_list2:
                                        # initial_end_index = inner_value.index(z)
                                        # initial_end_element = inner_value[initial_end_index]
                                        #print(z)
                                        if z not in nt_word_list:
                                            #print(z)
                                            #end_index = my_data_list.index(initial_end_element)
                                            #print(end_index)
                                            for ind in range(start_index+1,end_index+1):
                                                if my_data_list[ind].isdigit() and len(my_data_list[ind]) <= 2:
                                                    continue # This will get rid of the page number
                                                elif my_data_list[ind] in nt_word_list:
                                                    continue
                                                elif my_data_list[ind] in non_element: # for 867773, it got rid of table of contents
                                                    continue
                                                else:
                                                    di_list.append(my_data_list[ind])
                                            break
                                #print(di_list)




 


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
            all_inner_json.update(inner_json)
            # if inner_key == "1214816":
            #     print(inner_json)

        output_json[key] = all_inner_json

    with open(f"../ST542_secDisclosures/cik_v2/dioutput.json","w", encoding='utf8') as new_content:
        new_content.write(json.dump(output_json, new_content,ensure_ascii=False, indent=4))
