import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import math
data = pd.read_csv('followersCount.csv', skiprows=1, sep=',',header=None)
y_axis = data[1].values.tolist()
# my friends count =980
myFriends = 193
mean  = round(np.mean(y_axis),2)
median = round(np.median(y_axis),2)
sd = round(np.std(y_axis),2)
y_axis.append(mean)
y_axis.append(median)
y_axis.append(sd)
# y_axis.append(myFriends)
y_axis.sort()


# print(myFriends)

x_axis = [i for i in range(1, len(y_axis)+1)]

plt.plot(x_axis, y_axis, color='g' ) 
plt.xlabel('Users')
plt.ylabel('Followers Count')
plt.plot(y_axis.index(mean),mean, marker='x', color='r')
plt.text(y_axis.index(mean),mean+500,"Mean-"+str(mean))

plt.plot(y_axis.index(median),median, marker='x', color='r')
plt.text(y_axis.index(median),median-10000,"Median-"+str(int(median)))

plt.plot(y_axis.index(sd),sd, marker='x', color='r')
plt.text(y_axis.index(sd),sd-1000,"SD-"+str(sd))

plt.plot(y_axis.index(myFriends),myFriends, marker='x', color='r')
plt.text(y_axis.index(myFriends),myFriends+3000,"hemanthmalla-193")

plt.title('Twitter Followers Of Followers For Hemanth Malla')
# plt.xticks(x_axis)
plt.grid(True)
plt.show()