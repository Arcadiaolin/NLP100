newFile = None
nLine = 300

with open("resource\popular-names.txt") as popNames:
  for lineNumber, line in enumerate(popNames):

    if (lineNumber % nLine == 0):
      if newFile:
        newFile.close()
      smallFileName = "pop_names_{}.txt".format(lineNumber + nLine)
      newFile = open(smallFileName,'w')
    newFile.write(line)
  if newFile:
    newFile.close()
