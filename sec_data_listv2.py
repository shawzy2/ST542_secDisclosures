

non_element = [" ","","— ","•","    ",",",", ",": ",".","$",")","(a)","(b)", "(",
"                                           ","◦","■","▪"," — ","—","*","%", "®", "® ", "X","†","††", "•",", ",")%",
". ","​", " ", " (1)","﻿ ",""," —","–","-2-","I-12"," ","•13","**","\n\n\n\n\n \n\nGoldmanSachs2020Form 10-K\n\n5    ",
"\n\n13\n\n\n\n\n","\n13\n\n","25 ",":","Page 9", "):","on-going",
"_______________","- 11 -"," - "," 17","- 12 -","\n\n13\n\n\n\nTable of Contents\n\n","\n13\n","\nTable of Contents\n",
".  ","” below.","” above.","“","”)","(continued)","-10-","","-19-","-22-"]

di_v2_keys = [
    # Part 2
    "722723","723612","726601","728535","732717","732834","740260","742278","749251","750004","750577","759944","763744",
    "763901","764038","764180","764622","765880","766421","766829","768899","769520","776901","783325","784977",
    "785161","789460","789570","790051","793074","793733","793952",
    "798287","798354","802481","802681","805676","809248","811156","811596", "813672","813828","816761",
    "816956","818479","820027","820313","821189","823768","825313","827052","831001","831259","832428","837465",
    "842162","842633","844965","845877","850460","855874","856982","857855","860413","860730","860731","861459",
    "861842","861878","864749","866368","866829","867773","868780","871763","872589","873303",
    "873860","874015","874716","874977","875045","875357","876378","876437","877212","877422","879526",
    "880266","880631","882095","883948","884219","884269","884713","885590","885725","886346","886982","887343",
    "887596","889331","889900","890564","891014","893949","894405","894627","895126",
    "895421","896159","896262","897448","898174","899051","899629","899866","901491","903129","906107","906345",
    "908255","908937","909108","911177","912242","912595", "913144","913241","914475","915912","915913","916365",
    # Part 3
    "917491","917520","920112","920148","920371", "920522", "921082","921582","921738","922224",
    "923571","923796","924901","926326","927066", "927628","928022","929008","930420","931015",
    "931584","933136","935494","936340", "936468", "937556","944809","945764", "945841", "949157",
    "949870", "1000694", "1000697", "1001385", "1001902", "1004980", "1009829", "1011570", "1012100", "1013462",
    "1013488","1013871","1013880","1015328","1018963","1020214","1020569","1020710","1021860","1022079",
    "1022321","1022652","1024725","1025378","1025996","1026214","1027838","1028918","1030469","1031203",
    "1031296","1033012","1035002","1035267","1035443","1035983","1037540","1037976","1038357",
    "1039684","1041061","1042893","1043604","1046025","1046311","1047340","1048477","1049502", "1049606",
    "1050441","1050797","1051343","1053507","1057877","1058090","1059556","1060391","1060736", "1060822",
    "1065088","1065696", "1066605","1067701","1068851","1068875","1069157","1069183","1069202", "1070412",
    "1070494","1070985","1071255","1071739","1073429","1075531", "1076930","1077183", "1077771","1082554",
    "1082923","1084048","1084961","1085913","1090012","1091667","1091748","1091883","1093557","1096056","1097149",
    "1097864","1099219","1099590","1101302","1102112", "1102993","1103982","1104506","1104657","1107843","1108109",
    "1108827","1109546","1111335","1111711","1114483",
    # Part 4
    "1120193", "1121142", "1121484","1122976","1123360","1124140","1124198","1127703","1128928","1129155",
    "1130310","1130713","1133421","1135185","1136869","1137774","1138118","1138639","1140536","1141103",
    "1142596","1142750","1144980","1145197","1156039","1156375","1158172", "1158324","1158463","1159036",
    "1159167","1159281","1162461","1163165","1163302","1163370","1163739","1165002","1166003","1168054",
    "1169445","1171662","1171759","1171825","1173514","1175454","1176948", "1177702","1196501","1200375",
    "1206264","1212458","1212545","1214816","1220754","1222840","1224608","1227025","1227636","1227654",
    "1230245","1232524","1255474","1257640","1258602","1267238","1271214","1273813","1273931","1274173",
    "1278021","1278027","1280600","1281761","1283630","1283699","1284812","1286613","1287213","1288403",
    "1288847","1289848","1289945","1290677","1293971","1294133","1295401","1296435","1297184","1297989",
    "1297996","1298675","1299130","1300514","1303313","1308208","1309108","1309402","1310114", "1311370",
    "1316835","1318220","1318568", "1320414","1320695","1321646","1323885","1324404","1324424","1325702",
    "1326801","1331520", "1331875","1332349","1333274","1333986","1334978","1336917","1337553", "1337619",
    "1338749","1345016","1351636","1352010","1354327","1355096","1356576","1358762","1359841","1360901",
    "1361113","1361658","1361983","1364479","1364885","1365135","1366246","1367644","1370450","1370880",
    "1371285","1373715","1374310","1374535","1377630","1378946","1378950","1380846","1381531","1388658",
    "1389002","1389170","1390777", "1391127","1392972","1393311","1393612","1396009","1396033","1396814",
    "1398987","1400891","1401521",
    # Part 5
    "1401680","1401708","1402057","1403256","1408075","1410636","1411207","1411494","1412707","1418091",
    "1418135","1419612","1421461","1424929"

]

di_v2_keys_s4 = [
    "811156","831259","850460","877212","887343","906107"
    # Part 3
    "1035002","1035443","1070494","1071255","1077183", "1077771", "1091883","1102112","1168054",
    # Part 4
    "1220754","1293971","1295401","1297184","1309402","1338749","1354327","1356576",
]
di_v2_keys_s4_1 = [
    "906107", 
    # Part 3
    "1071255","1077183", "1091883","1102112","1168054",
    # Part 4
    "1293971","1295401","1297184","1309402","1354327","1356576"
    #"1220754"
]
di_v2_keys_s4_2 = [
    # Part 3
    "920112","921082", "921738","1227025"#, "1220754" # I am a bit confliced if I should get rid of 920112 in di_v2_keys_s4 and s4_1
]
di_v2_keys_s4_3 = [
    # Part 3
    "917520",#, "1220754" # I am a bit confliced if I should get rid of 920112 in di_v2_keys_s4 and s4_1
]
di_v2_keys_s4b = [
    "827052","875357",# Confused as to why 811156, 831259, 877212 shows up here
    # Part 3
    "920148","920371","920522", "936468", "1013462" #Note:  This one has a table ; 906107 shows up here
    # 920522 has a table and a nt_keyword that is why it is not working.
]
di_v2_keys_s4b_1 = [
    # This will be a sub_case of di_v2_keys_sb_1: it will have a table and see if it has any keywords or not
    # If it has multiple keywords, it will use the last keyword
    "920522", "936468"
]
di_v2_keys_s4c = [
    "860731","914475","916365",#,"877212"
    # Part 3
    "923796","926326", "930420" , "937556", "1004980",
    # Part 4
    "1137774","1158172","1364479", "1380846","1389002","1393612","1401708"
]
di_v2_keys_s4d = [
    "867773","896159",
    # Part 3
    "923571","927628","1037540","1284812"
]
di_v2_keys_s4e = [
    "872589",
    # Part 3
    "935494","1060391", "1067701","1082554", "1084961","1090012", "1109546",
    # Part 4
    "1158324", "1163739","1232524","1278027","1281761", "1298675","1310114","1324404","1324424","1337619","1355096","1370450","1373715","1388658","1401521"#,"1212545"
    # Part 5
    ,"1411494","1418135","1424929"
]# This will be used if the nt_word does apper more than once, but less than 2
di_v2_keys_s4f = [
    "877212"
]# This will be used if the nt_word does apper more than once


'''
"742112" - does have info about d/i, but no section title
'''

no_di_v2_keys = [
    "719739","720672","720858","723188","723646","726728","726854","727207","729580","729986","730272"
]

st_word = [
    # Part 2
    "Diversity and Inclusion","Diversity, Inclusion and Belonging", "DE&I",
    "The Company operates in a cyclical business where financial performance and headcount is influenced by, among other things, changes in oil and natural gas prices. The Company’s key human capital management objectives are focused on fostering talent in the following areas:",
    #"Diversity and Equality - The Company’s workforce reflects the diversity of the communities in which it operates. Our dedicated team of employees works towards a common purpose.Our Company is strong in its values, relationships and consistency in management.  We have long been dedicated to recruiting and hiring recently discharged military personnel, and dedicated resources undertake this recruiting effort at our company. The Company received the U.S. Department of Labor's \"2019 Hire Vets Medallion Award\" in recognition of this effort and its success.  The Board of Directors has a diversity committee that monitors compliance with applicable non-discrimination laws related to race, gender and other protected classes.  The Committee provides a report of such incidences to the Board on an annual basis.",
    "Diversity, Equity and Inclusion",  "Diversity, Equity & Inclusion ","Diversity, Inclusion, and Belonging",
    "Inclusion and Diversity","Workforce Diversity","Inclusion and Belonging",
    "DIVERSITY AND INCLUSION ","Diversity, equity and inclusion","Diversity","Commitment to Diversity, Equity and Inclusion     ",
    "Diversity, Equity and Inclusion","Inclusion, Diversity, and Equity",
    "Equity, Diversity, and Inclusion (“ED&I”)","Diversity, Equity & Inclusion",
    "Diversity & Inclusion:","Diversity & Inclusion",
    "Diversity, Equity and Inclusion (DEI) ",
    "We contract with independent contractors to supply one or more trucks and drivers for our use. Independent contractors must pay their own truck expenses, fuel, maintenance, insurance, and driver costs. They must meet and operate within our guidelines with respect to safety. We have a lease-purchase program whereby we offer independent contractors the opportunity to lease a truck, with the option to purchase the truck at the end of the lease term. We believe our lease-purchase program has contributed to our ability to attract and retain independent contractors. At December 31, 2020, approximately 305 independent contractors were leasing 393 trucks in this program.",
    "Diversity and Inclusion. ","Diversity, Equity and Inclusion.","D&I ",
    "Diversity, Equity, and Inclusion", "Diversity and Inclusion ","A Culture of Diversity, Equity and Inclusion",
    "We have also continued to attract experienced, productive advisors, with 336 experienced advisors moving their practices to Ameriprise in 2020 and approximately 1,700 in the last 5 years.",
    "Governance and Culture - Our Board of Directors (the “Board”) is actively involved in overseeing the Company’s employee-related strategies and practices as well as the Company’s culture. This oversight is conducted both directly and through certain of the Board’s committees. At each of its regularly scheduled quarterly meetings, the Board reviews changes in key personnel and, at least annually, meets with management to discuss various human resources related topics, including talent development, succession planning, compensation and culture. We believe the Company’s culture has been a critical component of the Company’s success and reinforcing that culture is a key responsibility of our executive management.",
    "Inclusion and Diversity ","Equity, Diversity and Inclusion",
    "As of December 31, 2020, we had 5,989 employees located in approximately 39 different countries in a variety of different roles. In the highly competitive medical device industry, we consider attracting, developing, and retaining talented people in technical, operational, marketing, sales, research, management, and other positions to be critical to our overall long-term growth strategy. Our ability to recruit and retain such talent depends on several factors, including compensation and benefits, talent development, career opportunities, and work environment. We invest in our people and cultivate a company culture committed to supporting a diverse and inclusive workforce.",
    "Our People, Our Priority","Diversity, Equity and Inclusion ","Inclusive Diversity",
    "Diversity and Inclusion: ",
    "The importance of diversity, equity, and inclusion","Inclusion and Diversity",
    "We Are Focused on Our Diversity, Our People and Our Culture. ",
    "General Information. As of December 31, 2020, we had 866 employees globally, 461 of whom hold advanced degrees. Of these employees, 494 are engaged directly in research and development activities and 372 are in selling and general and administration. None of our employees in the United States are covered by collective bargaining agreements and we consider relations with our employees to be good.",
    "Diversity and Inclusion (D&I)","Diversity, Equity, and Inclusion.","Diversity and Inclusion Efforts",
    "Diversity, Equity & Inclusion, or DEI","Diversity and Inclusion Efforts","Inclusion & Diversity",
    " Diversity, Equity and Inclusion","Diversity, equity, and inclusion: ","Diversity Equity and Inclusion ",
    "Talent, Development, Diversity and Inclusion",
    "Demographics:As of December 31, 2020 the company employed 2,187 full and part-time employees. None of these employees is represented by a collective bargaining agreement. During fiscal year 2020, we hired 423 employees. Our voluntary turnover rate was 18.3% in 2020, which compares to 19.6% in 2019.",
    "The safety of our employees and others is our highest priority, as our goal is to provide an incident-free work environment. We have robust safety training programs in place that are designed to comply with applicable laws and industry standards and to benefit our employees, communities and our business. All field-based employees are required to attend an Employee Safety Orientation, which includes classes on behavior-based safety, hazard awareness, safe systems of work, permission to work, time out for safety, energy isolation, hazard communication (HAZCOM) and material handling. In response to the COVID-19 pandemic, we implemented, and continue to implement, safety protocols at our offices, facilities and worksites.These protocols include allowing many of our office-based employees to work from home, while implementing additional safety measures for employees continuing critical on-site work.",
    "Celebrating Inclusion and Diversity","Diversity and inclusion",
    "Corporate Social Responsibility, Diversity, Equity and Inclusion","Inclusive Diversity and Equity (“IDE”)",
    "Diversity, Inclusion, and Belonging:","Diversity, Equity, and Inclusion. ",
    "Diversity, Equity & Inclusion (“DE&I”)","Diversity, Equity, and Inclusion",
    "Our Diversity, Equity and Inclusion (“DEI”) Initiatives","Diversity & Inclusion. ",
    "Diversity and Inclusion.",
    # Part 3
    "Workplace Diversity","Diversity and Veteran Recruitment Initiatives",
    "PPL, together with its subsidiaries, is committed to fostering an exceptional workplace for employees. PPL pledges to enable success of its current and future workforce through a human capital management approach that cultivates a diverse, equitable and inclusive culture, fosters professional development and encourages employee engagement. Matters related to these priorities and corporate culture are overseen by PPL's senior management, which provides updates to the PPL Board of Directors (the Board). Three priorities of this commitment and their oversight are as follows: ",
    "Corporate Culture & Diversity","Diversity & Belonging","Inclusion and Diversity. ","Diversity, Equity and Inclusion Program",
    "Commitment to Diversity and Inclusion.","Employee Inclusion", "Diversity and Inclusion Initiatives:",
    "Diversity, Equity, and Inclusion (DEI)", "Diversity.", "Inclusion& Diversity ",
    "Each of our plants utilize various interactions to achieve this performance, from a toolbox meeting to cover the day’s work and any particular safety concern, to monthly Safety Plan Meetings, ‘No Days Away’ Safety Awards, and our employee-favorite, Safety Day. Each year, a plant may close for one full day to cover safety training and updates. Outside vendors demonstrate the latest safety procedures and equipment in a hands-on fun atmosphere.",
    "Culture, Values & Inclusion, Diversity, & Equity",
    "Development and Training: The attraction, development and retention of our employees is important to TTEC’s success. To support advancement of our employees and prepare them for demands of rapidly changing workplace and client requirements we offer an extensive career focused curriculum. The pressures of COVID-19 pandemic notwithstanding, in 2020 we made significant investments in our talent management platform, TTEC University, that includes a library of more than 8,000 courses that cover topics important to general business acumen ranging from business operations, leadership, ethics, finance, negotiations, and project management to subject-matter specific professional and technical curriculum. TTEC development programs help identify top performers, improve employee retention, and create promotion-from-within opportunities in the Company. In 2020, TTEC launched the Talent Accelerator Program (“TAP”) designed to identify and attract new talent and prepare them for success within our organization. The program recruits recently graduated candidates with diverse backgrounds ranging for technology to humanities who undergo a three-year specialized training and rotation through all business functions and segments in our organization. Program participants gain experience in finance, risk, human capital, IT, communication, marketing, sales, and operations, becoming fully immersed in the day-to-day operations of the business. Once the program is completed, the TAP participants will be equipped with knowledge and experience necessary to progress as a manager in the Company.",
    "INCLUSION AND DIVERSITY","Diversity and Inclusion.","Inclusion and Diversity","Diversity and Inclusion ",
    "Inclusion and Diversity",
    "Total Rewards: Rewarding and supporting our employees is essential to Company morale. To ensure we maintain a competitive salary and benefits package, we utilize an independent third party to evaluate employee wages. We continue to explore and utilize benefits options in line with our growing and diverse workforce to attract and retain top talent. These benefits include but are not limited to retirement savings, employee stock purchase plans, a variety of health insurance options, including dental and vision, discounts on healthy foods and fitness memberships, disability insurance, and paid maternity/paternity leave. Our Remote Work Policy also allows for a flexible work schedule and location, depending on business needs and the specific role. ",
    "Diversity, Equity, and Inclusion.","Diversity, equity and inclusion",
    "Diversity, Equity and Inclusion (“DEI”)","Diversity, equity and inclusion. ",
    "Diversity, Equality, and Inclusion","Building a diverse and inclusive workforce",
    "Safety—We have established comprehensive safety programs throughout our operations to ensure that all employees comply with safety standards we have established and that are established under federal, state and local laws and regulations. Safety leadership establishes safety programs and benchmarking to improve safety across the Company. Additionally, our employment screening process seeks to determine that prospective employees have requisite skills, sufficient background references and acceptable driving records, if applicable. Our rate of incidents recordable under the standards of the Occupational Safety and Health Administration (“OSHA”) per one hundred employees per year, also known as the OSHA recordable rate, was 1.36 during 2020. This level was 20% better than the most recently published OSHA rate for our industry.",
    "Diversity & Inclusion ","Diversity and inclusion. ","Equity, Inclusion & Belonging", "Employee Development",
    "Diversity, Equity, and Inclusion ","Choice Culture and Diversity",
    "Health and Safety – Protecting the health and safety of our employees, our customers, our business partners and the natural environment is one of our core values. We are committed to conducting our business in ways that provide all personnel with a safe and healthy work environment and have established safety and environmental programs and goals to achieve such results. We expect our manufacturing facilities to produce our products safely and in compliance with local permits and policies intended to protect the environment and we have established global policies designed to promote such compliance. We require our employees to comply with legal and regulatory requirements and our policies, standards and practices.",
    "Diversity, Equity and Inclusion. ", "Diversity, Equity, and Inclusion:",
    "Culture, Values & Diversity, Equity & Inclusion", "Inclusion and diversity (“I&D”):",
    "As of December31, 2020, the Company had 3,756 full-time equivalent associates, 1,124 of whom were officers of the Bank. Neither the Company nor the Bank is a party to any collective bargaining agreement.",
    "Employee and Board Diversity. ",
    "Employee Engagement, Benefits & Development.We believe that our future success is dependent upon our ability to recruit, hire and retain exceptional employees. We provide our employees with competitive cash compensation, opportunities to own equity, and an employee benefit program that promotes well-being, including healthcare, retirement planning and paid vacation time. We also provide employees with opportunities to continue their education and growth, including leadership development and tuition reimbursement. In order to receive feedback from our employees and evaluate our level of employee engagement, we regularly conduct an employee survey.",
    "Diversity, Equity, and Inclusion (DEI)","Diversity and Gender Equity","Human resources and hiring","World-Class Culture",
    "Diversity, Equity and Inclusion.  ","Diversity, Equity & Inclusion","Driving a diverse and inclusive culture.",
    "Diversity & Inclusion (\"D&I\")","Diversity. ","Diversity, equity and inclusion:",
    "Diversity and Inclusion.. ","Focus on Inclusion",#"Promoting an Inclusive Culture Through Learning Opportunities."
    # Part 4
    "Diversity, Inclusion and Belonging (DIB)",
    "The recreational boating industry is cyclical and therefore headcount is subject to change based on production levels which are a function of dealer and consumer demand. The Company’s key human capital management objectives are focused on fostering talent in the following areas:",
    "Diversity, Equity and Inclusion (“DEI”)","Diversity and Inclusion at Prudential",
    "At December 31, 2020, Willis Towers Watson’s global workforce was 53.8% female and 46.2% male, and global and senior leadership was 27.7% female. Our Board of Directors was 33.3% female, including the Compensation Committee Chairman.Voluntary turnover (rolling 12-month attrition) was 11.3% in 2020 compared to 11.2% in 2019. ",
    "Diversity, Equality, and Inclusion. ","Diversity, Equality and Inclusion",
    "As of December 31, 2020, we had 1,083 employees located in 15 different countries in a variety of different roles. Approximately 82.5% of our employees are located in the United States and Canada, 16.8% are located in Europe and 0.7% are located in Asia. As of December 31, 2020, 53% of our employees were quota-bearing sales representatives, 13% were in sales management or sales support roles and 34% were in operational or administrative functions.  Unions represent 30 of our employees in France.  We believe that we have a satisfactory relationship with our employees.",
    "Diversity and Inclusion:","Employees and Equal Opportunity. ",
    "Employee Profile and Diversity","Diversity and Equal Opportunity",
    "Diversity, Equity and Inclusion:","Diversity, inclusion and belonging","Global Workforce and Diversity. ",
    "Diversity and Inclusion  ","Demographics and Diversity","Diversity and Inclusion (\"D&I\")",
    "Training, Development and Career Opportunities.  We are committed to the personal and professional development of our employees, with the belief that a greater level of knowledge, skill and ability is of personal benefit to the employee and fosters a more creative, innovative, efficient and therefore competitive company. We strive to empower our employees to develop the skills they need to perform their current jobs while developing acumen for future opportunities. We want our talent pool to identify a successful and fulfilling career progression within our company. ",
    "Health and safety – Protecting the health and safety of our employees, our customers, our business partners and the natural environment is one of our core values. We are committed to conducting our business in ways that provide all personnel with a safe and healthy work environment and have established safety and environmental programs and goals to achieve such results. We expect our manufacturing facilities to produce our products safely and in compliance with local permits and policies intended to protect the environment and have established global policies designed to promote such compliance.We require our employees to comply with legal and regulatory requirements and our policies, standards and practices.",   
    "Fostering Diversity, Equity and Inclusion ","Diversity and inclusion initiatives. ",
    "Diversity, Equity & Inclusion—",
    "Employee Empowerment, Training and Professional Development. We enable and encourage our employees to grow, excel and realize their full potential. We strive to hire people more talented than we are. We empower our people to make the decisions needed today, and prepare them for even bigger decisions they will make in the future. We support professional development by providing access to internal and external training resources and programs.",
    "In order to build the best team, it is necessary for us to fill talent needs with qualified, diverse and engaged associates. Key to our success is our internal talent management program which strives to optimally deploy existing talent across Regions by focusing on where our associates excel and helping them find the best roles for them. One of the hallmarks of our success in this area is demonstrated by our ability to fill vacancies from within. For example, in 2020, 45 percent of our hires were internal fills. For those roles which we fill externally, we continually build talent pipelines with an eye towards not only current needs, but also future demands of our business. Regions uses a number of innovative tools and structured processes to achieve our goals including applications and resources designed to reach larger and more diverse audiences. Our recruiting technology is agile, user friendly and allows us to offer to candidates a robust understanding of our needs, requirements and a view of our culture to support the building of a diverse, engaged workforce.",
    "As part of our compensation philosophy, we believewe must offer and maintain market competitive total rewards programs in order to attract and retain superior talent. These programs not only include base wages and incentives in support of our pay for performance culture, but also healthand retirement benefits. We focus many programs on employee wellness. We believe these solutions helpthe overall health and wellness of our employees and helpus successfully manage healthcare and prescription drug costs for our employee population.",
    "Diversity & Inclusion at Five9 ","DIVERSITY, EQUITY AND INCLUSION",
    "Employee Engagement: To assess and improve employee retention and engagement, we have surveyed employees, with the assistance of third-party consultants, and use the results of and feedback from the survey to address employee concerns. Our most recent survey was conducted in November 2020 and included participation by over two-thirds of our employees.",
    "Retirement benefits: all eligible employees are able to participate in retirement planning schemes, which may include contributions from the employer, as well as the employee; ",
    "Inclusion and diversity",
    "Talent Development. We seek to hire talented and motivated individuals and prioritize their continued education and training. The Company works to support the success and growth of its employees through a collaborative and dynamic 360-degree performance management and review cycle. Furthermore, through investments in technology, we have enhanced knowledge management and collaboration tools across our businesses.",
    "Diversity and Inclusion of our workforce","Diversity, Equity, & Inclusion: ","Culture, Inclusion and Diversity.",
    "In managing the Company’s business, management focuses on various human capital measures and objectives designed to address the development, attraction and retention of personnel. These include competitive compensation and benefits, paid time off, an employee retirement plan, bonus and other incentive compensation plans, modern equipment and support, leadership development and professional development as well as those benefits described below.",
    "Equity, Diversity & Inclusion (",
    "Additionally, our operations have comprehensive safety programs that include safety audits, training, contractor safety requirements and that include annual health and safety budgets as part of essential capital planning. Furthermore, contractors must meet stringent state and federal safety regulations and undergo industry-specific safety training. Four of our seven Wood Products facilities have received the U.S. Occupational Safety & Health Administration’s Voluntary Protection Program (VPP) status which recognizes excellence in occupational health and safety. VPP status requires a good health and safety management system, hazard prevention, training, incident rates below industry average and audits to evaluate the facilities for health and safety performance.",
    "We strive to help our employees maintain job stability, so they are encouraged to stay with the Company and positioned to grow their skills and knowledge on the job. The 2020 annualized voluntary turnover rate in our workforce generally was flat as compared to 2019. In an effort to reduce employee turnover, we engage in annual surveys with employees, we maintain an open-door policy that enables us to help identify any issues before they cause an employee to leave the Company, and we review exit interview data, hotline calls and root cause analysis to help deter turnover. We also assign dedicated Company human resources representatives to each department so that we can better monitor employee morale within each department. ",
    "Additionally, as of December 31, 2020, our consolidated subsidiaries had an aggregate of approximately 26,424 full and part-time employees. Employment levels fluctuate due to seasonal factors affecting our business. Additionally, our consolidated subsidiaries utilize independent contractors and temporary staffing agency personnel to supplement their workforce, particularly on a seasonal basis. We believe that our employee relations are good and a key factor in our workforce strategy.",
    "Diversity, Equity and Inclusion: ","Promote Sense of Belonging through Diversity and Inclusion Initiatives",
    "Diversity, Equity, and Inclusion Commitment ","Diversity, inclusion and belonging. ",
    "We screen leadership hires and measure employee performance against these company values, and regularly measure employee engagement against these values through our Employee Voice Survey. We believe our values-driven culture of open and transparent communication has contributed to our recognition as a great place to work by our employees. ",
    "Equal Opportunity, Diversity, and Pay Equity",
    "Within the United States, approximately650 were hourly-rated, unionized employees. Outside the United States, we have government-mandated collective bargaining arrangements and union contracts in certain countries, particularly in Europe where certain of our employees are represented by unions and/or works councils. The Company believes that its relationship with employees is good. See “Risk Factors—Risks Related to Our Business and Industry—We may be subject to work stoppages at our facilities, or our customers may be subjected to work stoppages, which could seriously impact our operations and the profitability of our business.”",
    "—We invest in our employees by providing comprehensive benefits and compensation packages. Our benefits packages include: comprehensive health insurance with a wellness program for all employees working 30 hours or more, parental leave for all new parents for the birth or adoption of a child or placement of foster care, 401k plan with a comprehensive financial wellness component and voluntary benefits employees can tailor to their specific needs ranging from additional life insurance to pet insurance. ",
    "Diversity Equity and Inclusion/Culture","Diversity, Inclusion & equal opportunity",
    "We offer a competitive compensation package to attract, retain and motivate highly qualified and diverse talent. We believe in pay-for-performance; our compensation programs are grounded in a pay-for-performance philosophy that is designed to reward achievement of our Company’s financial and strategic performance. We review performance and compensation with all employees annually. We seek to pay our employees fairly for their work and we continuously monitor our performance and address any discrepancies or issues. We regularly benchmark roles and compensation data to help ensure internal pay equity. Discover partners with an independent, third-party consultant to conduct a company-wide pay equity analysis that includes race and gender to identify pay discrepancies. Based on our last two reviews using this approach, women and minorities at Discover earn, on average, between $0.99 and $1.02 for every $1 earned by men and non-minorities.",
    "Diversity and inclusion are important values at Vulcan","Diversity and Employment Statistics",
    # Part 5
    "Commitment to Diversity and Inclusion",
    "Workforce Demographics. Our people continue to be a critical component in our continued success, the delivery of our values and the execution of our growth initiatives. As of December31, 2020, we had a highly skilled workforce of approximately 3,300 employees, with approximately 89% of those employees in the U.S. Approximately 47% of our U.S. employees are represented by the International Union, United Automobile, Aerospace and Agricultural Implement Workers of America (“UAW”) and are subject to a collective bargaining agreement. In December 2017, we entered into a six year collective bargaining agreement with UAW Local 933 that expires in November 2023. There have been no strikes or work stoppages due to Allison-specific issues in over 30 years.",
    "Inclusion and Diversity (I&D).",
    "Leadership, Training and Development: We aim to provide our employees with advanced professional and development skills so that they can perform effectively in their roles and build their capabilities and career prospects for the future. We maintain a leadership program for managers and team leaders and deliver advanced professional training for sales, research and development and other functional teams as part of our extensive training program each year. ",
    "Inclusion, Diversity and Engagement",
]


# If the nt_word list ordering changes, the whole code base I wrote will break
nt_word = [
    # Part 2
    "Total Rewards","Health and Safety","Community Involvement","Employee Safety and Health","Health & Safety",
    "Development and Training - The Company’s management team and all its employees are expected to exhibit and promote honest, ethical and respectful conduct in the workplace. We have implemented and maintained a corporate compliance program to provide guidance for everyone associated with the Company, including its employees, officers and directors (the \"Code\"). Annual review of the Code is required which prohibits unlawful or unethical activity, including discrimination, and directs our employees, officers, and directors to avoid actions that, even if not unlawful or unethical, might create an appearance of illegality or impropriety. In addition, the Company provides annual training for preventing, identifying, reporting and ending any type of unlawful discrimination. The Company also provides a wide variety of opportunities for professional growth for all employees with in-classroom and online training, on-the-job experience, education tuition assistance and counseling.",
    "Health, Safety and Compensation","Safety","Talent Development ","Colleague Growth and Development", "Employee Experience ",
    "Talent Acquisition, Retention and Employee Development","Compensation and Benefits","Succession Planning",
    "Engagement: ",
    "Number of Employees As of January 31, 2021, we employed approximately 230,000 persons. ",
    "Competitive Wage and Benefits","Associates","A Focus on Ethics","Statistical Disclosure by Bank Holding Companies",
    "Safety and Health","COVID-19","Workforce development","Employee Development and Well-Being",
    "Health, Safety, and Wellness","Table of Contents","Professional Driver Recruitment:",
    "Health and Safety ",
    "Employee Health and Safety. We are committed to being an industry leader in health and safety standards. The physical health, wellbeing, and mental health of our employees is crucial to our success. Most recently, our primary concern during the COVID-19 pandemic has been to do our part to protect our employees, customers, vendors and the general public from the spread of COVID-19 while continuing to serve the vital role of supplying essential goods to the nation. Where possible, our employees are working remotely from their homes. For essential functions, including our driving professionals, we have distributed cleaning and protective supplies to various terminals so that they are available to those that need them, increased cleaning frequency and coverage, and provided employees direction on precautionary measures, such as sanitizing truck interiors, personal hygiene, and social distancing. We will continue to adapt our operations as required to ensure safety while continuing to provide a high level of service to our customers.",
    "Development and Retention","Retention and Career Development.","Health & Safety. ","Summary","Training",
    #"capABLE, aimed at removing barriers and creating pathways to meaningful work for employees of all abilities"
    "Labor Union Affiliations","Preventing Harassment and Discrimination",
    "Training, Development and Retention","Diversity & Inclusion Council",
    "Importantly, our compensation programs are designed to drive a high-performing workforce with deliberate alignment of rewards with client and shareholder success. Weighing both individual goal achievement (the “what”) and leadership performance (the “how”) is critical to driving strong business results and engaging, motivating and retaining our employees.",
    "Workforce Continuity","Workforce Development","Employee Well Being","Together We Belong ","Talent Development",
    "Career Development","Human Capital Risk",
    "Employee Engagement. The engagement of our workforce is critical to delivering on our competitive strategy, and we place high importance on informed and engaged employees. We communicate frequently and transparently with our employees through a variety of communication methods, including video and written communications, town hall meetings, and our company intranet, and we acknowledge individual contributions to Merit by celebrating milestones of service in ",
    "Employee Engagement Surveys","Compensation and Benefits ",
    #"In 2020, our diversity, equity and inclusion (DEI) efforts included focused DEI discussions at the executive and local team levels, assessment of DEI effectiveness across the HR lifecycle, hiring manager training, the development of a Women’s Leadership Mentoring program, and support and advocacy for local DEI councils at Tyler. We encourage you to review our 2020 Corporate Responsibility Report located at http://www.tylertech.com for more detailed information regarding our Human Capital programs and initiatives. "
    "Employee Development and Training","Grow, Engage and Elevate",
    "Work-from-Home and Protecting Our Team during the Pandemic ",
    "Compensation Policies:","A strong safety culture","Talent and Development",
    "Developing our People: We have increased our focus on learning through internal campaigns, curated self-directed learning and through our Sales Academies and our Talent Agent program, which provides skills enhancement to recruiters to foster career advancement. To date, we have trained 2,700 recruiters and 1,345 salespeople. We have also launched a new mobile learning platform that makes on-the-go micro-courses accessible to our employees. Our employees completed nearly 65,000 of these courses in 2020. We believe that our success is contingent upon the development of our next generation of leaders. In 2019, we launched the third cohort for our Emerging Leadership Experience Program. This program identifies emerging leaders who have worked for the company for five or more years and have potential to assume greater responsibility. The two-year program provides development through our three Es approach: Education, Exposure and Experience, which includes Harvard Business School Online coursework as well as mentoring from our most senior leaders.",
    "Employee Wellness, Health, and Safety",
    "Compensation, Benefits and Ongoing Professional Development. We are committed to rewarding, supporting, and developing the employees who make it possible to deliver on our strategy. To that end, we offer a comprehensive total rewards package that includes market-competitive pay, broad-based equity grants and bonuses, healthcare benefits, pension and retirement savings plans, paid time off and family leave, caregiving support, fitness subsidies, tuition reimbursement and an Employee Assistance Program.We offer robust onsite learning opportunities for employees at every stage in their career, and in 2020 we launched ELEVATE – our leadership development program, the participants of which reflect ethnic, racial and gender diversity. In recognition of the new challenges the COVID-19 pandemic brought, we took various steps to support our employees, including by transitioning to remote work and by offering flexible schedule, childcare assistance and sessions focused on resilience and happiness in uncertain times. At the same time, we protected our facility-dependent employees, including those needed to maintain manufacturing and clinical research, by instituting strict protocols designed to ensure they remain healthy.   ",
    "Talent Development","Training and Development","Compensation, Benefits and Well-being","Community Service", "Community Engagement",
    "COVID-19 Pandemic",
    #": We leverage technology to remove gendered language from job postings to attract a diverse pool of applicants. We also strive to create a diverse slate of candidates wherever possible, with additional emphasis on our director level roles and above. We have established partnerships with Catalyst, Society of Women Engineers (SWE), National Society of Black Engineers (NSBE), Disability IN, as well as Historically Black Colleges and Universities to enhance our recruitment efforts and deepen our partnerships with diverse talent."
    "Engagement ","Benefits and Compensation Offerings","Human Capital Risks","Employee Wellness, Health and Safety ","Health and Safety",
    "INFORMATION ABOUT OUR EXECUTIVE OFFICERS","Rewards and Performance Management: ","Talent Development",
    "Health, Safety and Wellness ",
    "Maintaining our Core Values – In 2020, we trained over 4,000 employees on our Code of Business Conduct and Ethics, which addresses conflicts of interest, confidentiality, fair dealing with others, proper use of company assets, compliance with laws, insider trading, keeping of books and records, zero tolerance for discrimination and harassment in the work environment, as well as reporting of violations.",
    "Work Practices and Employee Well-Being","Total Rewards: Compensation and Benefits ","Health, Safety, and Security",
    "Stewards of Our Environment","Talent Development and Retention","Attraction, Development, and Retention",
    "Talent Acquisition, Retention and Development:","Employee Development & Engagement","C.","Employee Wellbeing and Safety",
    "Employee Engagement","COVID-19 Pandemic:", "Talent Attraction, Retention and Development",
    "Purpose and Culture. We strive to differentiate ourselves by our culture and talent. How we manage our human capital is critical to how we deliver on our strategy and create sustained growth and value for our shareholders. Our purpose is to improve the lives of our team members, customers and shareholders, one experience at a time. We recognize a great culture is foundational to the success of this vision. Key components in managing our human capital are listed below.",
    "Engagement & Sentiment","Health and Well-Being",
    "Employee Engagement & Training and Development"," Employee Compensation and Benefits:","Well-being and Development ",
    "Our Compensation Practices","Wellness ","Associate Engagement.","Investment in Talent","Employee Growth and Development"
    # Part 3
    "Promoting an Inclusive Culture Through Learning Opportunities.",
    "Training and Development", "Employee Health and Safety",
    "Employee engagement – Create a workplace that fosters an engaged, high-quality workforce. PPL’s operating companies regularly conduct assessments related to employee engagement, safety and culture. Senior management reviews corporate culture with the Board annually.",
    "Safety","Employee Incentives","Talent Pipeline and Career Development","Compensation and Wellness",
    "Safety. ",
    "Headcount.","Human Capital Risks","Talent Management:",
    "Talent Acquisition, Retention and Development","Employee Compensation and Benefits",
    "Talent Development.  ","Corporate Social Responsibility ", "Corporate Social Responsibility",
    "Ethics and Compliance. We take pride in the high standards of conduct that identifies us as a company. We have controls in place relating to compliance with our Code of Business Conduct and Ethics (“Code”), including a requirement for employees to review and understand the requirements of our Code, as well as an established whistleblower hotline and related procedures.",
    "Management Team ", "Recruiting, Retaining and Engaging Employees and Learning and Development",
    "Employee Recruitment, Development and Retention",
    "Employee Wellness Initiatives",
    "Competitive Pay/Benefits and Pay for Performance Philosophy: TTEC compensation programs are designed to align compensation of our employees to market, and to provide appropriate incentives to attract, retain and motivate employees to achieve exceptional results for our clients and our shareholders. Our pay-for-performance philosophy aligns our compensation with TTEC’s performance and with the returns that our stockholders receive from their investment in the Company. Further, TTEC provides employees with a comprehensive benefits program that includes nicotine abatement, mental health initiatives, and overall wellness programs to support employees’ physical, emotional, and financial health.",
    "Learning & Development","Governanc","COMPANY CULTURE","Labor Relations.",
    "Career satisfaction and skills","Engagement","Table of Contents ","Talent","Competitive Pay","Employee Wellness and Benefits ",
    "Training and Education.","Compensation and Human Capital ",
    "Fair Labor Practices: We seek fair labor practices throughout our business, including from our partners and key suppliers who share our values for human rights, dignity, and respect. We have implemented a Supplier Code of Conduct requiring the same commitment to human rights, fair labor practices, and anticorruption that we value at Tactile Medical. ",
    "Health & Safety. ","Compensation ","Employee Development","Employee engagement. ",
    "Culture & Employee Engagement","Talent development.","Employee Safety",
    "COVID-19 Response","Engagement and Opportunities","Compensation, Benefits and Well-being",
    "Learning and Development",
    "Environmental, Social and Governance (“ESG”)","Employee Well-Being","Talent Acquisition",
    "IDACORP FINANCIAL SERVICES, INC.","Employee Engagement ","Recruiting and Retention", "Acting with Integrity",
    "Commitment to Values and Ethics","Employee Engagement.","Compensation programs and employee benefits:",
    "Compensation and Benefits. The Company believes in maintaining progressive employment policies, as well as a competitive wage and benefit package.The Company has invested heavily in its officers and associates by recruiting talented officers in its market areas and providing them with economic incentives. The senior management team has substantial experience in the Company’s market areas and the surrounding communities in which the Company has a presence. Most banking center locations are overseen by a local president or manager with knowledge of the community and lending expertise in the specific industries found in the community. The Company operates each banking center as a separate profit center, maintaining separate data with respect to each banking center’s net interest income, efficiency ratio, deposit growth, loan growth and overall profitability. Banking center presidents and managers are accountable for performance in these areas and compensated accordingly. ",
    "Utilization of Independent Contractors and Referring Representatives.",
    "Talent Acquisition, Development and Promotion",
    "Compensation and Benefit Programs. We are committed to providing our employees with a competitive compensation package that rewards performance and achievement of desired business results.  Our compensation package consists of three primary benefits: pay (base pay and incentive programs), health and welfare benefits, and retirement contributions.  We analyze our compensation and benefits programs annually to ensure we remain competitive and make changes as necessary.",
    "Employee Attraction and Retention", "Hiring and Sustaining our Workforce","Health, Safety and Well-Being","Labor relations",
    "Attraction, Development and Retention", "Employee Communication and Engagement. ","Hiring ", "Financial, Health and Mental Well-Being",
    "Harassment Prevention","Index to Financial Statements","Focusing on a safe and healthy workplace.  ","Recruitment and Retention",
    "Communications and Engagement", "Training and Development. ","Training and Professional Development",
    "Compensation, Benefits, Health, Safety and Wellness","Health and safety policies adopted during the COVID-19 pandemic",
    "Health, Safety and Wellness","Employee Wellness and COVID-19 Response", "Health and Safety","Training and Talent Development",
    "Recruiting & Hiring Practices","Giving Programs. ","Workplace Safety","Impact of COVID-19",
    # Part 4
    "Hiring, Training and Development of our Workforce","Compensation and Benefits Programs","Development Opportunities",
    "Employee and Leadership Development",
    "Development and Training - The Company’s management team and all its employees are expected to exhibit and promote honest, ethical and respectful conduct in the workplace. We have implemented and maintained a corporate compliance program to provide guidance for everyone associated with the Company, including its employees, officers and directors (the \"Code\"). Annual review of the Code is required which prohibits unlawful or unethical activity, including discrimination, and directs our employees, officers, and directors to avoid actions that, even if not unlawful or unethical, might create an appearance of illegality or impropriety. In addition, the Company provides annual training for preventing, identifying, reporting and stopping any type of unlawful discrimination.",
    "Compensation and Benefits.","Workforce Compensation & Pay Equity","Health and Wellness","Employee Engagement",
    "Compensation, Benefits and Well-being",
    "Our enterprise-wide I&D priorities include the following:","Team Member Engagement","Community Outreach",
    "For more information, please refer to our current Corporate Citizenship & Sustainability Report, which is available on our website at ",
    "Employee Retention.  We compete in an industry that is highly competitive for talent. Attracting, developing and retaining skilled people in sales, technical and other positions is crucial to executing our strategy and our ability to compete effectively. While we monitor overall employee retention, we focus in particular on sales representative retention, as our new sales and revenue growth are driven almost entirely by the sales generated by our direct sales force.   As a complement to our sales representative retention metric, we also closely track the pace of hiring new sales representatives.",
    "Crewmember Programs","Employee Engagement:","Board Diversity.","Employee Engagement","Hiring & Retention ",
    "Talent Development and Retention ","Support of Human Capital in Response to COVID-19","Training and Talent Management",
    "Employees","Talent Acquisition, Retention and Stability","Restaurant Management","Total Rewards ",
    "Employee Wellness","Recruiting","Engagement.","Health and safety","Freedom of Association and Collective Bargaining.",
    "Recruiting, Retention, and Talent Development","Professional Development and Training","Employee Development ",
    "Safety. “Safety Always” is one of our core, foundational values. We strive to create a culture of safety that promotes transparency and accountability by providing the tools and resources that empower our people to identify and report potential hazards and stop work when ",
    "Environmental, Social and Governance (“ESG”)","Talent, development, and training",
    "Pay Equity ",
    "•greater financial and human capital resources;",
    "Employee Remuneration and Benefits",
    "Discrimination and Harassment. As set forth in our Code and our discrimination and harassment policy, we have a zero-tolerance policy on discrimination and harassment and have several methods under which employees can report incidents, including an online and telephone hotline through which employees can report any discrimination and harassment or any other compliance and ethics concerns confidentially or anonymously and without fear of reprisal.",
    "Conduct and Ethics",
    "We also consider it critical to our success to invest in the professional development of all of our associates. We emphasize our commitment to professional development through opportunities such as technical, skills-based, management, and leadership training programs; formal talent and performance management processes; and sustainable career paths. We also aim to prepare our workforce for a rapidly changing environment and understand that reskilling and upskilling are crucial to staying competitive, meeting the needs of the modern workforce, and retaining associates. We’ve established a customized learning experience platform that provides the tools to measure, build, and communicate skills inside the Company. This tool provides the ability to inventory the skills our associates have, allowing us to target our development efforts on specific areas where elevated skills are needed. Regions also offers a leader and manager development program created to help people managers understand how to evaluate performance by leveraging the power of a strengths-based and engagement-focused workforce and culture.",
    "Training and Professional Development: ","Regulation ",
    "We were recently recognized as a “Best Place to Work in Money Management” by Pensions & Investments (“P&I”), the international newspaper of money management. The 2020 award was part of P&I’s ninth-annual survey and recognition program, which seeks to identify the best employers in the money management industry. This achievement recognized the strength of our culture, which is defined by the hard work, dedication, and commitment to excellence and inclusion by everyone at the Company.",
    "Development, Training and Retention","Website Access to Company Reports",
    "Compensation Philosophy","Risks Related to Human Capital Resources","Ethical Standards",
    "Training and Talent Development: We provide technical and leadership training to employees at both the officer and non-officer levels. The Company has also launched a learning management system for tracking training hours for its employees.",
    "Health and safety","Recruiting our Employees","Index to Financial Statements","COVID-19 Update",
    "Subsidized child care programs for employees, including access to onsite centers in Las Vegas;",
    "Compensation Programs and Employee Benefits","Employee","Benefits.",
    "Personal Well-Being. The Company invests in the well-being of our employees by offering benefits intended to meet the varied and evolving needs of our diverse workforce across businesses and geographies. The Company addresses this through its Work to Wellness program, a global initiative that educates, motivates and empowers employees to maintain a healthy lifestyle in and out of the workplace. We offer a wide range of resources to support employees and their families’ emotional and financial well-being. We have also made investments in technology that enable remote and hybrid working options.",
    "Employee Recruiting","Employee Engagement and Wellness","COVID-19 Response:","Total Rewards. ",
    "Workforce Health and Safety."," COVID-19 Response","Labor and Ethics ",
    "Employee Safety and Health.The health and well-being of our employees is a priority for our business. Our full-time officers and employees are provided hospitalization and major medical insurance. We pay a substantial part of the premiums for these coverages. We also provide other basic insurance coverage including dental, life, and long-term disability insurance.",
    "Training and Personal Development","Talent Acquisition, Development, and Retention:",
    "Description of Certain Indebtedness","Equitable Foundation","Safety and Wellness",
    #"Employee Growth and Development. We invest significant resources to develop the talent needed to remain a leader in the industry and an employer of choice.We have formal and informal programs to develop our workforce through employee improvement and professional growth. Additionally, succession planning is critical to ensuring that we have the right people in the right position at the right time. We conduct annual succession planning meetings across the organization starting with our local operations and rolling up to our division and corporate levels including our executive team. As part of our succession planning and commitment to developing talent, we conduct an annual leadership training program to build bench strength at the supervisor and management level. ",
    "Board Composition and Refreshment","Employee Engagement and Retention:",
    "Health and Safety. As a result of the spread of COVID-19, most local, state and federal governmental agencies have imposed travel restrictions and local quarantines or stay at home restrictions to contain the spread. In an effort to minimize the risk of COVID-19 to employees working for our consolidated subsidiaries and the communities in which they operate, the Company mandated that all non-essential employees work from home. For employees who need to perform their jobs on-site, including warehouse and studio production teams at our consolidated subsidiaries, the Company took precautions to protect their health and safety. This included reducing the number of people on-site to allow for more social distancing; limiting visitors and screening all people who come into the Company’s work sites; in addition to elevated cleaning protocols in alignment with the recommended protocols from the Centers for Disease Control and Prevention. Our consolidated subsidiaries have also taken measures to support their employees’ ability to make a living. In addition to offering flexible hours and expanding work-at-home policies, our consolidated subsidiaries have made changes to their attendance policies and are offering additional paid time off options to support certain COVID-19 related absences. Additionally, our consolidated subsidiaries have expanded programs to support their employees, including alternative work arrangements to help families juggling competing work and personal challenges, greater access to home care help, added resources to support mental health, and paid special bonuses for many employees, among a number of other initiatives.",
    "COVID-19employee safety and benefits","Talent Development: ","Provide Programs for Employee Recognition","Competitive Pay/Benefits",
    "Talent Management","Compensation, Benefits, and Wellness","Employee Compensation, Benefits & Wellbeing",
    "Social, Environmental, and Community Responsibility  ","Compensation and benefits.","Career Development",
    "Human Capital Management in Response to COVID-19","Performance and Career Development",
    "Employee Engagement.  We prioritize employee engagement and value employee feedback.In 2020, approximately 80% of Altra team members responded to and participated in our employee engagement survey.The survey enables us to monitor engagement and results serve as a guide to establish initiatives aimed to enhance the employee experience and analyze efficacy of those initiatives year over year.In addition to our company-wide engagement survey, our businesses also conduct localized, periodic reviews and pulse surveys to gauge employee satisfaction, obtain employee feedback of specific issues on initiatives, and identify shortfalls and opportunities for improvement.",
    "Organizational Development—Our Human Resources team is focused on providing training to our local sales team to provide our salespeople with the skills and confidence to sell larger contracts at a faster pace. With the exception of the current year due to the COVID-19 Pandemic, this training consists of in-person instruction. Managers and supervisors also participate in specialized training to develop management skills, encourage employee development and retention and assist the Company with succession planning by identifying top talent to be developed into future leaders. Our Human Resources department also regularly provides employees with mandatory compliance training regarding workplace diversity, our code of conduct, password management, cyber security and other personnel related courses to help them with their daily responsibilities. Compliance with mandatory training requirements is tracked by our Human Resources department and management is notified when the requirements are not met. ",
    "Health and Safety/Well-Being","Compensation and Pay Equity","Retention, Training and Development",
    "Health, safety, and wellness. ","Compensation, Health and Wellness","shareholder return performance","Employees ",
    "Independent Sales Agents","Oversight and Management",
    # Part 5
    "Giving Our People a Voice","Training & Developmen",
    "Employee Health & Safety. Allison’s overriding priority is to protect the health and safety of each employee. As part of our health and safety programs, employees participate in training focused on this topic and metrics are reviewed regularly, including the number of injury incidents that occur and those incidents that result in lost work days. For 2020, we achieved an overall recordable rate of 1.53, meaning that for every 100 employees, 1.53 employees incurred an injury that resulted in recordable medical treatment and the number of lost work days was 0.28, meaning that for every 100 employees, 0.28 individuals experienced an incident that resulted in days away from work.",
    "Flexibility and Decentralization.",
    "Workplace safety: We believe that all accidents and injuries at work are preventable and we aim to ensure a zero-injury culture across our offices and operations. We comply with applicable occupational health and safety regulations and are certified to Occupational Health and Safety Quality Management Standard ISO 45001:2018. Our injury rates are low. "
    "Employee Benefits"
]

i_start_word_list = [
    "Diversity"
]
i_nxt_word_list = [
    "Development"
]

''''
Did not include in d/i keys:
part2.json- 731012, 742112, 814453, "874238", "875320", "898437", "910329","912562","914208"
part3.json- 
part4.json - "1178711"
'''


"""
Questionable:
"818479
"820027"
"860413"
"""


"""
Did not do yet:

"1212545" - stopped for here today
"""


"""
Note:
"893949"- got rid of the "25 "
"1163165"- As of 02/27/2022, I do need to get rid of the "20 "!!!!!!!!!!!!!!!!!!!!!
Other than that, I have some feeling about dioutput.json that it is not totally correct.
"""


"""
This was not scraped properly or cleaned properly and it did have a d/i section and I did not include it in my code:
"926282"- I realized that in the part 3 json file, my code took out a good chunk of the code.-> actually this is due to scraping
"1026214" - This was not scraped properly, going to have to manually take it out->As of 02/27/2022 resolved it by hard coding
"1274173"- This was not scraped properly. Some information is missing, therefore, I could not scape it-> I did include it, but it is still missing info
"1378950" - this was not scraped properly.
"1404655"- this was not scraped properly.
"""