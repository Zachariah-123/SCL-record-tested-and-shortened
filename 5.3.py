import numpy as np
from scipy.integrate import *

def f(t):
    return 4*t**2 + 3
tmin = -2
tmax = 2
n = 10
t = np.linspace(tmin,tmax,n+1)
ft= f(t)
result = trapezoid (ft,t)
r1 = simpson(ft,x=t)
print(result ,r1)
