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
plt.title('Functions: sinx, cosx, exp(-x)')
plt.legend()
plt.show()

print("Ex.9.2")
