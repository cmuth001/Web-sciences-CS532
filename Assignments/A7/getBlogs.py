import requests


def getUniqueBlogs():
	file = open('100BlogUrls.txt','w') 
	uniqueBlogs = set()
	while (len(uniqueBlogs) < 100) : 
		
		try:
			url="http://www.blogger.com/next-blog?navBar=true&blogID=3471633091411211117"
			request = requests.get(url)
			final_url = request.url.strip('?expref=next-blog/')
			uniqueBlogs.add(final_url)
			# print final_url
			print len(uniqueBlogs)
		except:
			pass
	uniqueBlogs.add('http://f-measure.blogspot.com')
	uniqueBlogs.add('http://ws-dl.blogspot.com')
	uniqueBlogsList = list(uniqueBlogs)
	for i in range(0,len(uniqueBlogsList)):
		request = requests.get(uniqueBlogsList[i])
		rawhtml = request.content
		print uniqueBlogsList[i]
		#storing raw html content of 120 blogs in blogs in a sequence wise like 1.html, 2.html....
		rawf = open('blogs/%s.html' % str(i+1), 'w')
		rawf.write(rawhtml)
		# writing squence number of a blog and url of the blog in 100BlogUrls.txt file
		# For Example: 1.html<\t><blog_url_name>
		string = str(i+1)+".html	"+uniqueBlogsList[i]+"\n"
		file.write(string)

if __name__ == '__main__':
	getUniqueBlogs()

	