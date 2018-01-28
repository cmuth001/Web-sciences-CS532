from bs4 import BeautifulSoup
import urllib.request
with urllib.request.urlopen("https://www.odu.edu/") as res:
	redditHtml = res.read()
	soup = BeautifulSoup(redditHtml, "html.parser")
	for links in soup.find_all('a'):
		#print(res.url)
		print(links.get('href'))
