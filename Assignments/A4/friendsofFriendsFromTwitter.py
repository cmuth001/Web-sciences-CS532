import tweepy
import csv
ckey="v5YfpnUYDpYFrm9hn4wfV6hCw"
csecret="2nOHkJyPqteSudHrlS8YWcsuK8wvX7AgIPVIK8ySHj3dU5TnF6"
atoken="956029983469776897-GUROfj1hmnuImgewZAZrKAog5dJ1q3O"
asecret="UipAVctbQJUQEczQ2s7Dd5J3teLa6ZwEAWWbaceTSSfca"
# OAuth process, using the keys and tokens
auth = tweepy.OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

# Creation of the actual interface, using authentication
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True, compression=True)
screenName = "hemanthmalla"
myFriends = 0
myfollowers = 0
with open('friendsCount.csv', 'w',newline='') as csvfriends:
	fieldnames  = ['USER', 'FRIENDCOUNT']
	writerriends = csv.DictWriter(csvfriends, fieldnames=fieldnames)
	writerriends.writeheader()
	for friend in tweepy.Cursor(api.friends, screen_name=screenName).items():
		myFriends += 1
		writerriends.writerow({'USER': friend.screen_name, 'FRIENDCOUNT':friend.friends_count})
		print(friend.screen_name,":",friend.friends_count)
	writerriends.writerow({'USER': screenName, 'FRIENDCOUNT':myFriends})	

with open('followersCount.csv', 'w',newline='') as csvfollowers:
	fieldnames  = ['USER', 'FOLLOWERSCOUNT']
	writerfollowers = csv.DictWriter(csvfollowers, fieldnames=fieldnames)
	writerfollowers.writeheader()
	for follower in tweepy.Cursor(api.followers, screen_name=screenName).items():
		myfollowers +=1
		writerfollowers.writerow({'USER': follower.screen_name, 'FOLLOWERSCOUNT':follower.friends_count})
		print(follower.screen_name,":",follower.friends_count)
	writerfollowers.writerow({'USER': screenName, 'FOLLOWERSCOUNT': myfollowers})


print("myFriends: ", myFriends, "myfollowers: ",myfollowers)