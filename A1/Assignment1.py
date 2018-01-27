
"""
	Assignment #1
	Due: 11:59pm January 28
	1) curl -i <web-site>

	1) "http://www.cs.odu.edu/~mweigle/"
	2) "http://www.cs.odu.edu/~mln/teaching/cs532-s17/test/pdfs.html"
	3) "http://www.cs.odu.edu/~yaohang/"
"""
import sys
from bs4 import BeautifulSoup
import urllib.request
from urllib.error import  URLError
from urllib.parse import urlparse
class Assignment1:
	def __init__(self):
		self.title = "*** Extracting all the Links from a web-page. ***"
		self.vistitedLinks= []
		self.pdfList = {}
		self.movedLinks = []
		self.linkList = []

	def printSysArguments(self):
		length = len(sys.argv)
		if length>1:
			self.siteUrl = sys.argv[1]
			print("URL: ",self.siteUrl)
	def returnPdfs(self, url):
		
		req = urllib.request.Request(url)
		try:
			res = urllib.request.urlopen(req)
			info = res.info()
			redditHtml = res.read()
			soup = BeautifulSoup(redditHtml, "html.parser")
			for link in soup.find_all('a'):
				if not link.get('href')==None:
					
					if not link.get('href').startswith("#") and not link.get('href')=="" and not link.get('href').startswith("?") :
						if not bool(urlparse(link.get('href')).netloc):
							finalUrl = url+link.get('href')
							linkreq = urllib.request.Request(url+link.get('href'))
						else:
							finalUrl = link.get('href')
							linkreq = urllib.request.Request(link.get('href'))
						try:
							linkRes = urllib.request.urlopen(linkreq)
							
							linkStatus = linkRes.getcode()
							linkContentType = linkRes.info().get_content_type()
							if linkStatus==200:
								if linkContentType == "application/pdf":
									self.linkList.append(finalUrl)
									self.pdfList[link.get('href')]=linkRes.headers['content-length']
								elif linkContentType == "text/html":
									# print(bool(urlparse(link.get('href')).netloc),": ",finalUrl)
									# print(linkRes.info())
									self.linkList.append(finalUrl)
									if  link.get('href') not in self.vistitedLinks:
										self.vistitedLinks.append(link.get('href'))
							elif linkStatus>=300 and linkStatus<400:
								if link.get('href') not in self.vistitedLinks and linkRes.geturl() not in movedLinks:
									self.vistitedLinks.append(link.get('href'))
									self.vistitedLinks.append(linkRes.geturl())
									self.movedLinks.append(linkRes.geturl())
									self.returnPdfs(linkRes.geturl())
						except URLError as e:
						    if hasattr(e, 'reason'):
						    	# print('Reason: ', e.reason)
						    	pass
						    elif hasattr(e, 'code'):
						    	# print('Error code: ', e.code)
						    	pass

		except URLError as e:
		    if hasattr(e, 'reason'):
		    	# print('Reason: ', e.reason)
		    	pass
		    elif hasattr(e, 'code'):
		    	# print('Error code: ', e.code)
		    	pass
					
		return self.pdfList

obj = Assignment1()
obj.printSysArguments()
listOfLinks = obj.returnPdfs(obj.siteUrl)
if(len(listOfLinks)>0):
	print("Pdfs in the links:")
	for link in listOfLinks:
		print("\t",link,":",listOfLinks[link])
else:
	print("Pdfs in the links: None")

print("All the links in the given link:")
for link in obj.linkList:
	print("\t",link)


