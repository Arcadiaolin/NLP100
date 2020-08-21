import pandas as pd

dataFrame = pd.read_csv("resource\popular-names.txt",names=['name','sex','count','birth'],header=None,encoding="UTF-8",delim_whitespace='\t')

print(dataFrame["name"].value_counts())