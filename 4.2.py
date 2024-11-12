import matplotlib.pyplot as plt
import numpy as np

plt.subplot(1,3,1)
data = np.random.normal(45,0.5,100000)
plt.hist(data , 200)
plt.title("1.")

plt.subplot(1,3,3)
data = np.random.randint(0,10,100000)
plt.hist(data , 20)
plt.title("2.")

plt.show()
