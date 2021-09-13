import matplotlib.pyplot as plt
import numpy as np 

x = np.linspace(0.000001, 3, 1000)
y1 = .5 * (1-(x**2)/3)
y2 = (1/3) * 1/x
plt.plot(x[x<1], y1[x<1], color = "black")
plt.plot(x[x>1], y2[x>1], color = "black")
plt.plot(1, 1/3, marker = '.', markersize = 15, color = "blue")
plt.annotate("Boundary", (1.1, .35))
plt.xlabel("Distance from Center (R)")
plt.ylabel("Electric Potential")
plt.title("Electric Potential Plot")
ax = plt.gca()
ax.axes.yaxis.set_ticks([])


plt.show()

def update(hello):
    pass