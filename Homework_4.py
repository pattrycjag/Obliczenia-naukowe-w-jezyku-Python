print("Ex.4.1")

n = int(input("Enter the number of points: "))
point_list = []
for i in range(n):
    x = float(input(f"Enter x value of point {i+1}: "))
    y = float(input(f"Enter y value of point {i+1}: "))
    point_list.append((x, y))


unit_circle = lambda p: p[0]**2 + p[1]**2 <= 1
coord_positive = lambda p: p[0] > 0 and p[1] > 0
sort_yx = lambda p: (-p[1], p[0])
sort_sum = lambda p: abs(p[0]) + abs(p[1])

circle_unit = list(filter(unit_circle, point_list))
positive_coords = list(filter(coord_positive, point_list))

point_list.sort(key=sort_yx)
sort_by_sum = sorted(point_list, key=sort_sum)

print("Points inside unit circle:")
for p in circle_unit:
    print(p)

print("Points with positive coordinates:")
for p in positive_coords:
    print(p)

print("Points sorted by y decreasing, x increasing:")
for p in point_list:
    print(p)

print("Points sorted by |x|+|y|:")
for p in sort_by_sum:
    print(p)

print("Ex.4.2")

def reverse_range_iterative(L, left, right):
    while left < right:
        L[left], L[right] = L[right], L[left]
        left += 1
        right -= 1

def reverse_range_recursive(L, left, right):
    if left >= right:
        return
    L[left], L[right] = L[right], L[left]
    reverse_range_recursive(L, left+1, right-1)

L = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
reverse_range_iterative(L, 3, 6)
print(L)
reverse_range_recursive(L, 2, 7)
print(L)
