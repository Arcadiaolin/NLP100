string = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can"

extractedList = []
i = 1
extractedString = ''
for word in string.split():
  if(i in [1,5,6,7,8,9,15,16,19]):
    extractedString += word[:1:]
  else:
    extractedString += word[:2:]
  i+=1
print(extractedString)