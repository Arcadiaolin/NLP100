import pandas as pd

df = pd.read_csv('./resource/popular-names.txt', header=None, sep='\t', names=['name', 'sex', 'number', 'year'])

col1 = open("./Chapter_2/col1.txt","w")
for i, lines in enumerate(df['name']):
  col1.write(lines + '\n')
col1.close()

col2 = open("./Chapter_2/col2.txt","w")
for i, lines in enumerate(df['sex']):
  col2.write(lines + '\n')
col2.close()

# cut -f 1 popular-names.txt > col1,txt
# cut -f 2 popular-names.txt > col1,txt