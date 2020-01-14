#random_walk_4.py

#%%

import numpy as np
from numpy.random import random as rng
import matplotlib.pyplot as plt

#%%

num_steps=500
num_walkers=1000

#%%

plt.figure()
plt.title("Random Walk")
plt.xlabel("x")
plt.ylabel("y")

r2ave=np.zeros(num_steps)

x=np.zeros(num_steps)
y=np.zeros(num_steps)

for j in range(num_walkers):
    i=0
    while(i<num_steps-1):
        x_step=rng()
        y_step=rng()
        x_step=2*(x_step>0.5)-1
        y_step=2*(y_step>0.5)-1
        
        x1=x[i]+x_step
        y1=y[i]+y_step
        
        print(x1,y1)
        
    plt.plot(x,y)

plt.figure()
plt.title("Random Walk in Two Dimensions")
plt.xlabel("step number")
plt.ylabel("<r.r>")
plt.plot(r2ave/num_walkers)

plt.show()
    
'''        
        if x1 in x:
            ind=x.tolist().index(x1)
            print("x1 is at step", ind)
            
            if x[ind]==x1:
                print("step rejected")
            else:
                x[i+1]=x1
                y[i+1]=y1
                r2ave[i+1]=x[i+1]**2+y[i+1]**2
                i=i+1
            
        else:
            x[i+1]=x1
            y[i+1]=y1
            r2ave[i+1]=x[i+1]**2+y[i+1]**2
            i=i+1
'''        
        
'''            
        if y1 in y:
            ind=y.tolist().index(y1)
            print("y1 is at step", ind)
            
            if y[ind]==y1:
                print("step rejected")
            else:
                x[i+1]=x1
                y[i+1]=y1
                r2ave[i+1]=x[i+1]**2+y[i+1]**2
                i=i+1
            
        else:
            x[i+1]=x1
            y[i+1]=y1
            r2ave[i+1]=x[i+1]**2+y[i+1]**2
            i=i+1
'''