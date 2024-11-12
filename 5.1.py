'''5.1 AIM:Compute and plot the first and second deriva
tives for the functions sin t, cos t, sinht and cosht for the
 vector t =[0: 10] with increment 0.01 using grad'''
import numpy as np
import matplotlib.pyplot as plt

t = np.arange(0,10,0.01)
y1 = np.sin(t)
y2 = np.cos(t)
y3 = np.sinh(t)
y4 = np.cosh(t)


def ddt(a,t):
    return np.gradient(a,t)


plt.plot(t,ddt(y1,t))
plt.plot(t,ddt(ddt(y1,t),t))
plt.title("Sine")
plt.show()


plt.plot(t,ddt(y2,t))
plt.plot(t,ddt(ddt(y2,t),t))
plt.title("Cosine")
plt.show()


plt.plot(t,ddt(y3,t))
plt.plot(t,ddt(ddt(y3,t),t))
plt.title("Sinh")
plt.show()


plt.plot(t,ddt(y4,t))
plt.plot(t,ddt(ddt(y4,t),t))
plt.title("Cosh")
plt.show()
