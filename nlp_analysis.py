import os
import json
import pandas as pd
import nltk
import textstat
import pprint
import occurance_of_metrics
from nltk.tokenize import word_tokenize

non_element = [" ","","— ","•","    ",",",", ",": ",".","$",")","(a)","(b)", "(",
"                                           ","◦","■","▪"," — ","—","*","%", "®", "® ", "X","†","††", "•",", ",")%",
". ","​", " ", " (1)","﻿ ",""," —","–","-2-","I-12"," ","•13","**","\n\n\n\n\n \n\nGoldmanSachs2020Form 10-K\n\n5    ",
"\n\n13\n\n\n\n\n","\n13\n\n","25 ",":","Page 9", "):","on-going",
"_______________","- 11 -"," - "," 17","- 12 -","\n\n13\n\n\n\nTable of Contents\n\n","\n13\n","\nTable of Contents\n",
".  ","” below.","” above.","“","”)","(continued)","-10-","","-19-","-22-",
"__________________________________________________","o","     |     20", ",", "?",".","!","(",")"]

def lexical_diversity(text):
    return len(set(text)) / len(text)
def di_stat(d):
    dictionary_data = d
    #1. how many words in di
    #2. does it have a table
    #3. Lexical diversity (LD) is considered to be an important indicator of how complex and difficult to read a text is.

    summary_list = []
    value2= []
    all_cik_v2 = {}
    #print(dictionary_data.keys())
    for key,value in dictionary_data.items():
        print(key)
        # key is "allFilings2021_part1.json"
        # value is a dictionary
        all_cik = {}
        new_dict = {}
        for sub_key, sub_value in value.items():
            # sub_key is now cik
            # sub_value is a di_section that is in a list form
            new_value = ",".join(sub_value)
            new_dict[sub_key] = new_value
        #print(new_dict) # This is going through part 1-part 8
        part_di = {}
        for sub_key2, sub_value2 in new_dict.items():
            #print(type(sub_value2))
            cik_di = {}
            summary_dict = {}
            word_list = word_tokenize(sub_value2)
            #print(type(word_list))
            new_word_list = []
            for i in word_list:
                if i not in non_element:
                    new_word_list.append(i)
                else:
                    continue
            len_of_word_list = len(new_word_list)
            #reading_difficulty = lexical_diversity(sub_value2)
            metric_in_di = occurance_of_metrics.is_metric_in_di_section(sub_value2)
            sub_value2_tuple = (sub_value2) # -> ("Diveristy and et.c")
            fog_index = textstat.gunning_fog(sub_value2_tuple)
            if "tables" in word_list:# This might not be that accurate
                table_bool = 1
            else:
                table_bool = 0

            summary_dict["elements_num"] = len_of_word_list
            #summary_dict["reading_score"] = reading_difficulty # the higher it is, the more complex
            summary_dict["Gunning Fog Index"] = fog_index # the higher it is, the more complex
            summary_dict["table_present"] = table_bool
            summary_dict["metric_in_di"] = metric_in_di
            #pprint.pprint(summary_dict)
            #print(summary_dict)
            
            cik_di[sub_key2] = summary_dict
            #print(cik_di) # THis seemse to be fine
        #     #print(cik_di)
        #     #print(cik_di)
            part_di.update(cik_di)
            #print(part_di) # This is good as well
        #     #print(part_di)
            all_cik[key]=part_di
            #print(all_cik) # This is good as well
            all_cik_v2.update(all_cik)
            #print(all_cik_v2) # This is good as well
        #     #all_cik.update(part_di)
        #     #all_cik.update(cik_di)
        #     #pprint.pprint(all_cik)
    with open(f"../ST542_secDisclosures/dianalysis.json","w", encoding='utf8') as new_content:
        new_content.write(json.dump(all_cik_v2, new_content,ensure_ascii=False, indent=4)) 
    # all_cik_v2.update(all_cik)
    #pprint.pprint(all_cik_v2)

    #return cik_di
    #return new_content