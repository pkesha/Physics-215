# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 12:11:23 2017

@author: nbhatt9
"""
import matplotlib.pyplot as plt 
import numpy as np

c= 300
dx = 0.01
dt = dx/c 
l = 1 
t = 100

r = c*dt/dx
n = int(l/dx)

y = np.zeros( [n+1,3])

y[0,0] = 0
y[n,0] = 0

y[0,1] = 0
y[n,1] = 0 

y[0,2] = 0
y[n,2] = 0 

for i in range(n):
    y[i,0] = np.exp(-1000*(i*dx - 0.3)**2)
    y[i,1] = np.exp(-1000*(i*dx - 0.3)**2)

y[0,0] = 0
y[n,0] = 0

y[0,1] = 0
y[n,1] = 0 
    
 
for j in range(500):
    for i in range(n-1):
        temp_element2 = 2*(1-r**2)*y[i+1,1]-y[i+1,0]+r**2*(y[i+2,1] +y[i,1])
        y[i+1,2] = temp_element2
         
    y[0,2] = 2*(1- 0.5*r**2)*y[0,1] - y[0,0] + r**2*y[1,1]
    tamp1 = y[1,2]
    y[0,2] = tamp1
    y[n,2] = 2*(1- 0.5*r**2)*y[n,0] - y[n,0] + r**2*y[n-1,1]
    tamp2 = y[n-1,2]
    y[n,2] = tamp2
    
    for i in range(n+1):
        y0 =  y[i,1]
        y1 =  y[i,2]
        y[i,0] = y0
        y[i,1] = y1
    
    if (j%100 ==0):
        plt.plot(y[:,1])
