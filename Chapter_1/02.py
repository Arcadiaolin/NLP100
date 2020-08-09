string = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics"
slicedString = string.split()

i = 1
newList =[]
letterCountList = []

for word in slicedString:
  replacedWord = word.replace(',','')
  newList.append(replacedWord)
  letterCountList.append(len(word))
print(newList,letterCountList)