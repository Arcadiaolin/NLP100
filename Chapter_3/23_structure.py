import pandas as pd
import re

JSON_PATH = "resource/jawiki-country.json.gz"

pattern = re.compile('^=+.*=+$')  # 1回以上の=で始まり、1回以上の=で終わる文字列
wiki = pd.read_json(JSON_PATH, lines=True)
uk = wiki[wiki['title'] == 'イギリス'].text.values
ls = uk[0].split('\n')
for line in ls:
  # print(line)
    if re.search(pattern, line):
        level = line.count('=')
        print(line.replace('=', ''), level)
