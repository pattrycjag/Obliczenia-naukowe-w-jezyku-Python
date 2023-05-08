import numpy as np


print("Ex.8.1")

print("Ex.8.1 a)")
array1 = np.linspace(0.0, 1.0, 11)
print(array1)

print("\nEx.8.1 b)")
array2= np.zeros((5, 6), dtype=np.int8)
print(array2)

print("\nEx.8.1 c)")
x = complex(0, 1)
powers_of_x1 = np.power(x, np.arange(9))
array3 = np.array(powers_of_x1)
print(array3)

powers_of_x2 = np.array([x**i for i in range(9)], dtype=np.complex128)
print(powers_of_x2)

print("\nEx.8.2")
print("Ex.8.2 a)")
v1 = np.array([3, 6, 9, 12, 15, 18, 21, 24])
print(v1)

print("\nEx.8.2 b)")
v2 = v1[1::2]
print(v2)

print("\nEx.8.2 c)")
v3 = v1[::-1]
print(v3)

print("\nEx.8.3")
print("Ex.8.3 a)")

m1 = np.array([[7, 2, 9, 0, 5],
               [98, 17, 81, 91, 10],
               [111, 121, 7, 14, 1],
               [16, 90, 1, 9, 2]])
print(m1)


print("\nEx.8.3 b)")
m2 = np.flip(m1, axis=1)
print(m2)

print("\nEx.8.3 c)")
m3 = np.flip(m1, axis=0)
print(m3)

print("\nEx.8.3 d)")
m4 = m1[1:-1, 1:-1]
print(m4)

m5 = np.delete(m1, [0, m1.shape[0] - 1], axis=0)
m5 = np.delete(m5, [0, m5.shape[1] - 1], axis=1)
print(m5)




