import matplotlib.pyplot as plt
import numpy as np 

x = np.linspace(0.000001, 3, 1000)
axes = plt.gca()
axes.set_ylim([0,1.2])
y1 = 1*(x/x)
y2 = (1/x)
plt.plot(x[x<1], y1[x<1], color = "black")
plt.plot(x[x>1], y2[x>1], color = "black")
plt.plot(1, 1, marker = '.', markersize = 15, color = "blue")
plt.annotate("Boundary", (1.05, 1.05))
plt.xlabel("x")
plt.ylabel("y(x)")
plt.title("Electric Potential Plot")
ax = plt.gca()

plt.show()

def update(hello):
    pass