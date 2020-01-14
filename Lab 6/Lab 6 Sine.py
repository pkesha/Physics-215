import matplotlib.pyplot as plt
import numpy as np
#%% Define Constants
c = 300         
dx = 0.01       
r = 1           
l = 1                  
dt = r*dx/c     
r = c*dt/dx
A = 1
w = 939
n = int(l/dx)   
Y = np.zeros([n+1,3])
Y[0,0]= A*np.sin(w*dt)

#%%% Loop for driving force
for j in range(3000):
    for i in range(n):
        Y[0,1]= A*np.sin((j)*w*dt) 
        Y[0,2]= A*np.sin((j+1)*w*dt)
        temp_element2 = 2*(1-r**2)*Y[i,1]-Y[i,0]+(r**2)*(Y[i+1,1]+Y[i-1,1])
        Y[i,2] = temp_element2
    
    for i in range(n+1):
        Y0 = Y[i,1]; Y1 = Y[i,2]
        Y[i,0]= Y0; Y[i,1]= Y1
         
    if (j%300 == 0):
        plt.title("Diving Force when omega is 939")
        plt.plot(Y[:,2])
        plt.xlabel("length")
        plt.ylabel("Amplitude")
        plt.legend()
#%%
