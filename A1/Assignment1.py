
"""
	Assignment #1
	Due: 11:59pm January 28
	1) "http://www.cs.odu.edu/~mweigle/"
	2) "http://www.cs.odu.edu/~mln/teaching/cs532-s17/test/pdfs.html"
	3) "http://www.cs.odu.edu/~yaohang/"
"""
#!/usr/bin/env python3
import sys
import requests
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
			print("Entered URL: ",self.siteUrl)
	def returnPdfs(self, url):
		try:
			responsed = requests.get(url)
			if(responsed.history):
				res = urllib.request.urlopen(responsed.url)
				print("Final URL:",responsed.url)
			else:
				res = urllib.request.urlopen(url)
				print("Final URL:",url)

			intialStatus = responsed.status_code
			if(intialStatus==200):
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
if(len(sys.argv)==2):
	obj.printSysArguments()
	listOfLinks = obj.returnPdfs(obj.siteUrl)
	if(len(listOfLinks)>0):
		print("Pdfs in the link:")
		for link in listOfLinks:
			print("\t",link,":",listOfLinks[link]," Bytes")
		for link in obj.movedLinks:
			print("moved:", link)
	else:
		print("Pdfs in the link: None")

	print("All the links in the given link:")
	for link in obj.linkList:
		print("\t",link)

else:
	print("Please provide URL along with file name.")


