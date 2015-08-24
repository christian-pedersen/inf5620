# exercise 2

import numpy as np
import matplotlib.pyplot as plt

def differentiate(u, dt):
    steps = len(u)
    d = np.zeros(steps)
    d[0] = (u[1]-u[0])/dt
    for n in range(1, steps-1):
        d[n] = (u[n+1] - u[n-1])/(2*dt)
    d[-1] = (u[-1] - u[steps-2])/dt
    return d

def mesh_function(f, t):
    length = len(t)
    u = np.zeros(length)
    for i in range(length):
        u[i] = f[i]
    return u


def test_differentiate():
    """
        test differentiate on function
        t**2. Exact solution is 2t
    """
    dt = 0.1
    Nt = 5/dt
    t = np.linspace(0,5,Nt+1)
    func = lambda t: t**2
    exact = lambda t: 2*t
    diff = differentiate(mesh_function(func(t), t), dt)
    for i in range(len(t)):
        difference = diff[i] - exact(t[i])
        if abs(difference) >= 1e-13:
            print 'numerical error = %g in timestep %g' % (difference,i)
    plt.plot(t, exact(t), 'b-', t, diff, 'r--')
    plt.legend(['exact', 'numerical'])
    plt.show()
    

if __name__ == "__main__":
    test_differentiate()
    