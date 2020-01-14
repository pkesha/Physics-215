#%% import libs
import numpy as np
import matplotlib.pyplot as plt
#%% initialize constants            
t = 10
dt = 0.01 
n = int(t/dt)     
mass = 1   
l = 1 
gravity = 9.8        
       
#%% Calculate harmonic motion
def calc(theta):
    theta_f = np.zeros(n); w  = np.zeros(n); t  = np.zeros(n) 
    w[0] = 0; t[0] = 0; theta_f[0] = theta
     
    for i in range(n-1):
        w[i+1]  =  w[i] - (gravity/l)*np.sin(theta_f[i])*dt
        theta_f[i+1] = theta_f[i] + w[i+1]*dt
        t[i+1]  =  t[i] + dt
         
    Energy = ((1/2)*mass*(l**2)*(w**2)) + (l*mass*gravity*(1-np.cos(theta_f)))
    
    min_f = np.min(theta_f[0:int(3.0/dt)])
    Period = 2*np.argmin(theta_f[0:int(3.0/dt)])
    
    return(theta_f, Energy, t, min_f, Period)

#%% Plot functions
def plot2d(t, y):
    plt.plot(t, y, label = labels)
    plt.legend()
    plt.title(titleP) 
    
    # Label Axes
    plt.xlabel(labelx)
    plt.ylabel(labely)
    
#%%Plotting amplitude of pendulum
#setting up name variables and constraint values. These won't change as frequently
titleP = 'Amplitude of Pendulum vs. Time'; labelx = 'Time in Seconds'; labely = 'Angle with respect to vertical'
plt.figure(1)

labels = 'Angle Displacement 1 = n/12'
theta1,Energy1,t,mini1,T1 = calc(np.pi/12)
plot2d(t, theta1)

labels = 'Angle Displacement 2 = n/6'
theta2,Energy2,t,mini2,T2 = calc(np.pi/6)
plot2d(t, theta2)

labels = 'Angle Displacement 3 = n/3'
theta3,Energy3,t,mini3,T3 = calc(np.pi/3)
plot2d(t, theta3)

#%% Plotting energies
#setting up name variables and constraint values. These won't change as frequently
titleP = 'Energy vs. Time'; labelx = 'Time in Seconds'; labely = 'Joules'
plt.figure(2)

labels = 'Angle Displacement 1 = n/12'
plot2d(t, Energy1)

labels = 'Angle Displacement 2 = n/6'
plot2d(t, Energy2)

labels = 'Angle Displacement 3  = n/3'
plot2d(t, Energy3)

#%% plot the initial angles as a function of the periods 
xvales = [-mini1,-mini2,-mini3]
Period = [T1,T2,T3]

titleP = 'Period vs Theta'; labelx = "Theta"; labely = "Period (s)"
fig = plt.figure(3);

labels = 'T vs Theta'
plot2d(xvales, Period)