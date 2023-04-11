import math

class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        return f"Vector({self.x}, {self.y}, {self.z})"

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.z == other.z

    def __ne__(self, other):
        return not self == other

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z

    def cross(self, other):
        return Vector(self.y * other.z - self.z * other.y,
                      self.z * other.x - self.x * other.z,
                      self.x * other.y - self.y * other.x)

    def length(self):
        return math.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)

    def __hash__(self):
        return hash((self.x, self.y, self.z))

v = Vector(5, 3, 8)
w = Vector(-2, -3, 1)

print(f"{v.__repr__()}")
print(f"{w.__repr__()}")
print(f"Are the vectors equal? {v.__eq__(w)}")
print(f"Are the vectors different? {v.__ne__(w)}")
print(f"v+w {v.__add__(w)}")
print(f"v-w {v.__sub__(w)}")
print(f"Dot product v and w: {v.__mul__(w)}")
print(f"Cross product v and w: {v.cross(w)}")
print(f"Length w: {w.length()}")
print(f"Length v: {v.length()}")

print(f"{v+w}")
print(f"{v-w}")
print(f"{v != w}")
print(f"{v - w == Vector(-1, 5, 1)}")
print(f"{v * w == 2}")
print(f"{v*w}")
print(f"{v.length() == math.sqrt(14)}")
print(f"{v.cross(w) == Vector(27, -21, -9)}")
S = set([v, v, w])
print(f"{len(S) == 2}")

print("\nTests passed")
