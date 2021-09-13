import matplotlib.pyplot as plt
import numpy as np 

x = np.linspace(0.000001, 3, 1000)
axes = plt.gca()
axes.set_ylim([0,.5])
y1 = x/3
y2 = (1/3)*(1/x**2)
plt.plot(x[x<1], y1[x<1], color = "black")
plt.plot(x[x>1], y2[x>1], color = "black")
plt.plot(1, 1/3, marker = '.', markersize = 15, color = "blue")
plt.annotate("Boundary", (1.1, .35))
plt.xlabel("Distance from Center (R)")
plt.ylabel("Electric Field")
plt.title("Electric Field Plot")
ax = plt.gca()
ax.axes.yaxis.set_ticks([])


plt.show()

def update(hello):
    pass