import random
testString = "I couldn’t believe that I could actually understand what I was reading : the phenomenal power of the human mind"

def shuffleMid(string):
  wordList = string.split()
  shuffledWordList = []
  for word in wordList:
    if(len(word) > 4):
      word = word[0] + ''.join((random.sample(word[1:len(word)-1],len(word)-2)))+word[-1]
      
    shuffledWordList.append(word)

  return ' '.join(shuffledWordList)

print(shuffleMid(testString))