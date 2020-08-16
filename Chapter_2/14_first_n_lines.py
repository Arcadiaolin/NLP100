import pandas

def readFirstNlines(n):
  df = pandas.read_table("resource\popular-names.txt",header=None,names=['name','sex','count','birth'])
  print(df.head(n))

readFirstNlines(10)

# head -n 5 ./popular-names.txt