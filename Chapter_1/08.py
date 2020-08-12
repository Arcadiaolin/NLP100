def cipherC(string):
  if ('c' in string):
    string = string.replace('c',chr(219))
  return string

def deCipherC(string):
  if (chr(219) in string):
    string = string.replace(chr(219),chr(99))
  return string

print(cipherC("I am a cipher"))