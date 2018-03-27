import json, requests
import yaml
import csv
# data = ''
count = 0
imdbRating = {}

movieLensDataRating = {}
keys = {'Rating':0.0, 'count':0}
for line in open('dataset/u.data'):
	item = line.split('\t')
	# print(item[1])
	movieLensDataRating[item[1]] = []
	movieLensDataRating[item[1]].append(0.0)
	movieLensDataRating[item[1]].append(0)
	# print(movieLensDataRating)

for line in open('dataset/u.data'):
	item = line.split('\t')
	print(item[1],item[2])
	# print("before:",movieLensDataRating[item[1]])
	movieLensDataRating[item[1]][0] = movieLensDataRating[item[1]][0]+float(item[2])
	movieLensDataRating[item[1]][1] =movieLensDataRating[item[1]][1] + 1
	# print("after: ",movieLensDataRating[item[1]])
for key,value in movieLensDataRating.items():
	try:
		print("before:",movieLensDataRating[key][0],movieLensDataRating[key][1])
		movieLensDataRating[key][0] = movieLensDataRating[key][0]/movieLensDataRating[key][1]
		print("after:",movieLensDataRating[key][0],movieLensDataRating[key][1])
		# print(movieLensDataRating[key]['Rating'],movieLensDataRating[key]['count'])
	except:
		pass

for line in open('dataset/u.item'):
	movieTitle = line.split("|")[1].split("(")[0].split(",")[0]
	count +=1
	try:
		url = 'http://www.omdbapi.com/?t='+movieTitle+'&apikey=74052bd2'
		# print(line.split("|")[1].split("(")[0].split(",")[0])
		resp = requests.get(url=url)
		# data = json.dump(resp.json(), file,indent=4, sort_keys=True,ensure_ascii=False)
		data = yaml.safe_load(resp.text)
		imdbRating[line.split('|')[0]] = {'movieId': line.split('|')[0], 'ImdbId': data['imdbID'], 'movieTitle':data['Title'],'Rating':data['imdbRating'],'imdbVotes':data['imdbVotes']}
		# print(imdbRating[line.split('|')[0]])
		# print(data['Title'],data['imdbRating'])
		# writer.writerow({'movieId': line.split('|')[0], 'ImdbId': data['imdbID'], 'movieTitle':data['Title'],'Rating':data['imdbRating']})
		
	except:
		pass



with open('dataset/test.csv', 'w') as csvfile:
	fieldnames = ['movieId', 'ImdbId','movieTitle', 'Rating','imdbVotes','movieLenseRating','movieLensUserCount']
	writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
	writer.writeheader()
	for key,value in imdbRating.items():
		try:
			if key in movieLensDataRating:
				print(movieLensDataRating[key])
				writer.writerow({'movieId': key, 'ImdbId': value['ImdbId'], 'movieTitle':value['movieTitle'],'Rating':value['Rating'], 'imdbVotes':value['imdbVotes'],'movieLenseRating':round(movieLensDataRating[key][0],2), 'movieLensUserCount':round(movieLensDataRating[key][1],2)})
		except:
			pass
# print(imdbRating)