import matplotlib.pyplot as plt
import pandas as pd 
points = [[3,9],[4,8],[5,4]]

df  = pd.read_csv('dataset/test.csv').dropna()
df1 = df.copy()
df2 = df.copy()
df1 = df1.sort_values(by=['Rating', 'imdbVotes'])
df2 = df2.sort_values(by=['movieLenseRating', 'movieLensUserCount'])
xrank ={}
yrank = {}
i=1
for index, row in df1.iterrows():
	xrank[row["movieTitle"]] = i
	i =i+1
# print("xrank",xrank)
i =1

for index, row in df2.iterrows():
	# 
	# print(index,row['movieId'],row['Rating'],row['imdbVotes'])
	yrank[row["movieTitle"]] = i
	i +=1
	# print(xrank[row["movieId"]],yrank[row["movieId"]])
# print("yrank",yrank)
for key,value in xrank.items():
	# print(xrank[key],yrank[key])
	y = int(xrank[key])
	x = int(yrank[key])
	plt.plot(x, y, 'bo',markersize=2)
	plt.text(x * (1 + 0.01), y * (1 + 0.01) , key, fontsize=4)

plt.xlabel('MovieLense ranking', fontsize=12)
plt.ylabel('IMDB ranking', fontsize=12)
plt.show()