import matplotlib.pyplot as plt
import numpy as np 

x = np.linspace(0, 5, 1000)
y = 1.202 * np.exp(-2*x) *np.cos(3*x - .588)

plt.plot(x, y)

plt.xlabel("Time")
plt.ylabel("Position")
plt.title("Underdamped")


plt.show()


def update(hello):
    pass