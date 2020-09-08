import pandas as pd

JSON_PATH = "resource\jawiki-country.json.gz"

dataFrame = pd.read_json(JSON_PATH,lines=True)

UKText = dataFrame.query('title=="イギリス"')['text'].values[0]
UKTexts = UKText.split('\n')

answers = list(filter(lambda x: '[Category:' in x, UKTexts))

print(answers)