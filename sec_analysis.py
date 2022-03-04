import os
import json
import pandas as pd
import nltk


# This code should combine all of the json files
data = {}

files = ["part1dioutput.json","dioutput.json","allFilings2021_part8.json"]
# Merge all files
#for file in os.listdir("../ST542_secDisclosures/"):
for file in files:
    new_name = f"../ST542_secDisclosures/yescik/di/{file}"
    data.update(json.load(open(new_name, encoding = 'utf-8')))

with open(f"../ST542_secDisclosures/di.json","w", encoding='utf8') as new_content:
    new_content.write(json.dump(data, new_content,ensure_ascii=False, indent=4)) 
