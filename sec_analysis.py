import os
import json
import pandas as pd
import nltk
import nlp_analysis
import textstat

di_stat = nlp_analysis.di_stat
# # # # This code should combine all of the json files
# data = {}
# #data_dict = {}
# files = ["part1dioutput.json","dioutput.json","allFilings2021_part8.json","missedCIKsExtra.json"]
# # Merge all files
# for file in files:
#     new_name = f"../ST542_secDisclosures/{file}"
#     data.update(json.load(open(new_name, encoding = 'utf-8')))
# #data_dict.update(data)
# with open(f"../ST542_secDisclosures/di.json","w", encoding='utf8') as new_content:
#     new_content.write(json.dump(data, new_content,ensure_ascii=False, indent=4)) 


# #NLP Analysis
di_file = "di.json"
#if di_file  in os.listdir("../ST542_secDisclosures/"):
    #print("TRUE")
di_file_dic = {}
new_di_file = f"../ST542_secDisclosures/{di_file}"
with open(new_di_file, encoding='utf-8') as content:
    json_data = json.load(content)
    di_stat_data = di_stat(json_data)
    #print(type(di_stat_data))
    #print(type(di_stat_data))
    di_stat_data
    #print(di_stat_data)
    # di_file_dic[di_file] = di_stat_data


# Converting to dataframe
# di_df = pd.read_json('../ST542_secDisclosures/dianalysis.json', orient='index')
# di_df.to_csv('../ST542_secDisclosures/di_data.csv') 
# print(di_df)

# di_file2 = "dianalysis.json"
# new_di_file2 = f"../ST542_secDisclosures/{di_file2}"
# with open(new_di_file2) as content:
#     json_data = json.load(content)
#     di_df =pd.DataFrame.from_dict(json_data,orient='index')
    
# #     print(di_df.head())
#     di_df.to_csv('../ST542_secDisclosures/di_data.csv')  
# #     # di_stat_data = di_stat(json_data)
# #     # di_stat_data
