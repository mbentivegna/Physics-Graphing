import matplotlib.pyplot as plt
import numpy as np 

x = np.linspace(-2*(np.pi), 2*np.pi, 1000)
y = ((np.sin(2*6*x)/np.sin(6*x))**2)*(np.sin(x)/x)**2

plt.plot(x, y)

plt.xlabel("β")
plt.ylabel("Intensity")
plt.title("Combined Plot")


plt.show()


def update(hello):
    pass