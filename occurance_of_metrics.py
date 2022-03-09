
import re

def extract_number(s):
    num = []
    num.extend(re.findall(r'\d+,\d+', s))
    num.extend(re.findall(r'\d+\.\d+', s))
    num.extend(re.findall(r'\d+', s))
    try:
        num = [n for n in num if 
               (',' in n) or 
               ('.' in n) or 
               ('%' in n) or 
               (int(n) > 50 and                  # exclude numbers below 50...could mean page number or 'COVID-19'
                (int(n) < 1990 or int(n) > 2022) # exclude numbers referencing year
               )] 
        return num
    except:
        return []

def extract_dollar(s):
    dollar = []
    dollar.extend(re.findall(r'\$\s*\d+', s))
    return dollar

def extract_percentage(s):
    percents = []
    percents.extend(re.findall(r'\d+\.?\s?\d?%', s))
    percents.extend(re.findall(r'\d+\spercent', s))
    return percents

def is_metric_in_di_section(s):
    metrics = []
    metrics.extend(extract_percentage(s))
    metrics.extend(extract_dollar(s))
    metrics.extend(extract_number(s))
    if len(metrics) > 0:
        #return True
        return metrics
        #return len(metrics)
    #return False
    return 0