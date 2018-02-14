'''
	prerequisites:
	0. create a twitter account
	1. obtain your access tokens: https://apps.twitter.com/
		1.0 create new app
	2. install tweepy (pip install tweepy)

	credit: 
	http://docs.tweepy.org/en/v3.4.0/streaming_how_to.html
	http://adilmoujahid.com/posts/2014/07/twitter-analytics/
	https://pythonprogramming.net/twitter-api-streaming-tweets-python-tutorial/

	Tweet JSON:, use http://jsonviewer.stack.hu/ to view object
	https://developer.twitter.com/en/docs/tweets/data-dictionary/overview/intro-to-tweet-json

	rate limiting:
	https://developer.twitter.com/en/docs/basics/rate-limiting

	streaming rate limiting:
	https://developer.twitter.com/en/docs/tweets/filter-realtime/guides/connecting.html
'''

#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json
import time
import requests
from urllib.error import  URLError
from http.client import IncompleteRead
# import http.client

#get keys from: https://apps.twitter.com/
#consumer key, consumer secret, access token, access secret.
ckey="v5YfpnUYDpYFrm9hn4wfV6hCw"
csecret="2nOHkJyPqteSudHrlS8YWcsuK8wvX7AgIPVIK8ySHj3dU5TnF6"
atoken="956029983469776897-GUROfj1hmnuImgewZAZrKAog5dJ1q3O"
asecret="UipAVctbQJUQEczQ2s7Dd5J3teLa6ZwEAWWbaceTSSfca"
MyUniqueLinks = []
class listener(StreamListener):
	global MyUniqueLinks
	def on_data(self, data):
		#learn about tweet json structure: https://developer.twitter.com/en/docs/tweets/data-dictionary/overview/intro-to-tweet-json
		tweetJson = json.loads(data)
		links = tweetJson['entities']['urls']
		if( len(links) != 0 and tweetJson['truncated'] == False ):
			links = self.getLinksFromTweet(links)
			for l in links:
				if l not in MyUniqueLinks:
					if len(MyUniqueLinks)<1001:
						MyUniqueLinks.append(l)
						print(l)
		return True

	def getLinksFromTweet(self, linksDict):
		links = []
		for uri in linksDict:
			try:
				responsed = requests.get(uri['expanded_url'], stream=True,timeout=5,allow_redirects=True,headers={'User-Agent':'Mozilla/5.0'})
				intialStatus = responsed.status_code
				if intialStatus==200 and responsed.headers['content-type'] != None:
					if(responsed.history):
						if "twitter.com" not in responsed.url:
							links.append(responsed.url )
					else:
						if "twitter.com" not in uri['expanded_url']:
							links.append( uri['expanded_url'] )
				if(responsed.history):
					if "twitter.com" not in responsed.url:
						links.append(responsed.url )
			except KeyboardInterrupt:
				exit()
			except:
				pass

		return links

	def on_error(self, status):
		print( status )
		
		if status_code == 420:
			#returning False in on_data disconnects the stream
			return False
		return True

		
auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

twitterStream = Stream(auth, listener())
twitterStream.filter(track=['football','cricket'])