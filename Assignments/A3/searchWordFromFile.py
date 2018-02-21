# Import the os module, for the os.walk function
import os
import re
# Set the directory you want to start from
rootDir = 'output/processedHtml/'
filesCount = 0
for dirName, subdirList, fileList in os.walk(rootDir):
	# print('Found directory: %s' % dirName)
	for fname in fileList:
		with open(os.path.join(dirName, fname),encoding="utf8") as openfile:
			lines = openfile.readlines()
			counter=0
			istaken= False
			for line in lines:
				if not istaken:
					for part in line.split():
						if re.match("football", part):
							# print("line: ",line)
							counter = counter+1
						if counter>10:
							istaken = True
							filesCount = filesCount+1
							print(fname)
							# print(filesCount,": ",fname)
							break
				else:
					break
