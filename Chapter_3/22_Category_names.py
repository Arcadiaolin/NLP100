import pandas as pd
import re

JSON_PATH = "resource\jawiki-country.json.gz"

# dataFrame = pd.read_json(JSON_PATH,lines=True)

# UKText = dataFrame.query('title=="イギリス"')['text'].values[0]
# UKTexts = UKText.split('\n')

# answers = list(filter(lambda x: '[Category:' in x, UKTexts))

# print(answers)


import pandas as pd
import re
pattern = re.compile('Category')
wiki = pd.read_json(JSON_PATH, lines = True)
uk = wiki[wiki['title']=='イギリス'].text.values
ls = uk[0].split('\n')
for line in ls:
    if re.search(pattern, line):
        line = line.replace('[[','').replace('Category:','').replace(']]','').replace('|*','').replace('|元','')
        print (line)