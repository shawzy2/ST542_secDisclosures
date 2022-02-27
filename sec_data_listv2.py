

non_element = [" ","","— ","•","    ",",",", ",": ",".","$",")","(a)","(b)", "(",
"                                           ","◦","■","▪"," — ","—","*","%", "®", "® ", "X","†","††", "•",", ",")%",
". ","​", " ", " (1)","﻿ ",""," —","–","-2-","I-12"," ","•13","**","\n\n\n\n\n \n\nGoldmanSachs2020Form 10-K\n\n5    ",
"\n\n13\n\n\n\n\n","\n13\n\n","25 ",":"]

di_v2_keys = [
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
    "895421","896159","896262","897448","898174","899051","899629","899866","901491","903129","906107"

]

di_v2_keys_s4 = [
    "811156","831259","850460","877212","887343","906107"
]
di_v2_keys_s4_1 = [
    "906107"
]
di_v2_keys_s4b = [
    "827052","875357"
]
di_v2_keys_s4c = [
    "860731"#,"877212"
]
di_v2_keys_s4d = [
    "867773","896159"
]
di_v2_keys_s4e = [
    "872589"
]# This will be used if the nt_word does apper more than once, but less than 2
di_v2_keys_s4f = [
    "877212"
]# This will be used if the nt_word does apper more than once, but less than 2


'''
"742112" - does have info about d/i, but no section title
'''

no_di_v2_keys = [
    "719739","720672","720858","723188","723646","726728","726854","727207","729580","729986","730272"
]

st_word = [
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
    "Diversity, Inclusion, and Belonging:"
]



nt_word = [
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
    "Labor Union Affiliations","Table of Contents","Preventing Harassment and Discrimination",
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
    "Employee Engagement","COVID-19 Pandemic:", "Talent Attraction, Retention and Development"
]

i_start_word_list = [
    "Diversity"
]
i_nxt_word_list = [
    "Development"
]

''''
Did not include in d/i keys:
731012
742112
814453
"874238"
"875320"
"898437"
'''


"""
Questionable:
"818479
"820027"
"860413"
"""


"""
Did not do yet:

 "880631"
"""


"""
Note:
"893949"- got rid of the "25 "

"""