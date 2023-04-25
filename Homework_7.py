import math
import itertools
import random

print("\nEx.7.1")
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

    def normalize(self):
        length = self.length()
        if length == 0:
            raise ValueError("Cannot normalize a zero vector")
        return Vector(self.x / length, self.y / length, self.z / length)

    def find_axis(vector1, vector2):
        if vector1.cross(vector2).length() == 0:
            raise ValueError("vector_1 and vector_2 are parallel (or zero)")
        return vector1.cross(vector2).cross(vector1).cross(vector2).normalize()


v = Vector(5, 3, 8)
w = Vector(5, 3, 8)

try:
    axis = Vector.find_axis(v, w)
    print(f"Axis: {axis}")
except ValueError as x:
    print(f"ValueError: {x}")


print("\nEx.7.2")

def zero_one():
    yield from ((i & 1) for i in itertools.count())

def random_zero_one():
    yield from (random.randint(0, 1) for _ in itertools.count())

def zero_one_minus_one():
    yield from itertools.cycle([0, 1, 0, -1])

print("Iterator 0 1")
iter_a = zero_one()
for i in itertools.islice(iter_a, 10):
    print(i, end=" ")
print("\n\nIterator random 0 1")

iter_b = random_zero_one()
for i in itertools.islice(iter_b, 10):
    print(i, end=" ")
print("\n\nIterator 1 0 -1")
iter_c = zero_one_minus_one()
for i in itertools.islice(iter_c, 10):
    print(i, end=" ")
print("\n")
