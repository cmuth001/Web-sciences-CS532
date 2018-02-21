import os
from collections import Counter
import pandas as pd
import numpy as np
wordVector = {}
tf = {}
idf = {}
tfidf = {}
hashedUrls = {}

df = pd.read_csv('output/hashedUrls.csv', sep=',',header=None, skiprows=1)
with open("tenUrls.txt",'r') as file:
  lines = file.readlines()
  for line in lines:
    for index, row in df.iterrows():
      if row[1].strip()+".txt"==line.strip():
        # print(row[0])
        hashedUrls[line.strip()] = row[0]
        break

with open("tenUrls.txt",'r') as file:
	totalWordsInFile=0
	footballCount = 0
	lines = file.readlines()
	for line in lines:
		fileName = line.strip()
		# print(fileName)
		with open(os.path.join("output/processedHtml", fileName),'r',encoding='utf-8') as con:
  			wordcount = Counter(con.read().split())
  			for item in wordcount.items(): 
  				# print(item[0])
  				totalWordsInFile = totalWordsInFile+item[1]
  				if(item[0]=='football'):
  					footballCount = item[1]
  			wordVector={fileName:totalWordsInFile}
  			tf[fileName]=(footballCount/totalWordsInFile)
# print(tf)
for key, value in tf.items():
  idf[key] = np.log2(1000/345) #total number of files my search key words in 1000 urls
print("TFIDF","\t","TF","\t","IDF","\t", "URL")
for key,value in tf.items():
  tfidf[key] = tf[key]*idf[key]
  print(round(tfidf[key],4),"\t",round(tf[key],4),"\t",round(idf[key],4),"\t",hashedUrls[key])