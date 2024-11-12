import numpy as np
from numpy import exp
import matplotlib.pyplot as plt
from scipy.integrate import odeint

def f(i , t):
    didt=5*exp(-t) - i
    return didt
t = np.linspace (0 , 20 , 100)
i = odeint(f , 0 , t)
plt.plot(t, i)
plt.xlabel("Time")
plt.ylabel("Current")
plt.legend(["AC current"])
plt.show()
