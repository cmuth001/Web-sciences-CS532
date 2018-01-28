"""
	Assignment #1
	Due: 11:59pm January 28
	1) curl -i <web-site>
"""
import sys
from bs4 import BeautifulSoup
import urllib.request
from urllib.error import  URLError
import re
from urllib.parse import urlparse
class CrawlPdfFromWebsites:
	def __init__(self):
		self.title = "*** Extracting all the pdf's from a web-site. ***"
		self.vistitedLinks= []
		self.pdfList = []
		self.movedLinks = []


	def returnPdfs(self,url):
		print("returnPdfsUrl:",url)
		info = res.info()
		redditHtml = res.read()
		soup = BeautifulSoup(redditHtml, "html.parser")
		for link in soup.find_all('a'):
			if not bool(urlparse(link.get('href')).netloc):
				print("relativePath: ",url,link.get('href'))
				linkreq = url+link.get('href')
			else:
				print("normalUrl: ",link.get('href'))
				linkreq = link.get('href')
			res = checkValidURL(linkreq)
			if not res==None:
				if not link.get('href').startswith("#")  and not link.get('href')=="" and not link.get('href').startswith("?") :
					#and not link.get('href').startswith("/") check this
					linkRes = urllib.request.urlopen(linkreq)
					linkStatus = linkRes.getcode()
					linkContentType = linkRes.info().get_content_type()
					if linkStatus==200:
						if linkContentType == "application/pdf":
							pdfList.append(link.get('href'))
						elif linkContentType == "text/html":
							if  link.get('href') not in self.vistitedLinks:
								self.vistitedLinks.append(link.get('href'))
							else:
								print("vistitedLinks:",link.get('href'))
					elif linkStatus>=300 and linkStatus<400:
						if link.get('href') not in self.vistitedLinks and linkRes.geturl() not in movedLinks:
							self.vistitedLinks.append(link.get('href'))
							self.vistitedLinks.append(linkRes.geturl())
							#finalURL = getFinalURL(linkRes.geturl())
							self.movedLinks.append(linkRes.geturl())
						else:
							print("movedLinks:",link.get('href'))
	#def getFinalURL(self,url):


	def checkValidURL(self, url):
		print("checkValidURL:",url)
		req = urllib.request.Request(url)
		try:
			res = urllib.request.urlopen(req)
			return res
		except URLError as e:
			if hasattr(e, 'reason'):
				print('Reason: ', e.reason)
				pass
			elif hasattr(e, 'code'):
				print('Error code: ', e.code)
				pass

if __name__ == "__main__":

	obj = CrawlPdfFromWebsites()
	print(obj.title)
	print("Example, python <file_name> 'URL'(https:// or http://)")
	if(len(sys.argv) == 2):
		  print("Argument Received:")
		  url = sys.argv[1]
		  response = obj.checkValidURL(url)
		  if not response is None:
		  	listOfLinks = obj.returnPdfs(url)
		  else:
		  	print("Enter valid URL")


	else:
		print("Please provide URL along with file name.")
		# print("Example, python <file_name> 'URL'(https:// or http://)")