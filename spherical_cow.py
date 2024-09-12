import numpy as np 
from matplotlib import pyplot as plt 

x0 = 0
y0 = 1000
v0x =1 
v0y =100
dt = 0.001

m = 1000
k = 0

g = 9.8 #m/s^2
 

def force_function(x,y,vx,vy):
    v = (vx**2 + vy**2)**(1/2)
    Fx = -(k*vx*vx)
    Fy = -(k*vy*vy + m*g)
    return(Fx, Fy)

def position_function(x,y,vx,vy,Fx,Fy,dt):
    xf = x + vx*dt
    yf = y+ vy*dt
    vxf = vx + (Fx*dt)/m
    vyf = vy + (Fy*dt)/m
    return (xf, yf, vxf, vyf)

def energy_function(vx, vy, y):
    K = (m/2)*( vx**2 + vy**2) 
    U = m*g*y
    T = K + U
    return(K, U, T)
F0x , F0y = force_function(x0,y0,v0x,v0y)
K0, U0, T0 = energy_function(v0x, v0y, y0)

x = [x0]
y = [y0]
vx = [v0x]
vy= [v0y]
Fx = [F0x]
Fy =[F0y]
K = [K0]
U= [U0]
T = [T0]
t = [dt]

for i in range(28000):   
     xl, yl, vxl, vyl = position_function(x[i], y[i],vx[i],vy[i], Fx[i], Fy[i], dt)
     x.append(xl)
     y.append(yl)
     vx.append(vxl)
     vy.append(vyl)

     Fxl, Fyl  = force_function(x[i], y[i], vx[i], vy[i])
     Fx.append(Fxl)
     Fy.append(Fyl)

     Kl, Ul,Tl  =energy_function(vx[i],vy[i],y[i])
     K.append(Kl)
     U.append(Ul)
     T.append(Tl)
     tl = t[i] + dt
     t.append(tl)
plt.figure()
plt.plot(x,y)
plt.xlabel("x (m)")
plt.ylabel("y (m)")
plt.title("trajectory for spherical cow (no drag)")
plt.savefig("trajectory_k=0.png")
plt.show()
plt.close()


plt.figure()
plt.plot(t, T, label='Total Energy')
plt.plot(t,U, label='Potential Energy')
plt.plot(t,K, label ='Kinetic Energy')
plt.xlabel("time (s)")
plt.ylabel("Energy(J)")
plt.title("Energy of spherical cow (no drag)")
plt.legend()
plt.savefig("Energy_for_spherical_cow.png")
plt.show()

with open("Spherical_cow_no_drag.txt", 'w') as f:
     f.write(f"x(m),y(m),t(s)\n")
     for i in range(len(x)):
         f.write(f"{x[i]}, {y[i]}, {t[i]}\n")
