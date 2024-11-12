from numpy import cos , linspace , pi
import matplotlib.pyplot as plt

def f1(t):
    return cos(2*pi*t)
def f2(t):
    return cos(2*pi*t)*cos(2*pi*5*t)+ cos(2*pi*5*t)
t = linspace(-1,1,10000)
plt.plot(t,f1(t))
plt.plot(t,f2(t))
plt.legend(["f1(t)","f2(t)"])
plt.show()
