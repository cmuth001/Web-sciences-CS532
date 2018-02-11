import pandas as pd
import matplotlib.pyplot as plt
df  = pd.read_csv("ageAndMementos.csv")
df.plot()  # plots all columns against index
df.plot(kind='scatter',x='age',y='mementos') # scatter plot
plt.show()