#EXERCISE 3.1
print("Ex.3.1")
word = "Patrycja"

n = int(len(word))

print("+-----" * n + "+")
print("|"+"|".join(i.center(5) for i in word) + "|")
print("+-----" * n + "+")


#EXERCISE 3.2
print("Ex.3.2")

#instrukcja while
x=1
while x <= 40:
    if x == 13:
        x += 1
        continue
    if x % 5 == 0 and x % 7 == 0:
        print(f"{x} is divided by 5 and 7")
    elif x % 5 == 0:
        print(f"{x} is divided by 5")
    elif x % 7 == 0:
        print(f"{x} is divided by 7")
    else:
        print(f"{x} is not important")
    x += 1

print("\n")
#instrukcja for
for x in range(1, 41):
    if x == 13:
        x=x+1
        continue
    if x % 5 == 0 and x % 7 == 0:
        print(f"{x} is divided by 5 and 7")
    elif x % 5 == 0:
        print(f"{x} is divided by 5")
    elif x % 7 == 0:
        print(f"{x} is divided by 7")
    else:
        print(f"{x} is not important")

#EXERCISE 3.3
print("Ex.3.3")
import math

n = 2022
x = round(math.pi, 5)
word = "Python"
polish = "book"

with open("vars.txt", "w") as f:
    f.write(f"{n}\n")
    f.write(f"{x}\n")
    f.write(f"{word}\n")
    f.write(f"{polish}\n")

with open("vars.txt", "r") as f:
    print(f.read())





