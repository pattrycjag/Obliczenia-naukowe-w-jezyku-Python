##11.1
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

##11.2
Nx, Nt, L, T, c = 20, 100, 1.0, 2.0, 1.0
t = np.linspace(0, T, num=Nt+1, dtype=float)
x = np.linspace(0, L, num=Nx+1, dtype=float)
dx = x[1] - x[0]
dt = t[1] - t[0]
r = (c * dt / dx) ** 2
print("r =", r)
assert r < 1

u = np.empty((Nx+1, Nt+1), dtype=float)

u[:, 0] = np.abs(x - L/2) - L/4  #fala, która jest symetryczna względem środka odcinka [0, L] i ma wartość maksymalną w środku odcinka.

# boundary condition, x=0 and x=L
u[0, :] = 0.0
u[Nx, :] = 0.0

# initial condition j=1
u[1:-1, 1] = u[1:-1, 0] + (r * 0.5) * (u[:-2, 0] - 2 * u[1:-1, 0] + u[2:, 0])

for j in range(1, Nt):
    u[1:-1, j+1] = -u[1:-1, j-1] + 2 * u[1:-1, j] + r * (u[:-2, j] - 2 * u[1:-1, j] + u[2:, j])

plt.title("1D wave equation")
plt.xlabel("t")
plt.ylabel("x")

plt.imshow(u, cmap='hot', interpolation='nearest')

plt.colorbar()
plt.show()

