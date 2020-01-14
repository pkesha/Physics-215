
import numpy as np
from numpy.random import random as rng
import matplotlib.pyplot as plt

#Constants and initializations
sizer = 100
probability = np.zeros(sizer)
count = 0
max_val = np.zeros((sizer, sizer))

#Calculation in big nested for loop
for p in range(sizer):
    for p1 in range(sizer):
        lattice_size = 10
          
#%% Initialized given code
        n = np.zeros((lattice_size,lattice_size))
        b = np.zeros((lattice_size,lattice_size))
        prob =(1+p)/sizer
        occupancy = int(prob * (lattice_size-2) * (lattice_size-2))
        
        
        clust = np.zeros(lattice_size*lattice_size)
        d = np.zeros((lattice_size,lattice_size))
        
#%% Given Code
        # cluster count
        x = 0
        counter = 0
        for count in range(occupancy):
            counter = counter + 1
            i = int((lattice_size-2)*rng())+1
            j = int((lattice_size-2)*rng())+1
            while n[i,j] > 0:
                    i = int((lattice_size-2)*rng())+1
                    j = int((lattice_size-2)*rng())+1
            
            x = x+1
            n[i,j]=1
            d[i,j]=x
            clust[x]=x
            
            if (n[i-1,j] !=0):
                ind = d[i-1,j]
                ind = clust[int(ind)]
                while ind < 0:
                    ind = clust[int(-1*ind)]
                if (ind !=x):
                    clust[int(ind)] = -1 * x
                
            if (n[i+1,j] != 0):
                ind = d[i+1,j]
                ind = clust[int(ind)]   
                while ind < 0:
                    ind = clust[int(-1*ind)]      
                if (ind !=x):
                    clust[int(ind)] = -1 * x
        
                
            if (n[i,j-1] != 0):
                 ind = d[i,j-1]    
                 ind = clust[int(ind)]
                 while ind < 0:
                    ind = clust[int(-1*ind)]        
                 if (ind !=x):
                    clust[int(ind)] = -1 * x
        
                
            if (n[i,j+1] != 0):
                 ind = d[i,j+1]    
                 ind = clust[int(ind)]
                 while ind < 0:
                    ind = clust[int(-1*ind)]
                 if (ind !=x):
                     clust[int(ind)] = -1 * x 
                           
#%%
        b = np.zeros((lattice_size,lattice_size))#create new matrix to hold matrix that holds all numbered clusters
        decoy = np.zeros(clust.size)#cluster will hold all orignal val of cluster
        
        for i in range(clust.size):
            decoy[i] = clust[i]
        
        #re organzie and make the clusters positive -THIS BLOCK OF CODE IS AN INFINTE LOOP
        '''
        for i in range(count + 1):
            while(clust[np.abs(i)]<0):
                if (clust[np.abs(clust[i])] >= 0):
                    a = clust[np.abs(clust[i])]
                    break
                '''
#%%Graph the probability        
y = np.zeros(sizer)
for i in range(sizer):
    sum_val = 0
    
    for j in range(sizer):
        sum_val = max_val[i,j]+sum_val
    
    y[i] = sum_val/sizer
    den = (lattice_size-2)**2
y = y/((lattice_size-2)**2)

plt.xlabel("Probability of matrix connecting matrix clusters")
plt.ylabel("Matrix blocks occupies")   
plt.plot(probability, y)
             