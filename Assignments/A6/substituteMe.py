import csv
from pprint import pprint as pp
def substituteUsers():
	
	users = []
	with open("dataset/u.user") as csvFile:
		lines = csv.reader(csvFile, delimiter='|')
		for line in lines:
			age = 24
			gender = 'M'
			occupation = 'engineer'
			if age == int(line[1]) and gender == line[2] and occupation == line[3] and len(users)<3:
				users.append(line)


	return users
def getMoviereviews(userIds):
	reviews = {}
	for i in userIds:
		reviews[i] = []
		with open("dataset/u.data") as csvFile:
			lines = csv.reader(csvFile, delimiter = "	")
			for line in lines:
				if i == line[0]:
					reviews[i].append(line)
	return reviews
def findMovie(movieId):
    with open("dataset/u.item", 'r') as f:
        reader = csv.reader(f, delimiter='|')
        for i in reader:
            itemId = i[0]
            if movieId == itemId:
                # id, name, URI
                return (i[0], i[1], i[4])


def findMoviesMerge(reviewDict):
    userMovieDict = {}
    for userId, reviews in reviewDict.items():

        userMovieDict[userId] = {}
        moviesReviewed = []
        botMovies = []
        topMovies = []
        for r in reviews:
            movieId = r[1]
            rating = r[2]

            movie = findMovie(movieId)
            movie = tuple(rating) + movie
            moviesReviewed.append(movie)

        # botMovies.sort(key=lambda tup: tup[0])
        moviesReviewed.sort(key=lambda tup: tup[0])
        botMovies = moviesReviewed[:3]
        topMovies = moviesReviewed[-3:]
        userMovieDict[userId]["bottomMovies"] = botMovies
        userMovieDict[userId]["topMovies"] = topMovies

    return userMovieDict




if __name__ == '__main__':
	selectedUsers = substituteUsers()
	userIds = []
	for user in selectedUsers:
		userIds.append(user[0])
	userMovieReviews = getMoviereviews(userIds)
	with open("dataset/closestUsers.txt", 'w') as f:
		pp(findMoviesMerge(userMovieReviews), stream=f)