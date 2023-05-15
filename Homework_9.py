import numpy as np
import matplotlib.pyplot as plt

print("Ex.9.1")
x = np.linspace(0, 10, 1000)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.exp(-x)

plt.plot(x, y1, color='red', linestyle='solid', label='sin(x)')
plt.plot(x, y2, color='green', linestyle='dashed', label='cos(x)')
plt.plot(x, y3, color='blue', linestyle='dotted', label='exp(-x)')

plt.xlabel('x')
plt.ylabel('y')
plt.title('9.1: Functions: sinx, cosx, exp(-x)')
plt.legend()
plt.show()

print("Ex.9.2")
n = 100
points = np.random.rand(n, 2)

colors = []
marker_areas = []

for point in points:
    x, y = point
    distance = np.sqrt(x**2 + y**2)
    if distance < 1:
        colors.append('green')
    else:
        colors.append('red')
    marker_area = np.abs(x) + np.abs(y)
    marker_areas.append(marker_area)

plt.scatter(points[:, 0], points[:, 1], c=colors, s=np.array(marker_areas)*100, alpha=0.5)
plt.xlim(0, 1)
plt.ylim(0, 1)
plt.xlabel('x')
plt.ylabel('y')
plt.title('9.2: Random Points')
plt.grid(True)

plt.show()
