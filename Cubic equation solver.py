import math

print("Solving equation: ax³ + bx² + cx + d = 0")

# Input coefficients
a = float(input("Enter a (≠0): "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))
d = float(input("Enter d: "))

# Convert to depressed cubic: t³ + pt + q = 0
f = ((3 * a * c) - (b ** 2)) / (3 * a ** 2)
g = ((2 * b ** 3) - (9 * a * b * c) + (27 * a ** 2 * d)) / (27 * a ** 3)
h = (g ** 2) / 4 + (f ** 3) / 27

if h > 0:
    # One real root
    R = -(g / 2) + math.sqrt(h)
    S = math.copysign(abs(R) ** (1 / 3), R)
    T = -(g / 2) - math.sqrt(h)
    U = math.copysign(abs(T) ** (1 / 3), T)
    x1 = S + U - (b / (3 * a))
    print("One real root:", x1)

elif h == 0 and f == 0 and g == 0:
    # Triple real root
    x = - (d / a) ** (1 / 3)
    print("Triple real root:", x)

else:
    # Three real roots
    i = math.sqrt((g ** 2 / 4) - h)
    j = i ** (1 / 3)
    k = math.acos(-(g / (2 * i)))
    m = math.cos(k / 3)
    n = math.cos((k + 2 * math.pi) / 3)
    p = math.cos((k + 4 * math.pi) / 3)
    sqrt3 = math.sqrt(3)

    x1 = 2 * j * m - (b / (3 * a))
    x2 = 2 * j * n - (b / (3 * a))
    x3 = 2 * j * p - (b / (3 * a))
    print("Three real roots:")
    print("x1 =", x1)
    print("x2 =", x2)
    print("x3 =", x3)
