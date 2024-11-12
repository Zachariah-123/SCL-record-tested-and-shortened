# 7.1 AIM: Program to find the solution of the first order
#differential equation
#dx/dt +2x = 0
#with the initial condition x(0) = 1

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

def f(x,t):
    dxdt = (-2)*x
    return dxdt
t = np.linspace(0,10,50)
x = odeint(f,1,t)
plt.ylabel("x")
plt.xlabel("t")
plt.plot(t,x)
plt.grid(True)
plt.show()
