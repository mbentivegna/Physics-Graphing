import matplotlib.pyplot as plt
import numpy as np 

x = np.linspace(-3*(np.pi)/2, 3*(np.pi)/2, 1000)
y1 = np.sin(6*x)
y2 = np.sin(x)
y3 = 0 *x

plt.plot(x, y1, label = "sin(Nα)")
plt.plot(x, y2, label = "sin(α)")
plt.plot(x, y3)

plt.legend(loc="upper right")
plt.xlabel("α")
plt.ylabel("Intensity")
plt.title("Interference Intensity (N = 6)")


plt.show()


def update(hello):
    pass