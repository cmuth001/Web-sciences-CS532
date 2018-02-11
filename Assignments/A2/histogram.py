import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
data = pd.read_csv('mementosCollection.csv', sep=',', skiprows=0,header=None, index_col =0).dropna()
# data = pd.read_csv('testMementos.csv', sep=',', index_col =0)
 
data.plot(kind='bar')
plt.ylabel("URL's count")
plt.xlabel('mementos')
plt.title('Histogram')
L=plt.legend()
L.get_texts()[0].set_text('URLs count')
plt.show()