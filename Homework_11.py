import numpy as np
import matplotlib.pyplot as plt

D, Nx, Nt, L, T = 1.0, 50, 500, 1.0, 0.1

t = np.linspace(0, T, num=Nt+1, dtype=float)
x = np.linspace(0, L, num=Nx+1, dtype=float)
dx = x[1] - x[0]

dt = 0.25 * (dx*dx) / D
r = D * dt / (dx*dx)
print("r = {}".format(r))

u = np.empty((Nx+1, Nt+1), dtype=float)

# initial condition, t=0
u[:, 0] = np.sin(2*np.pi*x)

# boundary conditions, x=0 and x=L=1
u[0, :] = np.cos(2*np.pi*t)
u[Nx, :] = 15

for j in range(Nt):
    u[1:-1, j+1] = r * u[:-2, j] + (1 - 2*r) * u[1:-1, j] + r * u[2:, j]


plt.title("1D heat equation")
plt.xlabel("x")
plt.ylabel("time")

plt.imshow(u, cmap='hot', interpolation='nearest')
plt.colorbar()
plt.show()
