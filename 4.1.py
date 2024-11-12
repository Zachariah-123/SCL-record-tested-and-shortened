import matplotlib.pyplot as plt
import numpy as np
data = np.random.random(100)
x= np.arange(1,100)
plt.subplot(2,5,1)
plt.stem(x[:20],data[:20])
plt.title("Stem plot")

plt.subplot(2,5,3)
plt.boxplot(data)
plt.title("Box plot")

plt.subplot(2,5,5)
x_bar= np.arange(1,11)
data_bar = np.random.randint(1,29,size = 10)
plt.bar(x_bar , data_bar)
plt.title("Bar Plot")


plt.subplot(2,5,7)
y = np.random.random(100)
plt.scatter(data , y)
plt.title("Scatter plot")
plt.show()
