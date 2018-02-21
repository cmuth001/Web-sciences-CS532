import urllib.request
count = 1
with open('finalurls.txt') as fp:
	for line in fp:
		try:
			res = urllib.request.urlopen(line.strip())
			print(count,":",res.getcode(),line.strip())
			count = count+1
		except KeyboardInterrupt:
			exit()
		except:
			print(count,"-1:",res.getcode(),line.strip())
			count = count+1
			pass