import matplotlib.pyplot as plt
import numpy as np
#%% Define Constants
c = 300    
dx = 0.01  
r = 1
dt = r*dx/c  
l = 1      
t = 10    
r = c*dt/dx
n = int(l/dx) 
Y = np.zeros([n+1,3])

#%%% Boundary Conditions
Y[0,0] = 0; Y[n,0] = 0; Y[0,1] = 0; Y[n,1] = 0; Y[0,2] = 0; Y[n,2]= 0

# Initial Condition excluding the end points
for j in range(2):
    for i in range(n):
        Y[i,j]=np.exp(-1000*(i*dx - 0.3)**2)
    
Y[0,0] = 0; Y[n,0] = 0; Y[0,1] = 0; Y[n,1]= 0
 
#%%% Loop for calculation and graphing
for j in range(300):
    for i in range(n-2):
        temp_2 = (2*(1-(r**2))) * (Y[i+1,1])- Y[i+1,0]+ ((r**2)*(Y[i+2,1]+Y[i,1])); Y[i+1,2] = temp_2
    
    for i in range(n-2):
        Y_0 = Y[i+1,1]; Y_1 = Y[i+1,2]
        Y[i+1,0]= Y_0; Y[i+1,1]= Y_1
         
    if (j%50 ==0):
        plt.title("Wave motion of a string with fixed endpoints")
        plt.plot(Y[:,2])
        plt.xlabel("length")
        plt.ylabel("Amplitude")
        plt.legend()