string1 = "paraparaparadise"
string2 = "paragraph"

def nGram(string,n):
  return tuple(string[i:i+n] for i in range(len(string)-n+1))

X = set(nGram(string1,2))
Y = set(nGram(string2,2))

print(X)
print(Y)

print(sorted(X.union(Y)))

# sorted(X.union(Y))