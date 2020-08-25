import json

JSON_PATH = "./resource\jawiki-country.json"

def extractNewsAboutEngland(filePath):
  newsAboutEngland = list()

  with open(filePath,'r',encoding='UTF-8') as jsonFile:
    countLine = 0
    for line in jsonFile:
      jsonDate = json.loads(line)
      if jsonDate['title'] == "イギリス":
        newsAboutEngland.append(jsonDate["text"])

  return newsAboutEngland

for element in extractNewsAboutEngland(JSON_PATH):
  print(element)