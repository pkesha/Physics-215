import matplotlib.pyplot as plt
import numpy as np
#%% Define Constants
c = 300         
dx = 0.01       
r = 1           
l = 1           
dt = r*dx/c     
r = c*dt/dx
n = int(l/dx)   
Y = np.zeros([n+1,3])

#%%% Boundary Condition
Y[0,0] = 0; Y[n,0] = 0; Y[0,1] = 0; Y[n,1] = 0
    
# Initial Condition (excluding the end points)
for i in range(n):
    Y[i,0]=np.exp(-1000*(i*dx - 0.3)**2)
    Y[i,1]=np.exp(-1000*(i*dx - 0.3)**2)


temp0= Y[1,0]; Y[0,0]= temp0
temp01= Y[n-1,0]; Y[n,0]= temp01

temp11= Y[1,1]; Y[0,1]= temp11
temp12= Y[n-1,0]; Y[n,1]= temp12

#%%% Loops
for j in range(200):
    for i in range(n):
        Y[0,2]= 2*(1-0.5*r**2)*Y[0,1]-Y[0,0]+r**2*Y[1,1]
        Y[n,2]= 2*(1-0.5*r**2)*Y[n,1]-Y[n,0]+r**2*Y[n-1,1]
        temp_2 = 2*(1-r**2)*Y[i,1]-Y[i,0]+r**2*(Y[i+1,1]+Y[i-1,1]); Y[i,2] = temp_2
        
    for i in range(n+1):
        Y0 = Y[i,1]; Y1 = Y[i,2]
        Y[i,0] = Y0; Y[i,1] = Y1
         
    if (j%20 ==0):
        plt.title("Wave motion of string with free end points")
        plt.plot(Y[:,2])
        plt.xlabel("length")
        plt.ylabel("Amplitude")
        plt.legend()