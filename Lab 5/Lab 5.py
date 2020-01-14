
import numpy as np
import matplotlib.pyplot as plt
#%% Calculate
#initialize arrays and constants
d_theta = 0.001; l = 1 ; gravity = 9.8
theta_m = np.linspace(np.pi/30, np.pi, 777); Period = np.zeros(theta_m.size)

#initializing to calculate the angle vs. time
for j in range(len(Period)):
    i_max = int(theta_m[j]/d_theta)     #calculation for i_max
    dT = []     #place holder
    
    #Caluclation of all period and theta_m
    for i in range(i_max-1):
        dT.append(d_theta/ ( np.sqrt(np.cos(i*d_theta) - np.cos(theta_m[j]) )))
    Period[j] = np.sum(dT)*np.sqrt((8*l)/gravity)
#%%Plot
plt.plot(theta_m,Period)
plt.title('Swing period vs. Max angle')
plt.xlabel('theta_m(radians)')
plt.ylabel('Period in Seconds')