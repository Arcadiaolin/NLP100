import pandas as pd

col1 = pd.read_table("Chapter_2\col1.txt",names=["name"],header=None)
col2 = pd.read_table("Chapter_2\col2.txt",names=["sex"],header=None)

mergedCols = pd.concat([col1,col2],axis=1)

mergedFile = open("Chapter_2/mergedFile.txt",'w')
mergedCols.to_csv(mergedFile,sep = '\t',index=None,line_terminator='\n')
mergedFile.close()

# paste ./col1.txt ./col2.txt