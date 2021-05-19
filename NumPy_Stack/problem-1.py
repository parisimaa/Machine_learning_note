# Problem 1: 

import numpy as np
import matplotlib.pyplot as plt

A= np.array([[0.3,0.6,0.1],[0.5,0.2,0.3],[0.4,0.1,0.5]])
v=np.ones(3)/3
d= np.zeros(25)

for i in range(25):
    o= np.dot(v,A)
    d[i]= np.linalg.norm(o-v)
    v= o
    
plt.plot(d)
plt.show()

# If |v'-v|=0 then v=v'=vA in which we found the eigenvector for A for which corresponding eigenvalue is 1