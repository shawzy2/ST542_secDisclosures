


non_element = [" ","","— ","•","    ",",",", ",": ",".","$",")","(a)","(b)", "(",
"                                           ","◦","■","▪"," — ","—","*","%", "®", "® ", "X","†","††", "•",", ",")%",
". ","​", " ", " (1)","﻿ ",""]

allFilings2021_part1_di_keywords = [
    "Inclusion, Diversity and Equity","Inclusion, Diversity and Engagement","Inclusion and Diversity ","Inclusion and Diversity",
    "Diversity & Inclusion.","Human Capital and Diversity and Inclusion", "Diversity & Inclusion","Diversity and inclusion",
    "Diversity, Equity and Inclusion (DE&I)","Diversity & inclusion", "Culture, Diversity and Inclusion ",
    "Diversity and Inclusion.","Diversity Equity and Inclusion","Diversity, equity and inclusion","Diversity, Equity and Inclusion  ",
    "Diversity and Inclusion:","Diversity and Inclusion (D&I).","Diversity and Inclusion. ","Diversity and inclusion","Diversity & Inclusion (D&I)",
    "Diversity, Equity, and Inclusion (DEI)","Diversity, Equity and Inclusion (“DE&I”)","DIVERSITY, EQUITY AND INCLUSION",
    "Diversity, Equity & Inclusion","Diversity, Inclusion & Belonging", "Diversity, Inclusion and Belonging","Culture and Inclusion",
    "Promoting Diversity, Equity and Inclusion.  ","DIVERSITY, EQUITY, AND INCLUSION (DE&I)","DIVERSITY, EQUITY AND INCLUSION",
    "Inclusion and Diversity", "Diversity, Equity and Inclusion (“DEI”)", "Diversity, Equity & Inclusion (DE&I)",
    "Diversity, Inclusion, and Non-discrimination","Diversity, Equity & Inclusion ","Diversity and Inclusion.  ",
    "Diversity and Inclusion - Employee Hiring Practices","Our Inclusion, Diversity and Equity",
    "Diversity, Equity and Inclusion (\"DE&I\")","D+I","Inclusion and diversity", "Belonging and Inclusion", "Diversity, Equity and Inclusion:",
    "Diversity and Inclusion ", "Diversity and Inclusion","Diversity, Equity and Inclusion",
    "Gender and Racial/Ethnic Diversity by Employee Population","Diversity. ","People, Culture, and Community"
]

# allFilings2021_part1_di_keywords the ones in question
'''
89800
37808
60977
61986

Raw notes:
Culture and Engagement... Imight exclude this 89800.. as of 02/21/2022. this one is exlcuded
Diversity. - this was 37808. double check thiis one
Diversity 0 60977 ,doube check this one
Diversity:   61986. double check this one
diversity and inclusion     this is in 314489 also appears in 315852  ... I might exclude for now-> nvmd
'''
# This could fail based off of ordering
allFilings2021_part1_di_next_section_keywords = ["Compensation and Benefits","Total Rewards","Total Rewards Programs:",
"Development and Training","Health and Safety","Reward Programs",
"Culture","Learning and Development","AVAILABLE INFORMATION ","Arrow’s Response to COVID",
"Pay & Benefits ","Employee Rights, Health and Safety.  In addition to on-the-job safety, Badger Meter takes a holistic view of employee health and well-being, including our multifaceted wellness program, B|Well which aims to provide information, activities and support for smart and healthy choices.  ",
"Training and Well-Being Programs","COVID-19, Employee Safety and Wellness","Talent","Compensation and Benefits",
"Career Growth and Development","Compensation, Benefits and Employee Insights","Employee Health and Safety",
"Positive Corporate Culture","Talent Acquisition, Development and Retention",
"Health and Safety. In response to the COVID-19 pandemic, we implemented significant operating environment changes that we determined were in the best interest of the health of our employees and independent agents, as well as the communities in which we operate, and which comply with government regulations. These changes included having the vast majority of our employees work from home, while implementing additional safety measures for employees continuing critical on-site work.  We also created training programs to assist our independent agents with online sales efforts in order to minimize face-to-face interactions with potential customers and our policyholders.",
"Foreign Operations","Employee Wellness ","Employees","Succession Planning",
"Retention and Employee Development – Dana believes the development of its people is critical to the company’s success. The company empowers individuals to lead their development by articulating their professional, personal, and career growth aspirations to their manager. Development of all Dana people is strongly encouraged and should be considered each year as a part of their goals. Dana as an organization has the responsibility to set the tone, culture, and organizational expectations. The company also provides regular training opportunities for our associates across the globe to ensure they have the skills and information to keep pace with technological change. This development is supported and measured with robust performance management and development plans that encourages employees to continuously improve upon their past performance and build on critical skills the company requires to remain competitive. The company has a mentorship program for diverse employees to help guide and coach employees to positions of leadership and ensure the company is developing a diverse talent pool.",
"Compensation and Benefits","Employee Engagement","Pay Equity","Table of Contents","Health, Safety, and Wellness",
"20 Fifth Third Bancorp","Talent and Development","Development and Engagement","Health, Safety and Wellness","Safety ",
"Engagement.  ","Investing in Our People","Talent Development, and Retention","Table of Contents",
"Health and Safet","HUMAN CAPITAL MANAGEMENT",
"Integrity - We demonstrate an uncompromising commitment to ethical principles.  We act ethically and in the interest of the customers we serve.  We treat others with dignity and respect, and value honesty above all else.",
"Employee Engagement","Ethical Business Practices ","Community and Social Impact","Health & Safety",
"Pay and Benefits Philosophy, Compensation and Financial Security","Labor Relations","Total Rewards",
"Training and Development: ","Employee Journeys ","Training and Professional Development",
"Training and Talent Development: We provide all Manitowoc employees with a wide range of professional development opportunities throughout their careers.  Programs designed to help our employees effectively perform their duties include our training courses in: environmental health and safety, welding apprenticeships, sales skills development, Lean manufacturing methodologies, The Manitowoc Way and corporate compliance (ethics & code of conduct, diversity & inclusion, insider training and workplace harassment).  The Company also provides tuition reimbursement and routinely invests in seminars, conferences, and other training or continuing education for our employees.  Additionally, the CEO and EVP, Human Resources conduct annual global succession planning meetings with senior leadership and the board of directors to review the Company’s top talent.  We have implemented several programs to support the ongoing development of the Company’s top talent including: a mentorship program which includes a focus on developing female leaders, a supervisor leadership development program and ongoing individual development programs designed to build the leadership capabilities of our existing and future leaders.  ",
"Talent Development","Future Workforce","Training and Development","Workplace Health and Safety",
"Learning and Development Programs","Colleague Development","Leadership and Development",
"Talent Acquisition, Development and Retention. ","Employee Engagement and Talent Retention",
"Environmental, Social and Governance (“ESG”) - We seek to operate our businesses in line with sound ESG principles that include corporate governance, social responsibility, sustainability, and cybersecurity.  At our facilities, we undertake various environmental sustainability programs, and we promote social responsibility and volunteerism through programs designed to support and give back to the local communities in which we operate.  At a corporate level, we engage in periodic reviews of our cybersecurity programs, including cybersecurity risk and threats, and we have established stock ownership guidelines for our non-employee directors.  In addition, Kronos publishes a Sustainability Report on its website every two years to provide its customers, stockholders and other stakeholders with additional information on its approach to sustainability. ",
"Compensation, Health and Wellness Benefits","Health and Safety",
"Health, safety and wellness","Colleague Engagement","Employee Engagement and Development",
" Health and Safety","Ethics and Compliance","Human Capital Management",
"Effects of COVID-19", "Lifelong Learning","Human Capital Risks",
"Total Rewards","Diversity in Governance - As of December 31, 2020, women represented 29% of our executive management team and 33% of our Board of Directors.",
"Human Capital Risks","THERMO FISHER SCIENTIFIC INC.","Available Information ",
"Health Benefits: COVID-19 Impacts.","Sustainability","Community Engagement",
"Training and Development","Local Hire","Retention",
"Labor Practices and Policies","Human Capital","Team Member Experience",
"Compensation and Benefits","Employee Engagement and Recruitment",
"Fair Wages and Benefits", "Employee Engagement","Employee Engagement: ",
"Talent Assessment, Succession Planning and Career Path","Total rewards",
"Total Rewards."
]

'''
Notes: Cik to take a look at again
7084- part of the d+i got cut off...if there is no other element
7536- just has a table
9346- weird in terms of structure
15615- I might have to write a condition if the element length is long

19411 - empty eelement... did not include this yet into the list
66756- not sure how this works
73124, 78128,78890,84246, 104889, 107263, 318154, 351569, 352541,702165- it just ends

101778- did not include has d+i as our people
717423 barely has anything
'''


'''
Test cases: 26780
40987
56047
61986 
62709
97745
84748
320335- this one is definately going to get cut off
702165
'''





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