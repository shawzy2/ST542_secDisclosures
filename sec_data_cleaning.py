import os
#import pandas as pd
import json
import unicodedata
import pprint
import re
import string
import sec_data_lists
from glob import glob

# non_element = [" ","","— ","•","    ",",",", ",": ",".","$",")","(a)","(b)", "(",
# "                                           ","◦","■","▪"," — ","—","*","%", "®", "® ", "X","†","††", "•",", ",")%",
# ". ","​", " ", " (1)","﻿ "]
non_element = sec_data_lists.non_element
allFilings2021_part1_di_keywords = sec_data_lists.allFilings2021_part1_di_keywords
allFilings2021_part1_di_next_section_keywords = sec_data_lists.allFilings2021_part1_di_next_section_keywords


def clean(d):
    dictionary_data = d
    clean_dict = {}
    #no_hc = {}
    yes_hc = {}
    #new_val = []
    for cik, value_list in dictionary_data.items():
        #print(cik)
        # We would want to strip empty elements, dash elements, elements that have \xa0, percent elements, dot element and period, etc.
        # "4962" is empty list
        #if cik == "4962":
        if cik not in clean_dict:
        # Would eventually have to indent this line]
            new_val = []
            temp_val = []
            temp_val2 = []
            temp_val3 = []
            new_temp_val3 = []
            temp_val4 = []
            no_hc = {}
            no_hc_list = []
            if value_list == []:
                nohc = 'There is no Human Capital Disclosure'
                no_hc_list.append(nohc)
                no_hc[cik] = no_hc_list
                #pprint.pprint(no_hc)
                for i in range(len(list(no_hc.keys()))):
                    new_dict2 = {}
                    new_dict2[list(no_hc.keys())[i]] = list(no_hc.values())[i]
                    no_hc_path = '../ST542_secDisclosures/nocik'
                    #print(list(no_hc.values())[i])
                    for k, v in new_dict2.items():
                        if k in list(no_hc.keys()):
                            if not os.path.exists(no_hc_path):
                                os.makedirs(no_hc_path)
                            else:
                               # if f"../ST542_secDisclosures/nocik/{list(no_hc.keys())[i]}.json" in no_hc_path:
                                if os.path.isfile(f"../ST542_secDisclosures/nocik/{list(no_hc.keys())[i]}.json"):
                                    #print("skipping")
                                    continue
                                else:
                                    with open(f"../ST542_secDisclosures/nocik/{list(no_hc.keys())[i]}.json","w", encoding='utf8') as new_content:
                                        json.dump(new_dict2, new_content,ensure_ascii=False, indent=4)
                    #print(f"Creating: ../ST542_secDisclosures/nocik/{list(no_hc.keys())[i]}.json file") 
                #temp_val.append(element)
            else:
                #########################

                for element in value_list:
                    #if element in non_element:
                    if element not in non_element:
                        temp_val.append(element)

                for i in temp_val:
                    if '\xa0' in i:
                        temp_val2.append(i.replace('\xa0',''))
                    # elif "​" in i:
                    #     temp_val
                    #elif i.strip("%,. ").isdigit():
                    # elif i[0].isdigit() or i[1].isdigit():
                    #     temp_val3.append(i)
                    else:
                        #temp_val2.append(i.strip())
                        temp_val2.append(i)


                # Getting rid of duplicate elements
                for i in temp_val2:
                    if i not in temp_val3:
                        temp_val3.append(i)
                    else:
                        continue

                # for element in temp_val3:
                #     di_list = 
                #     if element in allFilings2021_part1_di_keywords:
                #         print

                #new_val = new_temp_val3
                new_val = temp_val3
                #no_hc[cik] = no_hc_list
                clean_dict[cik] = new_val
                yes_hc[cik] = "There is Human Capital"


                for i in range(len(list(clean_dict.keys()))):
                    new_dict = {}
                    new_dict[list(clean_dict.keys())[i]] = list(clean_dict.values())[i]
                    yes_hc_path = '../ST542_secDisclosures/yescik'
                    # di_dic = {}
                    # di_list = []
                    # di_path = '../ST542_secDisclosures/di'
                    for k, v in new_dict.items():
                        if k in list(yes_hc.keys()): 
                            if not os.path.exists(yes_hc_path):
                                os.makedirs(yes_hc_path)
                            else:
                                if os.path.isfile(f"../ST542_secDisclosures/yescik/{list(clean_dict.keys())[i]}.json"):
                                #f"../ST542_secDisclosures/yescik/{list(clean_dict.keys())[i]}.json" in yes_hc_path:
                                    #print("skipping")
                                    # for json_file in os.listdir("../ST542_secDisclosures/yescik/"):
                                    #     print(json_file)
                                        
                                    continue
                                else:
                                    with open(f"../ST542_secDisclosures/yescik/{list(clean_dict.keys())[i]}.json","w", encoding='utf8') as new_content:
                                        json.dump(new_dict, new_content,ensure_ascii=False, indent=4)
        else:
            continue

# Open json file for reading and print content using json.load
for file_name in glob('*.json'):
    #print(file_name) # working with allFilings2021_part1.json
    with open(file_name, encoding='utf-8') as content:
        json_data = json.load(content)
        clean_json_data = clean(json_data)
        #clean_json_data

        #print(clean_json_data)
        #clean_json_data
        #filter_di_data
        #print(type(json_data)) class is a dict
        #pprint.pprint(json_data)
    break # Would need to comment this out for the other json files for part2-6

# This will look into the yescik directory:

# gray area- "101778", "89800", "65984"
di_keys = ["1800","2488","3453", "3570","4281","4447",
"4904","5513",
"6176","7084","7431","8063","8818",
"9092","9326","9346","9389",
"12208","14272","15615","18230", "18349","18926","19411","20212", "21344","21535","21665","24090","24491", "25475","26172","26324","26780", "27996","28412","28823","29669",
"30697","31791","34067","34903", "35527","36047","36270","36377", "37785","37808","37996","39899","40211", "40729","40888","40987", "46080","46129","46195","47111",
"48039","49071","49196","49826", "50863","51434","52827", "54381","55067","56047","58492","59255","59478", "59527","59558","60977", "61986","62709","62996",
"63276","63908","64040", "64803","65984","66570", "66756","67716","69488", "70415","70858","71691", "72162","72741","72971", "73088","73124","74208", "77360","78003","78128",
"78814","79282","80661", "84246","84748","86312", "89800","91767","92230", "92380","93410","93556", "97134","97216","97745", "98222","100517","101199",
"101778","102212","104889", "104894","105319","105770","106535","107263","200406", "216085","216228","217346", "225648","230557","277135", "277509","310158","310522", "313616","313927","317540", "318154","318833","320335", "350894","351569","352541",
"352825","353020","354707", "357301","700564","701288", "701374","702165","702513", "704415","708821","708955", "712034","712534","713676", "714310","717423","718877"]
# Unsure- "19612" if this should be included for no_di
no_di_keys= ["2098","2178","3197",
"4977","5272","5981",
"7039","7332","7536",
"7789","9984","10456","11544",
"12927","14930","19584","19612","19617","19745","20520","21175", "22356","22701","23111","23194","25445","25743","26058","27904", "29002","29905","29989",
"30305","30625","31107","31462", "33213","35214","36029", "36506","38725","39263","40533", "42682","42888","43196","45876", "48287","48898","49754","51143", "54480","55135","59440","60086",
"60714","61398","62234","64996","65596","66740", "68505","70318","70487", "72903","73309","73756", "74303","75208","75252", "75362","75677","76282", "76605","77281","77476", "77543","77877","78890", "80035","80172","82811",
"85961","87347","88121", "88205","89439","90498", "91142","91440","91576", "91928","92122","93389", "94049","94344","95574", "95953","96943","97210", "97476","98362","99780", "100885","101382","101984", "102729","102752","103145",
"103730","105016","105418", "105634","106640","109380", "203596","215466","277948", "310142","311094","314203", "314489","315709","315852", "316709","318300","350698", "350852","351834","352915", "353569","354190","354908", "354963","355811","356171",
"357173","700565","700923", "701347","703604","704440", "704532","706129","707179", "708781","709005","709337", "711669","711772","712537", "714395","715072","715787", "715957","716006","716634", "717538","717605","717806", "718937","719220","719413"]
def filter_di(d):
    dictionary_data = d
    di_path = "../ST542_secDisclosures/yescik/di/"
    no_di_path = "../ST542_secDisclosures/yescik/nodi/"
    #new_json = {}
    for key, value in dictionary_data.items():
        new_json = {}
        new_no_di_json = {}
        my_data_list = dictionary_data[key]
        di_list = []
        temp_val = []
        #no_di_list = []
        if key in di_keys:
            if key == "1800":
                start_index = my_data_list.index("Diversity and Inclusion ")
                end_index = my_data_list.index("5")
                for ind in range(start_index+1,end_index):
                    di_list.append(my_data_list[ind])
            elif key == "2488":
                start_index = my_data_list.index("Belonging and Inclusion")
                end_index = my_data_list.index("Total Rewards")
                for ind in range(start_index+1,end_index):
                    di_list.append(my_data_list[ind])
            elif key == "3453":
                start_index = my_data_list.index("Diversity, Equity and Inclusion:")
                end_index = my_data_list.index("Total Rewards Programs:")
                for ind in range(start_index+1,end_index):
                    di_list.append(my_data_list[ind])
            elif key == "3570":
                start_index = my_data_list.index("Diversity and Inclusion")
                end_index = my_data_list.index("Development and Training")
                for ind in range(start_index+1,end_index):
                    di_list.append(my_data_list[ind])
            elif key == "4281":
                start_index = my_data_list.index("Diversity, Equity and Inclusion")
                end_index = my_data_list.index("Health and Safety")
                for ind in range(start_index+1,end_index):
                    di_list.append(my_data_list[ind])
            elif key == "4447":
                start_index = my_data_list.index("Inclusion, Diversity and Equity")
                end_index = my_data_list.index("Reward Programs")
                for ind in range(start_index+1,end_index):
                    di_list.append(my_data_list[ind])
            elif key == "4904":
                start_index = my_data_list.index("Diversity and Inclusion")
                end_index = my_data_list.index("Culture")
                for ind in range(start_index+1,end_index):
                    di_list.append(my_data_list[ind])
            elif key == "5513":
                start_index = my_data_list.index("Inclusion and Diversity")
                end_index = my_data_list.index("17")
                for ind in range(start_index+1,end_index):
                    di_list.append(my_data_list[ind])
            elif key == "6176":
                for ind in range(9,10):
                    di_list.append(my_data_list[ind])
            elif key == "7084":
                for ind in range(1,127):
                    di_list.append(my_data_list[ind])
            elif key == "7431":
                for ind in range(10,11):
                    di_list.append(my_data_list[ind])
            elif key == "8063":
                start_index = my_data_list.index("Diversity and Inclusion ")
                end_index = my_data_list.index("Health and Safety")
                for ind in range(start_index+1,end_index):
                    di_list.append(my_data_list[ind])
            elif key == "8818":
                for ind in range(44,45):
                    di_list.append(my_data_list[ind])
            elif key == "9092":
                for ind in range(11,12):
                    di_list.append(my_data_list[ind])
            elif key == "9326":
                start_index = my_data_list.index("Diversity and Inclusion ")
                end_index = my_data_list.index("Training and Well-Being Programs")
                for ind in range(start_index+1,end_index):
                    di_list.append(my_data_list[ind])
            elif key == "9346":
                # start_index = my_data_list.index("Diversity and Inclusion")
                # end_index = my_data_list.index("\n\n14\n\n\n\n")
                for ind in range(14,15):
                    di_list.append(my_data_list[ind])
            elif key == "9389":
                start_index = my_data_list.index("Diversity and Inclusion")
                end_index = my_data_list.index("Talent")
                for ind in range(start_index+1,end_index):
                    di_list.append(my_data_list[ind])
            elif key == "12208":
                start_index = my_data_list.index("Diversity, Equity and Inclusion")
                end_index = my_data_list.index("Compensation and Benefits")
                for ind in range(start_index+1,end_index):
                    di_list.append(my_data_list[ind])
            elif key == "14272":
                start_index = my_data_list.index("Diversity, Equity and Inclusion")
                end_index = my_data_list.index("Career Growth and Development")
                for ind in range(start_index+1,end_index):
                    di_list.append(my_data_list[ind])
            elif key == "15615":
                for ind in range(12,14):
                    di_list.append(my_data_list[ind])
            elif key == "18230":
                start_index = my_data_list.index("Diversity and Inclusion")
                end_index = my_data_list.index("Compensation, Benefits and Employee Insights")
                for ind in range(start_index+1,end_index):
                    di_list.append(my_data_list[ind])
            elif key == "18349":
                start_index = my_data_list.index("Diversity, Equity and Inclusion (“DE&I”)")
                end_index = my_data_list.index("Employee Health and Safety")
                for ind in range(start_index+1,end_index):
                    di_list.append(my_data_list[ind])
            elif key == "18926":
                start_index = my_data_list.index("Diversity, Inclusion & Belonging")
                end_index = my_data_list.index("Positive Corporate Culture")
                for ind in range(start_index+1,end_index):
                    di_list.append(my_data_list[ind])
            elif key == "19411":
                for ind in range(6,7):
                    di_list.append(my_data_list[ind])
            elif key == "20212":
                start_index = my_data_list.index("Diversity and Inclusion")
                end_index = my_data_list.index("Talent Acquisition, Development and Retention")
                for ind in range(start_index+1,end_index):
                    di_list.append(my_data_list[ind])
            elif key == "21344":
                start_index = my_data_list.index("Diversity, Equity and Inclusion")
                end_index = my_data_list.index("Compensation and Benefits")
                for ind in range(start_index+1,end_index):
                    di_list.append(my_data_list[ind])
            elif key == "21535":
                start_index = my_data_list.index("Diversity, Inclusion, and Non-discrimination")
                end_index = my_data_list.index("Employees")
                for ind in range(start_index+1,end_index):
                    di_list.append(my_data_list[ind])
            elif key == "21665":
                start_index = my_data_list.index("Diversity, Equity & Inclusion ")
                end_index = my_data_list.index("Succession Planning")
                for ind in range(start_index+1,end_index):
                    di_list.append(my_data_list[ind])
            elif key == "24090":
                start_index = my_data_list.index("Diversity and Inclusion.  ")
                end_index = my_data_list.index("Health and Safety.")
                for ind in range(start_index+1,end_index):
                    di_list.append(my_data_list[ind])
            elif key == "24491":
                start_index = my_data_list.index("Diversity and Inclusion ")
                end_index = my_data_list.index("Foreign Operations")
                for ind in range(start_index+1,end_index):
                    di_list.append(my_data_list[ind])
            elif key == "25475":
                start_index = my_data_list.index("Diversity and Inclusion - Employee Hiring Practices")
                end_index = my_data_list.index("Employee Wellness ")
                for ind in range(start_index+1,end_index):
                    di_list.append(my_data_list[ind])

            elif key == "26172":
                for ind in range(34,35):
                    di_list.append(my_data_list[ind])
            elif key == "26324":
                start_index = my_data_list.index("Diversity and Inclusion")
                end_index = my_data_list.index("Health and Safety")
                for ind in range(start_index+1,end_index):
                    di_list.append(my_data_list[ind])
            elif key == "26780":
                for ind in range(16,17):
                    di_list.append(my_data_list[ind])
            elif key == "27996":
                start_index = my_data_list.index("Inclusion, Diversity and Equity")
                end_index = my_data_list.index("Health, Wellness and Safety")
                for ind in range(start_index+1,end_index):
                    di_list.append(my_data_list[ind])
            elif key == "28412":
                start_index = my_data_list.index("Diversity")
                end_index = my_data_list.index("Compensation and Benefits")
                for ind in range(start_index+1,end_index):
                    di_list.append(my_data_list[ind])
            elif key == "28823":
                start_index = my_data_list.index("Diversity and Inclusion")
                end_index = my_data_list.index("Employee Engagement")
                for ind in range(start_index+1,end_index):
                    di_list.append(my_data_list[ind])
            elif key == "29669":
                start_index = my_data_list.index("Diversity, Equity and Inclusion ")
                end_index = my_data_list.index("Pay Equity")
                for ind in range(start_index+1,end_index):
                    di_list.append(my_data_list[ind])
            elif key == "30697":
                start_index = my_data_list.index("Diversity, Equity and Inclusion")
                end_index = my_data_list.index("Compensation and Benefits")
                for ind in range(start_index+1,end_index):
                    di_list.append(my_data_list[ind])
            elif key == "31791":
                start_index = my_data_list.index("Diversity and Inclusion")
                end_index = my_data_list.index("12")
                for ind in range(start_index+1,end_index):
                    di_list.append(my_data_list[ind])
            elif key == "34067":
                start_index = my_data_list.index("Diversity and Inclusion. ")
                end_index = my_data_list.index("10")
                for ind in range(start_index+1,end_index):
                    di_list.append(my_data_list[ind])
            elif key == "34903":
                start_index = my_data_list.index("Diversity and Inclusion")
                end_index = my_data_list.index("Health, Safety, and Wellness")
                for ind in range(start_index+1,end_index):
                    di_list.append(my_data_list[ind])
            elif key == "35527":
                start_index = my_data_list.index("Inclusion and Diversity ")
                end_index = my_data_list.index("20 Fifth Third Bancorp")
                for ind in range(start_index+1,end_index):
                    di_list.append(my_data_list[ind])
            elif key == "36047":
                start_index = my_data_list.index("Inclusion and Diversity")
                end_index = my_data_list.index("Talent and Development")
                for ind in range(start_index+1,end_index):
                    di_list.append(my_data_list[ind])
            elif key == "36270":
                start_index = my_data_list.index("Diversity, Inclusion and Belonging")
                end_index = my_data_list.index("Development and Engagement")
                for ind in range(start_index+1,end_index):
                    di_list.append(my_data_list[ind])
            elif key == "36377":
                start_index = my_data_list.index("Diversity and Inclusion")
                end_index = my_data_list.index("Health, Safety and Wellness")
                for ind in range(start_index+1,end_index):
                    di_list.append(my_data_list[ind])
            elif key == "37785":
                start_index = my_data_list.index("Culture and Inclusion")
                end_index = my_data_list.index("Safety ")
                for ind in range(start_index+1,end_index):
                    di_list.append(my_data_list[ind])
            elif key == "37808":
                start_index = my_data_list.index("Diversity. ")
                end_index = my_data_list.index("Engagement.  ")
                for ind in range(start_index+1,end_index):
                    di_list.append(my_data_list[ind])
            elif key == "37996":
                start_index = my_data_list.index("Diversity, Equity, and Inclusion")
                end_index = my_data_list.index("Talent Attraction, Growth, and Capability Assessment")
                for ind in range(start_index+1,end_index):
                    di_list.append(my_data_list[ind])
            elif key == "39899":
                start_index = my_data_list.index("Diversity, Equity and Inclusion")
                end_index = my_data_list.index("Investing in Our People")
                for ind in range(start_index+1,end_index):
                    di_list.append(my_data_list[ind])
            elif key == "40211":
                start_index = my_data_list.index("Diversity and Inclusion")
                end_index = my_data_list.index("7")
                for ind in range(start_index+1,end_index):
                    di_list.append(my_data_list[ind])
            elif key == "40729":
                start_index = my_data_list.index("Diversity and Inclusion")
                end_index = my_data_list.index("15")
                for ind in range(start_index+1,end_index):
                    di_list.append(my_data_list[ind])
            elif key == "40888":
                start_index = my_data_list.index("Inclusion, Diversity and Engagement")
                end_index = my_data_list.index("Health and Safet")
                for ind in range(start_index+1,end_index):
                    di_list.append(my_data_list[ind])
            elif key == "40987":
                for ind in range(10,13):
                    di_list.append(my_data_list[ind])
            elif key == "46080":
                start_index = my_data_list.index("Diversity and Inclusion (D&I). ")
                end_index = my_data_list.index("23")
                for ind in range(start_index+1,end_index):
                    di_list.append(my_data_list[ind])
            elif key == "46129":
                start_index = my_data_list.index("Diversity and Inclusion ")
                end_index = my_data_list.index("Ethical Business Practices ")
                for ind in range(start_index+1,end_index):
                    di_list.append(my_data_list[ind])
            elif key == "46195":
                for ind in range(6,7):
                    di_list.append(my_data_list[ind])
            elif key == "47111":
                start_index = my_data_list.index("Diversity and Inclusion")
                end_index = my_data_list.index("Community and Social Impact")
                for ind in range(start_index+1,end_index):
                    di_list.append(my_data_list[ind])
            elif key == "48039":
                start_index = my_data_list.index("Diversity & Inclusion")
                end_index = my_data_list.index("Health & Safety")
                for ind in range(start_index+1,end_index):
                    di_list.append(my_data_list[ind])
            elif key == "49071":
                start_index = my_data_list.index(" Inclusion and Diversity ")
                end_index = my_data_list.index("Pay and Benefits Philosophy, Compensation and Financial Security")
                for ind in range(start_index+1,end_index):
                    di_list.append(my_data_list[ind])
            elif key == "49196":
                start_index = my_data_list.index("Attraction")
                end_index = my_data_list.index("9")
                for ind in range(start_index+1,end_index):
                    di_list.append(my_data_list[ind])
            elif key == "49826":
                start_index = my_data_list.index("Diversity and Inclusion")
                end_index = my_data_list.index("Labor Relations")
                for ind in range(start_index+1,end_index):
                    di_list.append(my_data_list[ind])
            elif key == "50863":
                start_index = my_data_list.index("Inclusion")
                end_index = my_data_list.index("Compensation and Benefits")
                for ind in range(start_index+1,end_index):
                    di_list.append(my_data_list[ind])
            elif key == "51434":
                start_index = my_data_list.index("DIVERSITY AND INCLUSION")
                end_index = my_data_list.index("2")
                for ind in range(start_index+1,end_index):
                    di_list.append(my_data_list[ind])
            elif key == "52827":
                start_index = my_data_list.index("Inclusion and Diversity")
                end_index = my_data_list.index("18")
                for ind in range(start_index+1,end_index):
                    di_list.append(my_data_list[ind])
            elif key == "54381":
                start_index = my_data_list.index("Diversity & Inclusion")
                end_index = my_data_list.index("Total Rewards")
                for ind in range(start_index+1,end_index):
                    di_list.append(my_data_list[ind])
            elif key == "55067":
                start_index = my_data_list.index("Equity, Diversity and Inclusion")
                end_index = my_data_list.index("Training and Development: ")
                for ind in range(start_index+1,end_index):
                    di_list.append(my_data_list[ind])
            elif key == "56047": # This could be a gray area
                for ind in range(13,14):
                    di_list.append(my_data_list[ind])
            elif key == "58492":
                start_index = my_data_list.index("Our Inclusion, Diversity and Equity")
                end_index = my_data_list.index("Our Workforce Health and Safety")
                for ind in range(start_index+1,end_index):
                    di_list.append(my_data_list[ind])
            elif key == "59255":
                for ind in range(32,33):
                    di_list.append(my_data_list[ind])
            elif key == "59478":
                start_index = my_data_list.index("Diversity and Inclusion")
                end_index = my_data_list.index("Employee Journeys ")
                for ind in range(start_index+1,end_index):
                    di_list.append(my_data_list[ind])
            elif key == "59527":
                start_index = my_data_list.index("Diversity and Inclusion")
                end_index = my_data_list.index("3")
                for ind in range(start_index+1,end_index):
                    di_list.append(my_data_list[ind])
            elif key == "59558":
                #start_index = my_data_list.index("Diversity and Inclusion")
                #end_index = my_data_list.index("Table of Contents")
                for ind in range(7,8):
                    di_list.append(my_data_list[ind])
            elif key == "60977":
                start_index = my_data_list.index("Diversity")
                end_index = my_data_list.index("Training and Professional Development")
                for ind in range(start_index+1,end_index):
                    di_list.append(my_data_list[ind])
            elif key == "61986":
                for ind in range(3,4):
                    di_list.append(my_data_list[ind])
            elif key == "62709":
                start_index = my_data_list.index("Diversity & Inclusion.")
                end_index = my_data_list.index("Talent Development")
                for ind in range(start_index+1,end_index):
                    di_list.append(my_data_list[ind])
            elif key == "63276":
                start_index = my_data_list.index("Diversity and Inclusion")
                end_index = my_data_list.index("Training and Development")
                for ind in range(start_index+1,end_index):
                    di_list.append(my_data_list[ind])
            elif key == "62996":
                start_index = my_data_list.index("Diversity, Equity and Inclusion (\"DE&I\")")
                end_index = my_data_list.index("Future Workforce")
                for ind in range(start_index+1,end_index):
                    di_list.append(my_data_list[ind])
            elif key == "63908":
                start_index = my_data_list.index("Diversity, Equity and Inclusion (“DEI”)")
                end_index = my_data_list.index("McDonald's Corporation ")
                for ind in range(start_index+1,end_index):
                    di_list.append(my_data_list[ind])
            elif key == "64040":
                start_index = my_data_list.index("Diversity & Inclusion (D&I)")
                end_index = my_data_list.index("Learning and Development Programs")
                for ind in range(start_index+1,end_index):
                    di_list.append(my_data_list[ind])
            elif key == "64803":
                start_index = my_data_list.index("Diversity, Equity & Inclusion")
                end_index = my_data_list.index("Colleague Development")
                for ind in range(start_index+1,end_index):
                    di_list.append(my_data_list[ind])
            elif key == "65984": # gray area
                di_list.append(my_data_list[36:68])
            elif key == "66570":
                start_index = my_data_list.index("Diversity & Inclusion")
                end_index = my_data_list.index("Leadership and Development")
                for ind in range(start_index+1,end_index):
                    di_list.append(my_data_list[ind])
            elif key == "66756":
                start_index = my_data_list.index("Diversity, Equity and Inclusion")
                end_index = my_data_list.index("Yellow Ribbon Program")
                for ind in range(start_index+1,end_index):
                    di_list.append(my_data_list[ind])
            elif key == "67716":
                di_list.append(my_data_list[69:88])
            elif key == "69488":
                start_index = my_data_list.index("Diversity and Inclusion")
                end_index = my_data_list.index("Talent Development")
                for ind in range(start_index+1,end_index):
                    di_list.append(my_data_list[ind])
            elif key == "70415":
                start_index = my_data_list.index("Diversity and Inclusion. ")
                end_index = my_data_list.index("Talent Acquisition, Development and Retention. ")
                for ind in range(start_index+1,end_index):
                    di_list.append(my_data_list[ind])
            elif key == "70858":
                start_index = my_data_list.index("Diversity and Inclusion ")
                end_index = my_data_list.index("Employee Engagement and Talent Retention")
                for ind in range(start_index+1,end_index):
                    di_list.append(my_data_list[ind])
            elif key == "71691":
                start_index = my_data_list.index("Diversity, Equity and Inclusion")
                end_index = my_data_list.index("Talent and Development ")
                for ind in range(start_index+1,end_index):
                    di_list.append(my_data_list[ind])
            elif key == "72162":
                di_list.append(my_data_list[30:31])
            elif key == "72741":
                start_index = my_data_list.index("Diversity & Inclusion.")
                end_index = my_data_list.index("Compensation, Health and Wellness Benefits")
                for ind in range(start_index+1,end_index):
                    di_list.append(my_data_list[ind])
            elif key == "72971":
                start_index = my_data_list.index("Promoting Diversity, Equity and Inclusion.  ")
                end_index = my_data_list.index("Pay Equity Review.")
                for ind in range(start_index+1,end_index):
                    di_list.append(my_data_list[ind])
            elif key == "73088":
                start_index = my_data_list.index("Diversity")
                end_index = my_data_list.index("Health and Safety")
                for ind in range(start_index+1,end_index):
                    di_list.append(my_data_list[ind])
            elif key == "73124":
                start_index = my_data_list.index("DIVERSITY, EQUITY, AND INCLUSION (DE&I)")
                end_index = my_data_list.index("Progress and Accountability.")
                for ind in range(start_index+1,end_index):
                    di_list.append(my_data_list[ind])
            elif key == "74208":
                start_index = my_data_list.index("Diversity and Inclusion")
                end_index = my_data_list.index("5")
                for ind in range(start_index+1,end_index):
                    di_list.append(my_data_list[ind])
            elif key == "77360":
                start_index = my_data_list.index("Inclusion and diversity")
                end_index = my_data_list.index("Health, safety and wellness")
                for ind in range(start_index+1,end_index):
                    di_list.append(my_data_list[ind])
            elif key == "78003":
                start_index = my_data_list.index("Diversity, Equity and Inclusion.")
                end_index = my_data_list.index("Colleague Engagement")
                for ind in range(start_index+1,end_index):
                    di_list.append(my_data_list[ind])
            elif key == "78128":
                di_list.append(my_data_list[69:71])
            elif key == "78814":
                start_index = my_data_list.index("Diversity and Inclusion")
                end_index = my_data_list.index("Health, Safety and Wellness")
                for ind in range(start_index+1,end_index):
                    di_list.append(my_data_list[ind])
            elif key == "79282":
                start_index = my_data_list.index(" Diversity, Inclusion, and Belonging")
                end_index = my_data_list.index(" Health and Safety")
                for ind in range(start_index+1,end_index):
                    di_list.append(my_data_list[ind])
            elif key == "80661":
                start_index = my_data_list.index("Diversity and Inclusion (D&I)")
                end_index = my_data_list.index("Employee Acquisition, Retention, Engagement and Development ")
                for ind in range(start_index+1,end_index):
                    di_list.append(my_data_list[ind])
            elif key == "84246": 
                di_list.append(my_data_list[21:22])
            elif key == "84748": 
                di_list.append(my_data_list[11:12])
            elif key == "86312": 
                start_index = my_data_list.index("Diversity and Inclusion")
                end_index = my_data_list.index("31")
                for ind in range(start_index+1,end_index):
                    di_list.append(my_data_list[ind])
            elif key == "89800": 
                start_index = my_data_list.index("Culture and Engagement")
                end_index = my_data_list.index("Talent Management.")
                for ind in range(start_index+1,end_index):
                    di_list.append(my_data_list[ind])
            elif key == "91767": 
                start_index = my_data_list.index("Diversity and Inclusion")
                end_index = my_data_list.index("Talent Acquisition and Development")
                for ind in range(start_index+1,end_index):
                    di_list.append(my_data_list[ind])
            elif key == "92230":  # Did not get grid of the source
                start_index = my_data_list.index("Diversity, Equity & Inclusion")
                end_index = my_data_list.index("Talent Development")
                for ind in range(start_index+1,end_index):
                    di_list.append(my_data_list[ind])
            elif key == "92380": 
                start_index = my_data_list.index("Diversity, Equity, and Inclusion")
                end_index = my_data_list.index("Effects of COVID-19")
                for ind in range(start_index+1,end_index):
                    di_list.append(my_data_list[ind])
            elif key == "93410": 
                start_index = my_data_list.index("Diversity and Inclusion")
                end_index = my_data_list.index("4")
                for ind in range(start_index+1,end_index):
                    di_list.append(my_data_list[ind])
            elif key == "93556": 
                start_index = my_data_list.index("Diversity, Equity & Inclusion")
                end_index = my_data_list.index("7")
                for ind in range(start_index+1,end_index):
                    di_list.append(my_data_list[ind])
            elif key == "97134": 
                di_list.append(my_data_list[6:7])
            elif key == "97216" or key =="97745": 
                end_index = my_data_list.index("13")
                if key == "97216":
                    start_index = my_data_list.index("DIVERSITY, EQUITY AND INCLUSION")
                elif key == "97745":
                    start_index = my_data_list.index("Diversity and Inclusion")
                for ind in range(start_index+1,end_index):
                    di_list.append(my_data_list[ind])
            # elif key == "97745": 
            #     start_index = my_data_list.index("Diversity and Inclusion")
            #     end_index = my_data_list.index("13")
            #     for ind in range(start_index+1,end_index):
            #         di_list.append(my_data_list[ind])
            elif key == "98222": # This has an empty element
                    di_list.append(my_data_list[39:42])
            elif key == "100517": 
                start_index = my_data_list.index("Diversity, Equity and Inclusion.")
                end_index = my_data_list.index("Health Benefits: COVID-19 Impacts.")
                for ind in range(start_index+1,end_index):
                    di_list.append(my_data_list[ind])
            elif key == "101199": 
                start_index = my_data_list.index("Diversity and inclusion")
                end_index = my_data_list.index( "Fulfilling careers; health, safety and wellness; compensation and benefits; talent development")
                for ind in range(start_index+1,end_index):
                    di_list.append(my_data_list[ind])
            elif key == "101778": # Gray area
                start_index = my_data_list.index("Our People")
                end_index = my_data_list.index("Our Talent Landscape")
                for ind in range(start_index+1,end_index):
                    di_list.append(my_data_list[ind])
            elif key == "102212": 
                start_index = my_data_list.index("Diversity and Inclusion")
                end_index = my_data_list.index("5")
                for ind in range(start_index+1,end_index):
                    di_list.append(my_data_list[ind])
            elif key == "104889": 
                di_list.append(my_data_list[24:25])
            elif key == "104894": 
                start_index = my_data_list.index("Diversity and Inclusion")
                end_index = my_data_list.index("Community Engagement")
                for ind in range(start_index+1,end_index):
                    di_list.append(my_data_list[ind])
            elif key == "105319": 
                start_index = my_data_list.index("Diversity and Inclusion")
                end_index = my_data_list.index("Training and Development")
                for ind in range(start_index+1,end_index):
                    di_list.append(my_data_list[ind])
            elif key == "105770": 
                start_index = my_data_list.index("Diversity and Inclusion")
                end_index = my_data_list.index("Compensation and Benefits")
                for ind in range(start_index+1,end_index):
                    di_list.append(my_data_list[ind])
            elif key == "106535": 
                start_index = my_data_list.index("DIVERSITY, EQUITY AND INCLUSION")
                end_index = my_data_list.index("WEYERHAEUSER COMPANY > 2020 ANNUAL REPORT AND FORM 10-K 3")
                for ind in range(start_index+1,end_index):
                    di_list.append(my_data_list[ind])
            elif key == "107263": # This one, was not sure to include or exclude the 20 because after that, it did talk a little bit more about diversity
                start_index = my_data_list.index("Diversity & Inclusion")
                end_index = my_data_list.index("Other operating costs including human capital expenses")
                for ind in range(start_index+1,end_index):
                    di_list.append(my_data_list[ind])
            elif key == "200406":
                start_index = my_data_list.index("Diversity, Equity, and Inclusion (DEI)")
                end_index = my_data_list.index("Compensation and Benefits ")
                for ind in range(start_index+1,end_index):
                    di_list.append(my_data_list[ind])
            elif key == "216085":
                start_index = my_data_list.index("Diversity")
                end_index = my_data_list.index("Retention")
                for ind in range(start_index+1,end_index):
                    di_list.append(my_data_list[ind])
            elif key == "216228":
                di_list.append(my_data_list[7:8])
            elif key == "217346":
                di_list.append(my_data_list[10:12])
            elif key == "225648":
                #di_list.append(my_data_list[10:28])
                start_index = my_data_list.index("Diversity, Equity and Inclusion (\"DE&I\")")
                end_index = my_data_list.index("Succession and Recruitment")
                for ind in range(start_index+1,end_index):
                    di_list.append(my_data_list[ind])
            elif key == "230557":
                start_index = my_data_list.index("Diversity and Inclusion")
                end_index = my_data_list.index("5")
                for ind in range(start_index+1,end_index):
                    di_list.append(my_data_list[ind])
            elif key == "277135":
                start_index = my_data_list.index("Diversity, Equity and Inclusion")
                end_index = my_data_list.index("9")
                for ind in range(start_index+1,end_index):
                    di_list.append(my_data_list[ind])
            elif key == "277509":
                start_index = my_data_list.index("Diversity and Inclusion")
                end_index = my_data_list.index("4")
                for ind in range(start_index+1,end_index):
                    di_list.append(my_data_list[ind])
            elif key == "310158":
                start_index = my_data_list.index("Global Diversity and Inclusion")
                end_index = my_data_list.index("Compensation and Benefits")
                for ind in range(start_index+1,end_index):
                    di_list.append(my_data_list[ind])
            elif key == "310522":
                di_list.append(my_data_list[15:16])
            elif key == "313616":
                start_index = my_data_list.index("D+I")
                end_index = my_data_list.index("Retention")
                for ind in range(start_index+1,end_index):
                    di_list.append(my_data_list[ind])
            elif key == "313927":
                start_index = my_data_list.index("Diversity, Equity and Inclusion")
                end_index = my_data_list.index("Hiring, Development and Retention")
                for ind in range(start_index+1,end_index):
                    di_list.append(my_data_list[ind])
            elif key == "317540":
                di_list.append(my_data_list[17:18])
            elif key == "318154":
                start_index = my_data_list.index("Diversity, Inclusion and Belonging")
                end_index = my_data_list.index("25")
                for ind in range(start_index+1,end_index):
                    di_list.append(my_data_list[ind])
            elif key == "318833":
                start_index = my_data_list.index("Diversity and inclusion")
                end_index = my_data_list.index("Health, safety and training")
                for ind in range(start_index+1,end_index):
                    di_list.append(my_data_list[ind])
            elif key == "320335":
                start_index = my_data_list.index("People, Culture, and Community")
                end_index = my_data_list.index("Talent Development")
                for ind in range(start_index+1,end_index):
                    di_list.append(my_data_list[ind])
            elif key == "350894":
                start_index = my_data_list.index("Diversity and Inclusion")
                end_index = my_data_list.index( "12")
                for ind in range(start_index+1,end_index):
                    di_list.append(my_data_list[ind])
            elif key == "351569": # like 700564
                di_list.append(my_data_list[14:21])
            elif key == "352541": # Was not able to get rid of the first elemetn
                #di_list.append(my_data_list[61,62,63,65]) 
                start_index = my_data_list.index("Diversity, Equity and Inclusion (DE&I)")
                end_index = my_data_list.index( "4")
                for ind in range(start_index+1,end_index):
                    di_list.append(my_data_list[ind])
            elif key == "352825":
                start_index = my_data_list.index("Diversity, Equity, and Inclusion")
                end_index = my_data_list.index("6")
                for ind in range(start_index+1,end_index):
                    di_list.append(my_data_list[ind])
            elif key == "353020":
                start_index = my_data_list.index("Diversity and Inclusion")
                end_index = my_data_list.index("Compensation and Benefits")
                for ind in range(start_index+1,end_index):
                    di_list.append(my_data_list[ind])
            elif key == "354707": # Similar to 700564
                di_list.append(my_data_list[27:28])
            elif key == "357301": # Similar to 700564
                di_list.append(my_data_list[39:40])
            elif key == "700564": # Similar to 701288
                di_list.append(my_data_list[7:8])
            elif key == "701288": # Similar to 702165
                di_list.append(my_data_list[13:14])
            elif key == "701374":
                start_index = my_data_list.index("Diversity and Inclusion")
                end_index = my_data_list.index("Employee Development")
                for ind in range(start_index+1,end_index+1):
                    di_list.append(my_data_list[ind])
            elif key == "702165": # similar to 708955"; Not sure why this has a dash element
                start_index = my_data_list.index("Diversity, Equity and Inclusion")
                end_index = my_data_list.index( "To underscore our commitment to cultivating a workplace experience where the unique experiences, perspectives, and contributions of all our people are valued, our senior management team recently signed a pledge reaffirming our commitment to diversity, equity, and inclusion.  To advance that commitment, senior leaders from across the company serve on an Inclusion Leadership Council, which is accountable for setting our enterprise inclusion strategy and articulating measurable goals and actions needed to achieve them.  ")
                for ind in range(start_index+1,end_index+1):
                    di_list.append(my_data_list[ind])
            elif key == "702513":
                start_index = my_data_list.index("Diversity and Inclusion")
                end_index = my_data_list.index("Fair Wages and Benefits")
                for ind in range(start_index+1,end_index):
                    di_list.append(my_data_list[ind])
            elif key == "704415":
                start_index = my_data_list.index("Diversity and Inclusion")
                end_index = my_data_list.index("Employee Engagement")
                for ind in range(start_index+1,end_index):
                    di_list.append(my_data_list[ind])
            elif key == "708821":
                start_index = my_data_list.index("Diversity and Inclusion")
                end_index = my_data_list.index("Employee Engagement: ")
                for ind in range(start_index+1,end_index):
                    di_list.append(my_data_list[ind])
            elif key == "708955": #Note: This had it at the end and the section was included inside of the elemnt
                start_index = my_data_list.index( "Employee Engagement. First Financial launched its engagement initiative in 2020, partnering with a third party to measure associate engagement and develop action plans for continued improvement.  In 2020, we hosted virtual town hall meetings for all associates, opening the lines of communications and answering associate concerns. In conjunction with the town hall meetings, pulse surveys were completed with themes around wellbeing, return to work, diversity and inclusion, and career coaching and development.  These surveys provided insight into our associates’ needs and desires, which we can use in future program development. ")
                end_index = my_data_list.index("Diversity, Equity and Inclusion. First Financial prioritizes diversity, equity and inclusion (DEI) as an employer, a financial institution and as a member of the communities in which we operate.  The DEI Committee of the Board provides guidance and oversight to First Financial’s executive committee, the Manager of Diversity, Equity and Inclusion, and the First Financial Diversity Council, which is comprised of 10 associates from across our footprint.  First Financial supports several associate-led business resource groups designed to facilitate networking and leadership development.  First Financial is in the process of building its DEI strategy which includes establishing goals for increased associate and management diversity.  During 2020, First Financial’s CEO held a series of listening sessions with diverse associates as part of our goal to foster a more inclusive environment.  ")
                for ind in range(start_index+1,end_index+1):
                    di_list.append(my_data_list[ind])
            elif key == "712034":
                start_index = my_data_list.index("Diversity and Inclusion")
                end_index = my_data_list.index("5")
                for ind in range(start_index+1,end_index):
                    di_list.append(my_data_list[ind])
            elif key == "712534":
                start_index = my_data_list.index("Diversity Equity and Inclusion")
                end_index = my_data_list.index("Talent Assessment, Succession Planning and Career Path")
                for ind in range(start_index+1,end_index):
                    di_list.append(my_data_list[ind])
            elif key == "713676":
                start_index = my_data_list.index("Diversity, equity and inclusion")
                end_index = my_data_list.index("Total rewards")
                for ind in range(start_index+1,end_index):
                    di_list.append(my_data_list[ind])
            elif key == "714310":
                start_index = my_data_list.index("Diversity, Equity and Inclusion.")
                end_index = my_data_list.index("Total Rewards.")
                for ind in range(start_index+1,end_index):
                    di_list.append(my_data_list[ind])
            elif key == "717423": 
                start_index = my_data_list.index("Diversity, Equity and Inclusion")
                end_index = my_data_list.index("13")
                for ind in range(start_index+1,end_index):
                    di_list.append(my_data_list[ind])
            elif key == "718877":
                start_index = my_data_list.index("Diversity, Equity, and Inclusion (“DE&I”)")
                end_index = my_data_list.index("Compensation and Benefits")
                for ind in range(start_index+1,end_index):
                    di_list.append(my_data_list[ind])
            

            for element in di_list:
                if element not in non_element:
                    temp_val.append(element)
            new_json[key] = temp_val
            if not os.path.exists(di_path):
                os.makedirs(di_path)
            else:
                if os.path.isfile(f"../ST542_secDisclosures/yescik/di/{key}.json"):                      
                    continue
                else:
                    with open(f"../ST542_secDisclosures/yescik/di/{key}.json","w", encoding='utf8') as new_content:
                        json.dump(new_json, new_content,ensure_ascii=False, indent=4)

        elif key in no_di_keys:
            #no_di_list.append("No D+I")
            new_no_di_json[key] = "No D+I"

            if not os.path.exists(no_di_path):
                os.makedirs(no_di_path)
            else:
                if os.path.isfile(f"../ST542_secDisclosures/yescik/nodi/{key}.json"):                      
                        continue
                else:
                        with open(f"../ST542_secDisclosures/yescik/nodi/{key}.json","w", encoding='utf8') as new_content:
                            json.dump(new_no_di_json, new_content,ensure_ascii=False, indent=4)
        else:
            #print(key,value)
            continue

# Currently missing 3 json. Not sure which ones
#for file_name in glob('*.json'):
for json_file in os.listdir("../ST542_secDisclosures/yescik/"):
    with open(file_name, encoding='utf-8') as content: #Weird how the file_name works here, now thinking about it
        json_data = json.load(content)
        filter_di_data = filter_di(json_data)
        filter_di_data

    break
