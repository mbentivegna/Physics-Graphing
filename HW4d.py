import matplotlib.pyplot as plt
import numpy as np 

x = np.linspace(-(np.pi), np.pi, 1000)
y = (np.sin(2*x)/np.sin(x))**2

plt.plot(x, y)

plt.xlabel("α")
plt.ylabel("Intensity")
plt.title("Interference Intensity (N = 2)")


plt.show()


def update(hello):
    pass