# exercise 1

import numpy as np
import matplotlib.pyplot as plt

def mesh_function(f, t):
    steps = len(t)
    u = np.zeros(steps)
    for i in range(steps):
        u[i] = f[i]
    return u

t_end = 5
dt = 0.1
Nt = t_end/dt

t = np.linspace(0, t_end, Nt)   
    
def f(t):
    f = t**2
    return f

#plt.plot(t, mesh_function(f(t), t))
#plt.show()


def g(t):
    g = np.zeros(len(t))
    for i in range(len(t)):
        if t[i] >= 0 and t[i] <= 3:
            g[i] = np.exp(-t[i])
        elif t[i] > 3 and t[i] <= 4:
            g[i] = np.exp(-3*t[i])
        else:
            print 't is not in region: 0 >= t >= 4'
            break
    return g

plt.plot(t, mesh_function(g(t), t))
plt.show()