#%%%Importing libraries
import numpy as np
from numpy.random import random as rng
import matplotlib.pyplot as plt

#%%Declaring constants
num_steps = 500
num_walkers = 1000
endpoints = np.zeros(num_walkers)
temp = np.zeros(num_walkers)

#%%Plotting
def plot2d():
    plt.figure(title)
    plt.xlabel('Distance in the x - direction')
    plt.ylabel('Distance in the y - direction')
    
#%%Code for 1D
for j in range(num_walkers):
    #initialization for number of elements in each step
    x_step = rng(num_walkers); y_step = rng(num_walkers)
    
    #Initialize the steps to be either zero or one
    x_step = 2 * (x_step > 0.5) - 1
    y_step = 2 * (y_step > 0.5) - 1
    
    #Sum of each step
    x = np.cumsum(x_step)
    y = np.cumsum(y_step)
    
    #Plotting of all steps in all direction 
    plot = x; title = "Ramdom walks in 1D"
    plot2d(); plt.plot(plot, y)
    
    #Calculations to plot the average
    r2 = x**2 + y**2
    temp = temp + r2

#Graph average
plot = temp/num_walkers; title = "Average Walk in 1D"
plot2d(); plt.plot(plot)

#%%Code for 2D plot calculations'''
temp1 = np.zeros(num_steps)
for i in range(num_walkers):
    #initialization for number of elements in each step
    theta_step = np.radians(np.random.randint(0,6,num_steps) * 60)
    x1_step = np.zeros(num_steps); y1_step = np.zeros(num_steps)
    
    #Initialize the steps to be either zero or one
    x1_step = np.cos(theta_step)
    y1_step = np.sin(theta_step)
    
    #Sum of each step
    x1 = np.cumsum(x1_step)
    y1 = np.cumsum(y1_step)
    
    #Plotting of all steps in all direction 
    plot = x1; title = "Ramdom walks in 2D"
    plot2d(); plt.plot(plot, y1)
    
    #Calculations to plot the average
    r21 = (x1**2 + y1**2); 
    temp1 = temp1 + (r21)

#Graph average
plot = temp1/(num_walkers); title = "Average Walk in 2D"
plot2d(); plt.plot(plot)