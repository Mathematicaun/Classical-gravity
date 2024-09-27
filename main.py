from matplotlib.colors import Normalize
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
h = 1e-10
fig = plt.figure()
fig.set_facecolor('black')
ax = fig.add_subplot(projection='3d')
density = 100
n = 5
k = 2
i = np.linspace(-n, n, int(2*n*density))

def x(t1, t2, r1, r2):
    return (r1*np.cos(t1)+r2)*np.cos(t2)

def y(t1, t2, r1, r2):
    return (r1*np.cos(t1)+r2)*np.sin(t2)

def z(t1, r1):
    return r1*np.sin(t1)

def dx(t1, t2, r1, r2):
    return ((r1*np.cos(t1+h)+r2)*np.cos(t2+h)-(r1*np.cos(t1)+r2)*np.cos(t2))/h

def dy(t1, t2, r1, r2):
    return ((r1*np.cos(t1+h)+r2)*np.sin(t2+h)-(r1*np.cos(t1)+r2)*np.sin(t2))/h

def dz(t1, r1):
    return (r1*np.sin(t1+h)-r1*np.sin(t1))/h
_ = np.linspace(0, 2*np.pi, int(2*np.pi*density))

def X(t1, t2):
    return x(np.pi/2*np.sin(2*np.pi*k/(2*np.pi)*t1), t2, 2, 5)

def Y(t1, t2):
    return y(np.pi/2*np.sin(2*np.pi*k/(2*np.pi)*t1), t2, 2, 5)

def Z(t1):
    return z(np.pi/2*np.sin(2*np.pi*k/(2*np.pi)*t1), 2)

def dX(t1, t2):
    return (x(np.pi/2*np.sin(2*np.pi*k/(2*np.pi)*(t1+h)), t2+h, 2, 5)-x(np.pi/2*np.sin(2*np.pi*k/(2*np.pi)*t1), t2, 2, 5))/h

def dY(t1, t2):
    return (y(np.pi/2*np.sin(2*np.pi*k/(2*np.pi)*(t1+h)), t2+h, 2, 5)-y(np.pi/2*np.sin(2*np.pi*k/(2*np.pi)*t1), t2, 2, 5))/h

def dZ(t1):
    return (z(np.pi/2*np.sin(2*np.pi*k/(2*np.pi)*(t1+h)), 2)-z(np.pi/2*np.sin(2*np.pi*k/(2*np.pi)*t1), 2))/h

Mag = np.sqrt(dX(_, _)**2 + dY(_, _)**2 + dZ(_)**2)
norm = Normalize(Mag.min(), Mag.max())

def simulation(t):
    ax.clear()
    ax.plot(X(_, _), Y(_, _), Z(_), color='white')
    ax.xaxis.pane.set(visible=0)
    ax.yaxis.pane.set(visible=0)
    ax.zaxis.pane.set(visible=0)
    ax.xaxis._axinfo['grid'].update(color='none')
    ax.yaxis._axinfo['grid'].update(color='none')
    ax.zaxis._axinfo['grid'].update(color='none')
    ax.set_facecolor('black')
    ax.set(xlim=[-n, n], ylim=[-n, n], zlim=[-n, n])
    mag = np.sqrt(dX(t, t)**2 + dY(t, t)**2 + dZ(t)**2)
    c = plt.get_cmap('plasma')(norm(mag))
    ax.scatter(0, 0, 0, color='yellow', s=2*10**3)

    ax.scatter(X(t, t), Y(t, t), Z(t), color='blue', s=10**2+500)
    ax.quiver(X(t, t), Y(t, t), Z(t), dX(t, t)/mag, dY(t, t)/mag, dZ(t)/mag, color=c)

    #The position vector
    ax.quiver(0, 0, 0, X(t, t), Y(t, t), Z(t), color='white', arrow_length_ratio=.1, alpha=.5)
    # for j in np.linspace(0, 2*np.pi, 100):
    #     ax.plot(x(_, j, 2, 5), y(_, j, 2, 5), z(_, 2), color='green')
sm = plt.cm.ScalarMappable(cmap='plasma', norm=norm)
cbar = plt.colorbar(sm, ax=ax)
cbar.set_label('Magnitud', color='white', font='serif')
plt.setp(plt.getp(cbar.ax, 'yticklabels'), color='white')

ani = FuncAnimation(fig, simulation, frames=np.linspace(0, 2*np.pi, int(2*np.pi*density)), interval=0, blit=0)
plt.tight_layout()
plt.show()
