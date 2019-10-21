from numpy import array, linspace
from math import sin, cos, pi,tan 
from pylab import plot, xlabel, ylabel, show
from scipy.integrate import odeint
from vpython import sphere, scene, vector, color, arrow, text, sleep, box

arrow_size = 0.5

arrow_x = arrow(pos=vector(0,0,0), axis=vector(arrow_size,0,0), color=color.red)
arrow_y = arrow(pos=vector(0,0,0), axis=vector(0,arrow_size,0), color=color.green)
arrow_z = arrow(pos=vector(0,0,0), axis=vector(0,0,arrow_size))

#parametros
m=1 #masa pendulo
M=0.1 #masa bloque
l =1 #longitud de la cuerda
g=9.8 #aceleracion de la gravedad en la tierra
    
def pendulo (init, t):
        
    m=1 #masa pendulo
    M=0.1 #masa bloque
    l =1 #longitud de la cuerda
    g=9.8 #aceleracion de la gravedad en la tierra
    
    w=init[0]
    x=init[1]  
    
    dx=init[2] 
    dw=init[3] 
           
    dv_w= (((-g/l)*sin(w)-(m/(m+M))*dw*dw*sin(w)*cos(w))/(1+(m/(m+M))*cos(w)*cos(w))) 
    dv_x= ((m*dw*dw*l*sin(w)-m*dv_w*l*cos(w))/(m+M) ) #aceleracion x
    print(dv_x, dv_w, x, w, dx, dw)
    
    
    #return array([dv_w,dv_x,dw,dx],float)
    return array([dw,dx, w, x],float)
    
n_steps = 1000
t_start = 0.
t_final = 15.
t_delta = (t_final - t_start) / n_steps 

t = linspace(t_start, t_final, n_steps)

init= [3*pi/180., 1 ,0 ,0]

sol,outodeint = odeint(pendulo, init, t, full_output=True)
vww, vxx, ww, xx = sol.T

scene.range = 2 # m

x = 0.+l*sin(init[0])
y = -l*cos(init[0])
z = 0.
x2 = 0.
y2=0.

sleeptime = 0.001
prtcl = sphere(pos=vector(x,y,z), radius=0.1, color=color.cyan)
prtcl2 = box(size=vector(0.2,0.2,0.2),pos=vector(x2,y2,z), color=color.cyan)

time_i = 0
t_run = 0

#for i in omega:
#    print(i)

print(ww)

while t_run < t_final:
    sleep(sleeptime)
    prtcl.pos = vector( xx[time_i]+l*sin(ww[time_i]), -l*cos(ww[time_i]), z )
    prtcl2.pos = vector( xx[time_i],y2, z )
    t_run += t_delta
    time_i += 1
    
