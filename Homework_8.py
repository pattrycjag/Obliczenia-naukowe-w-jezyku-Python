import numpy as np


print("Ex.8.1")

print("Ex.8.1 a)")
array_a = np.arange(0.0, 1.1, 0.1)
print(array_a)

print("\nEx.8.1 b)")
array_b = np.zeros((5, 6), dtype=np.int8)
print(array_b)

print("\nEx.8.1 c)")
x = complex(0, 1)
powers_of_x = np.power(x, np.arange(9))
array_c = np.array(powers_of_x)
print(array_c)

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
import numpy as np

m1 = np.array([[1, 2, 3, 4, 5],
               [6, 7, 8, 9, 10],
               [11, 12, 13, 14, 15],
               [16, 17, 18, 19, 20]])
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




