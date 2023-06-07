import unittest
import math

print("Ex.12.1")

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


class VectorTest(unittest.TestCase):
    def setUp(self):
        self.v = Vector(5, 3, 8)
        self.w = Vector(-2, -3, 1)

    def test_repr(self):
        self.assertEqual(repr(self.v), "Vector(5, 3, 8)")
        self.assertEqual(repr(self.w), "Vector(-2, -3, 1)")

    def test_eq(self):
        self.assertFalse(self.v == self.w)
        self.assertTrue(self.v == Vector(5, 3, 8))

    def test_ne(self):
        self.assertTrue(self.v != self.w)
        self.assertFalse(self.v != Vector(5, 3, 8))

    def test_add(self):
        result = self.v + self.w
        self.assertEqual(result, Vector(3, 0, 9))

    def test_sub(self):
        result = self.v - self.w
        self.assertEqual(result, Vector(7, 6, 7))

    def test_mul(self):
        result = self.v * self.w
        self.assertEqual(result, -11)

    def test_cross(self):
        result = self.v.cross(self.w)
        self.assertEqual(result, Vector(27, -21, -9))

    def test_length(self):
        result = self.w.length()
        self.assertEqual(result, math.sqrt(14))

    def test_hash(self):
        v_hash = hash(self.v)
        w_hash = hash(self.w)
        self.assertNotEqual(v_hash, w_hash)

    def test_set(self):
        S = set([self.v, self.v, self.w])
        self.assertEqual(len(S), 2)


if __name__ == "__main__":
    unittest.main()
