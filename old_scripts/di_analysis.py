import os
import nltk
#import pandas as pd
import json
from nltk.tokenize import word_tokenize


def lexical_diversity(text):
    return len(set(text)) / len(text)
def di_stat(d):
    dictionary_data = d
    #1. len of di
    #2. how many words in di
    #3. does it have a table
    #4. POsition of the word diversity. see how complex the sentence is->This is now done, and I would need to ask the professor of what he wants
    #5. Lexical diversity (LD) is considered to be an important indicator of how complex and difficult to read a text is.
    new_dict = {}
    summary_dict = {}
    summary_list = []
    value2= []
    for key,value in dictionary_data.items():
        # if len(value) == 1:
        #     new_value = value
        # else:
        new_value = ",".join(value)
        #print(new_value)
        #value2.append(new_value)
    new_dict[key] = new_value
    for key,value in new_dict.items():
        len_of_di = len(value)
        word_list = word_tokenize(new_value)
        len_of_word_list = len(word_list)
        reading_difficulty = lexical_diversity(value)
        #word_list = new_value.split()
        #counts = dict(Counter(word_list))
        #if "following table" in value:# This might need to be changed
        if "table" in value:
            table_bool = 1
        else:
            table_bool = 0
        #print(counts)
        #print(word_list)
        #print(len(word_list))
        #print(value)
    # length_of_di is counting spaces and characters
    # elements_num  is counting elements in word_lists
    summary_dict["length_of_di"] = len_of_di
    summary_dict["elements_num"] = len_of_word_list
    summary_dict["reading_score"] = reading_difficulty # the higher it is, the more complexs
    #summary_dict["word_count"] = counts
    summary_dict["table_present"] = table_bool
    # print("\n")
    # print(f"Processing 100517: {summary_dict}")
    return summary_dict
    #pprint.pprint(summary_dict)
    #print(new_dict.values())
    #pprint.pprint(new_dict)