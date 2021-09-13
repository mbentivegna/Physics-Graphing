import matplotlib.pyplot as plt
import numpy as np 

x = np.linspace(-3*(np.pi)/2, 3*(np.pi)/2, 1000)
y = (np.sin(6*x)/np.sin(x))**2

plt.plot(x, y)

plt.xlabel("α")
plt.ylabel("Intensity")
plt.title("Interference Intensity (N = 6)")


plt.show()


def update(hello):
    pass