import pandas as pd
from IPython.display import display

dataFrame = pd.read_csv("resource\popular-names.txt",names=['name','sex','count','birth'],header=None)
# display(len(dataFrame.drop_duplicates(subset='name')))

# dataFrame = dataFrame.drop_duplicates(subset=['name'])
display(dataFrame)
# print(len(dataFrame.drop_duplicates(subset=['name'],)))