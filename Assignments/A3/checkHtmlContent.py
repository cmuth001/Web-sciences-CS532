
import urllib.request
import hashlib
import os, errno
import csv
from boilerpipe.extract import Extractor
count = 1

# creating directory  for out to store files
def createDirectories():
	if not os.path.exists('output'):
		try:
			os.makedirs('output')
		except OSError as e:
			if e.errno != errno.EEXIST:
				raise
	if not os.path.exists('output/rawHtml'):
		try:
			os.makedirs('output/rawHtml')
		except OSError as e:
			if e.errno != errno.EEXIST:
				raise
	if not os.path.exists('output/processedHtml'):
		try:
			os.makedirs('output/processedHtml')
		except OSError as e:
			if e.errno != errno.EEXIST:
				raise

with open('finalurls.txt') as fp:
	createDirectories();
	with open('output/hashedUrls.csv', 'w') as csvfile:
		fieldnames  = ['url', 'key']
		writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
		writer.writeheader()

		for line in fp:
			md5value = hashlib.md5(line.strip().encode('utf-8')).hexdigest()
			writer.writerow({'url': line.strip(), 'key': md5value})
			print(count,":",md5value)
			count =count+1
			try:
				rawhtml = urllib.request.urlopen(line.strip()).read()
				with open('output/rawHtml/%s.html' % md5value, 'w+', encoding='utf-8' ) as rawf:
					print(rawhtml, file=rawf)

				extractor = Extractor(extractor='ArticleExtractor', html=rawhtml)
				htmlText=extractor.getText()
				with open('output/processedHtml/%s.txt' % md5value, 'w+', encoding='utf-8' ) as processedf:
					print(htmlText, file=processedf)
					# print(htmlText)
			except KeyboardInterrupt:
				exit()
			except:
				pass