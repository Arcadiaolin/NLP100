import pandas

def readLastNLines(n):
  df = pandas.read_table("resource\popular-names.txt",header=None,names=['name','sex','count','birth'])
  print(df.tail(n))

readLastNLines(10)

# tail -n 5 ./popular-names.txt