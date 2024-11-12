from numpy import *
from scipy.integrate import simpson
from scipy.signal import square
import matplotlib.pyplot as plt
T=2
dutycycles = 0.5
samples = 1000
terms = int(input("Enter number of terms:"))

plt.subplot(2,2,1)
x= linspace(0,T,samples)
plt.subplot(2,2,1)
y=square(2*pi*x/T,duty = dutycycles)
a0 = (2/T)*simpson(y, dx = T/samples)
an = lambda n: (2/T)*simpson(y*cos(2*pi*n*x/T), dx=T/samples)
bn = lambda n: (2/T)*simpson(y*sin(2*pi*n*x/T), dx=T/samples)
s= a0/2 + sum(an(k)*cos(2*pi*k*x/T)+bn(k)*sin(2*pi*k*x/T) for k in range (1,terms+1))
plt.plot(x,s)
plt.plot(x,y)
plt.grid()
plt.show()
