# exercise 5

import numpy as np
import matplotlib.pyplot as plt

def solver(I, a, t_end, dt):
    """
        calculate numerical error from using
        Forward Euler, Backwards Euler and Crank-Nicolson
        on the differential equation:
            u'(t) = -au(t)
        with initial condition u(0) = I
        in timeframe 0 < t < t_end
    """
    
    Nt = int(round(t_end/dt))
    t_end = Nt*dt
    t = np.linspace(0, t_end, Nt+1)
    u_f = np.zeros(Nt+1)
    u_b = np.zeros(Nt+1)
    u_cn = np.zeros(Nt+1)
    u_f[0] = I
    u_b[0] = I 
    u_cn[0] = I
    u_exact = np.zeros(Nt+1)
    for i in range(Nt+1):
        u_exact[i] = I*np.exp(-a*t[i])
    for i in range(0, Nt):
        u_f[i+1] = u_f[i]*(1 - a*dt)
        u_b[i+1] = u_b[i]/(1 + a*dt)
        u_cn[i+1] = (u_cn[i]*(1 - 0.5*a*dt))/(1 + 0.5*a*dt)
    error_f = np.zeros(Nt+1)
    error_b = np.zeros(Nt+1)
    error_cn = np.zeros(Nt+1)
    for i in range(Nt+1):
        error_f[i] = u_exact[i] - u_f[i]
        error_b[i] = u_exact[i] - u_b[i]
        error_cn[i] = u_exact[i] - u_cn[i]
    return error_f, error_b, error_cn, t

time_step = 0.2
dt = [time_step, 0.25*time_step, 0.125*time_step]
for i in range(3):
    f, b, cn, t = solver(5, 2, 5, dt[i])

    plt.plot(t, f, 'g--', t, b, 'r--', t, cn, 'b--')
    plt.legend(['Forward', 'Backward', 'Crank-Nicolson'])
    plt.xlabel('t'), plt.ylabel('error')
    plt.title('numerical error using finite difference')
plt.show()

