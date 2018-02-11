import requests
import csv
import json
import os, errno
mementos = {}
lineNo=1
class extractMementos:
	def collectmementos(self):
		global mementos
		global lineNo
		with open('test.txt') as fp:
			for line in fp:
				try:
					url = 'http://memgator.cs.odu.edu/timemap/json/'+line.strip()
					responsed = requests.get(url, stream=True,headers={'User-Agent':'Mozilla/5.0'})
					mementoCount = responsed.headers['X-Memento-Count']
					print("status:",responsed.status_code,"m:",mementoCount)
					if not os.path.exists('urlMementos'):
						try:
							print('foldercreated')
							os.makedirs('urlMementos')
						except OSError as e:
							if e.errno != errno.EEXIST:
								raise

					if responsed.status_code==200:
						with open('urlMementos/timemap%s.txt' % lineNo, 'w+') as outfile:
							json.dump(responsed.json(), outfile,indent=4, sort_keys=True,ensure_ascii=False)
							lineNo = lineNo+1

					# else:
					# 	print('else-404')
					# 	with open('outputPut/timemap%s.txt' % lineNo, 'w+') as outfile:
					# 		print('else-file',lineNo)
					# 		#print(responsed.headers)
					# 		outfile.write(responsed.headers)
					# 		lineNo = lineNo+1
					# 		print('l-no',lineNo)

					if mementoCount in mementos:
						mementos[mementoCount] = mementos[mementoCount]+1
					else:
						mementos[mementoCount] = 1
					print("memento:",mementos)
				except KeyboardInterrupt:
					exit()
				except:
					
					pass
obj=extractMementos()
obj.collectmementos()
with open('testMementos.csv', 'w') as csvfile:
	fieldnames  = ['mementos', 'count']
	writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
	writer.writeheader()
	for key,value in mementos.items():
		writer.writerow({'mementos': key, 'count': value})
		print (key, value)

