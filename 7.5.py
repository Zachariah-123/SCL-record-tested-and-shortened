'''
7.4 AIM Solve the second order differential equation
 d2y/dx2 + 2dy/dx +2y = cos(2x) with initial conditions y(0)=0
 and y’(0)=0 , xrange=(1,10,200
 '''

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

def f(y,x):
    y,z=y
    dydx = [z,np.cos(2*x)-2*z -2*y]
    return dydx
x = np.linspace(1,10,200)
sol = odeint(f , [0,0] , x)
plt.plot(x , sol[:,0])
plt.grid()
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend(["Solution of ODE",['']])
plt.show()
