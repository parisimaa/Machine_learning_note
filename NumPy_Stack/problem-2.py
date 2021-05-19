# Problem 2:

import numpy as np 
import matplotlib.pyplot as plt

N= 1000
y = np.zeros(N)

for i in range(N):
    x = np.random.uniform(size=N)
    y[i]= np.sum(x)
    
plt.hist(y)
plt.show()