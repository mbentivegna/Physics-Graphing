import matplotlib.pyplot as plt
import numpy as np 

x = np.linspace(-3*(np.pi), 3*(np.pi), 1000)
y = (np.sin(x)/x)**2

plt.plot(x, y)

plt.xlabel("β")
plt.ylabel("Intensity")
plt.title("Single Slit Defraction Pattern")


plt.show()


def update(hello):
    pass