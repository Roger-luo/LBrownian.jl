import string
import numpy as np 
from matplotlib import pyplot as plt 
from matplotlib import animation

data = open('data.dat','r')

StickLength = np.array([0.1,0.1])

pos_x = []
pos_y = []
alpha = []
beta = []

for line in data:
    pos_x.append(string.atof(line.split()[0]))
    pos_y.append(string.atof(line.split()[1]))
    alpha.append(string.atof(line.split()[2]))
    beta.append(string.atof(line.split()[3]))

pos_x = np.array(pos_x)
pos_y = np.array(pos_y)
alpha = np.array(alpha)
beta  = np.array(beta)

data.close()

fig = plt.figure()
ax = plt.axes(xlim=(-5,5),ylim=(-5,5))
line, = ax.plot([],[],lw=2)

def init():
    line.set_data([],[])
    return line,

def animate(i):
    x = [pos_x[i],pos_x[i]+StickLength[0]*np.cos(alpha[i]),pos_x[i]+StickLength[1]*np.cos(beta[i])]
    y = [pos_y[i],pos_y[i]+StickLength[0]*np.sin(alpha[i]),pos_y[i]+StickLength[1]*np.sin(beta[i])]
    #print (x[2]-x[0])*(x[2]-x[0])+(y[2]-y[0])*(y[2]-y[0])
    line.set_data(x,y)
    return line,

anim = animation.FuncAnimation(fig, animate, init_func=init, 
                frames=200000, interval=10, blit=False) 
#anim.save('basic_animation.gif')
plt.show()