import random
import numba as nb

@nb.njit
def approximate_pi(num_points):
    points_in_circle = 0

    for _ in range(num_points):
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)

        if x**2 + y**2 <= 1:
            points_in_circle += 1

    return 4 * points_in_circle / num_points

input_points = [10, 10**2, 10**3, 10**4, 10**5, 10**6]

for num_points in input_points:
    pi = approximate_pi(num_points)
    print(f"Approximation with {num_points} points: {pi}")

