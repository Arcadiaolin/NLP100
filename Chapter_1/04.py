sentence = "I am an NLPer"

def nGramWord(string,n):
  string = string.split()
  return[string[i:i+n] for i in range(len(string)-n+1)]

print(nGramWord(sentence,2))