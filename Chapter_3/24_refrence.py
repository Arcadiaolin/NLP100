import pandas as pd
import re
import configparser

config = configparser.RawConfigParser()
config.read('resource/config.txt')

JSON_PATH = config.get('PATH','JSON_PATH')
jsons = pd.read_json(JSON_PATH,lines=True)
uk = jsons[jsons['title'] == 'イギリス'].text.values
ls = uk[0].split('\n')

pattern = re.compile(r'File|ファイル:(.+?)\|')
# pattern = re.compile('File|ファイル:(.+?)\|')

for line in ls:
    target = re.findall(pattern,line)
    if target :
        print(target[0])

# import pandas as pd
# import re
# pattern = re.compile('File|ファイル:(.+?)\|')
# wiki = pd.read_json(JSON_PATH, lines = True)
# uk = wiki[wiki['title']=='イギリス'].text.values
# ls = uk[0].split('\n')
# for line in ls:
#     r = re.findall(pattern, line)
#     if r:
#         print (r[0])