string = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can"

extractedList = []
i = 1
AtomicSymbols = dict()
for i,word in enumerate(string.split(),1):
  if(i in [1,5,6,7,8,9,15,16,19]):
    AtomicSymbols[word[:1:]]= i
  else:
    AtomicSymbols[word[:2:]] = i
  i+=1
  
print(AtomicSymbols)