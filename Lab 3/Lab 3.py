#%% Importing libraries
import numpy as np                        
import matplotlib.pyplot as plt           

#%% Constants             
t, dt = 10.0, 0.01  #time and step values
theta = 35.0*(np.pi/180) #theta
phi = 0                #phi         
n = int(t/dt)       #the number of values that will be graphed
g = 9.81            #Gravity
mass = 1
#%% Calculate 2D Trajectories
v_x = 50*np.cos(theta)
v_y = 50*np.sin(theta)*np.cos(phi)        #since phi is 0, it is equivalent to 0*np.sin(th0) which is true for trajectories without mangus force
v_z = 50*np.sin(theta)*np.sin(phi)

#%% Calculations in 2D
def calc_F(velx, vely, velz, v_resitance, YY):
    #intitializing local arrays, constants, intital values
    x = np.zeros(n); y = np.zeros(n); z = np.zeros(n)
    x[0] = 0; y[0] = YY; z[0] = 0   #starting points
    #S0 is the mangus coeffiecient
    vd, delta = 35.0, 5.0 ;w = 2*(np.pi)*30; t = 0;S0 = (4.1e-4)*mass 
                                 
    for i in range(n-1):
        v_magnus = (np.sqrt((velx-v_resitance)**2 + vely**2 + velz**2))
        B2 = (0.0039 + (0.0058/(1 + np.exp((v_magnus-vd)/delta))))*mass

        #this is to calculate each value in the arrays
        velx = velx - (B2/mass) * v_magnus * (velx-v_resitance) * dt
        velz = velz - (S0/mass) * w * velx * dt
        #The exquation for y component changes when we plot for magnus
        if (YY > 0):
            vely = vely - g*dt
        else:
            vely = vely - g * dt - (B2/mass) * v_magnus * vely * dt
        
        #Stores the values in the arrays
        x[i+1]  = x[i] + velx*dt
        y[i+1]  = y[i] + vely*dt
        z[i+1]  = z[i] + velz*dt
        t = t + dt
    fly = [x,y,z]                     # Trajectory
    return(fly)

#%% Plot 2D Trajectories
def plot2d(y, tl, zbegin, xlim, ylim):
    # Label Axes
    plt.xlabel('Distance (m)')
    plt.ylabel(y)
    
    #plot constraints
    plt.xlim([0,xlim])
    plt.ylim([zbegin,ylim])
    
    plt.legend()                            
    plt.title(tl) 

#%% Main
y = "Y height (m)"; z = "Z width (m)"; title2 = "2D Trajectory"; title3 = "3D trajectory"

#windless
fly = calc_F(v_x, v_y, 0.0 , 0.0, 0.0)           
plt.plot(fly[0], fly[1], label = 'No resistance')
plot2d(y, title2,0, 150, 35)
plt.figure(1)

#Plotting tail wind graph
v_tail = 4.5                     
fly_tail = calc_F(v_x, v_y, 0.0 , v_tail, 0.0)   
plt.plot(fly_tail[0], fly_tail[1], label = 'Tail Wind')
plot2d(y, title2,0, 140, 35) 


#Plotting headwind Graph
v_head = -v_tail                 
fly_head = calc_F(v_x, v_y, 0 , v_head, 0)
plt.plot(fly_head[0], fly_head[1], label = "Head Wind") 
plot2d(y, title2,0, 140, 35)

#Magnus Plot initial variables
th0 = 0; y0 = 50; mass = 0.149
v_x = 30*np.cos(theta)
v_y = 30*np.sin(theta)*np.cos(phi)        #since phi is 0, it is equivalent to 0*np.sin(th0) which is true for trajectories without mangus force
v_z = 30*np.sin(theta)*np.sin(phi)

#XY Trace
plt.figure(2)
fly_3 = calc_F(v_x, v_y, v_z, 0.0, 50)
plt.plot(fly_3[0], fly_3[1], label = "XY Trace with magnus force")
plot2d(y, title3,0, 85, 85)

#XZ Trace
plt.figure(3)
plt.plot(fly_3[0], fly_3[2], label = "XZ Trace with magnus force")
plot2d(z, title3,-20,82,0)