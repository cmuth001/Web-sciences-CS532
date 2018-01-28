import requests

def derefURI(uri):

	uri = uri.strip()
	if( len(uri) == 0 ):
		return ''

	html = ''
	#this is a lie
	headers = {
				'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:38.0) Gecko/20100101 Firefox/38.0',
				'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
				'Accept-Language': 'en-US,en;q=0.5',
				'Accept-Encoding': 'gzip, deflate',
				'Connnection': 'keep-alive',
				'Cache-Control':'max-age=0'	
			}

	try:
		response = requests.get(uri, headers=headers, timeout=10)
		html = response.text
	except Exception as e:
		#generic exception catch
		print('\tError:', str(e))

	
	return html

uri = 'http://www.cs.odu.edu/~anwala/'
print(derefURI(uri))
print('\nhtml done')