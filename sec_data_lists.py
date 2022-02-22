


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