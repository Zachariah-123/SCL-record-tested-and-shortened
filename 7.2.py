import numpy as np
from numpy import exp
import matplotlib.pyplot as plt
from scipy.integrate import odeint

def f(i,t):
    didt = (-1)*i/3
    return didt
def f2(i,t):
    di2dt = -5*exp(-t) - i/3
    return di2dt
t = np.linspace(0,20,100)
i = odeint(f , 5 , t)
i2 = odeint(f2 , 5 , t)
plt.plot(t,i)
plt.plot(t,i2)
plt.legend(['DC current','AC current'])
plt.ylabel("Current")
plt.xlabel("Time")
plt.grid(True)
plt.show()
