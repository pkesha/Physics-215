#%%%
#!/usr/bin/python
import numpy as np
from numpy.random import random as rng
import matplotlib.pyplot as plt


#%%Plotting the variables
def plot2d(title):
    plt.figure(title)
    plt.xlabel('Distance in the x - direction')
    plt.ylabel('Distance in the y - direction')

#%%  Calculating the Entropy

def Entropy(x_coor, y_coor, RandomTitle2, closed):
    #Choosing the edges in order to calculate the correct Entropy
    if (closed == 1):
        bounds = 100
    else:
        bounds = num_steps
        
    #Initializing statements
    nbins = 64
    xedges = np.linspace(-1*bounds, bounds, nbins+1)
    yedges = np.linspace(-1*bounds, bounds, nbins+1)
    Entropy1 = np.zeros(num_steps)
    
    #Calculating Entropy
    for s in range(num_steps):
        h = np.histogram2d(x_coor[:,s], y_coor[:,s], bins=(xedges, yedges))
        p = h[0]/sum(sum(h[0]))
        v = 0
        for i in range(nbins):
            for j in range(nbins):
                if (p[i,j]>0):
                    v+=-p[i,j]*np.log(p[i,j])
                    Entropy1[s] = v
    
    #Hardcode the graphing for Entropy     
    plt.figure("Entropy vs time for" +  str(RandomTitle2) + "system")
    plt.xlabel("Time in seconds")
    plt.ylabel("Entropy in joules/kelvin")
    plt.plot(Entropy1)

#%%%Random walks in an open system
num_steps = 1500
num_walkers = 1000
def calc2D(closed, RandomTitle):
    #initalizing the number of elements in the arrays
    x_coor = np.zeros([num_walkers,num_steps])
    y_coor = np.zeros([num_walkers,num_steps])
    
    #Calculating/graphing the Walkers and the historgrams
    for j in range(num_walkers):
        #initailizing as all random numbers
        x_step = rng(num_steps)
        y_step = rng(num_steps)
        
        #initalizing as all zeros or ones
        x_step = 2 * (x_step >= 0.5) - 1
        y_step = 2 * (y_step >= 0.5) - 1
        
        #cummulative sum of each component at each step
        x = np.cumsum(x_step)
        y = np.cumsum(y_step)
        
        #This block of code is for closed system, rearranges walkers
        if (closed == 1):
            for i in range(num_steps):
                while (x[i] < -100 or x[i] > 100 or y[i] < -100 or y[i] > 100):
                    x_step[i:num_steps] = -1 * x_step[i:num_steps]
                    x[i:num_steps] = np.cumsum(x_step[i:num_steps]) +x[i-1]
                
                    y_step[i:num_steps] = -1 * y_step[i:num_steps]
                    y[i:num_steps] = np.cumsum(y_step[i:num_steps]) + y[i-1]
        
        #Plotting of all steps in all direction 
        plot = x; title = "Random walks in" +  str(RandomTitle) + "system"
        plot2d(title); plt.plot(plot, y)
        
        #Assign the x and why coordinates at a certain step
        x_coor[j,:] = x
        y_coor[j,:] = y
    
    #Plot the graph at iteration num_steps
    plot = x; titlehist = "2D random walk with" +  str(RandomTitle) + "system at iteration num_steps"; 
    plot2d(str(titlehist));
    plt.plot(x_coor[:,num_steps-1],y_coor[:,num_steps-1],'o')
    
    #Plot the histogram at iterantion num_steps/2
    plot = x; titlehist = "2D random walk with" +  str(RandomTitle) + "system at iteration num_steps/2"
    plot2d(titlehist);
    plt.plot(x_coor[:,int(num_steps/2)],y_coor[:,int(num_steps/2)],'o')
    
    RandomTitle1 = str(RandomTitle)
    
    #Calculate and plot the entropy
    Entropy(x_coor, y_coor, RandomTitle1, closed)
    
#%%Main
calc2D(0, " open ")

calc2D(1, " closed ")
