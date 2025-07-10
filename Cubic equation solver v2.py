import math

print("="*50)
print("Cubic Equation Solver: ax³ + bx² + cx + d = 0")
print("="*50)

while True:
    try:
        a = float(input("\nEnter a (≠0): "))
        if a == 0:
            print("Error: 'a' cannot be 0 for a cubic equation.")
            continue
        b = float(input("Enter b: "))
        c = float(input("Enter c: "))
        d = float(input("Enter d: "))

        # Convert to depressed cubic: t³ + pt + q = 0
        f = ((3 * a * c) - (b ** 2)) / (3 * a ** 2)
        g = ((2 * b ** 3) - (9 * a * b * c) + (27 * a ** 2 * d)) / (27 * a ** 3)
        h = (g ** 2) / 4 + (f ** 3) / 27

        print("\nCalculating roots...")

        if h > 0:
            # One real root
            R = -(g / 2) + math.sqrt(h)
            S = math.copysign(abs(R) ** (1 / 3), R)
            T = -(g / 2) - math.sqrt(h)
            U = math.copysign(abs(T) ** (1 / 3), T)
            x1 = S + U - (b / (3 * a))
            print("\nOne real root:")
            print("x =", round(x1, 6))

        elif h == 0 and f == 0 and g == 0:
            # Triple real root
            x = - (d / a) ** (1 / 3)
            print("\nTriple real root:")
            print("x =", round(x, 6))

        else:
            # Three real roots
            i = math.sqrt((g ** 2 / 4) - h)
            j = i ** (1 / 3)
            k = math.acos(-(g / (2 * i)))
            x1 = 2 * j * math.cos(k / 3) - (b / (3 * a))
            x2 = 2 * j * math.cos((k + 2 * math.pi) / 3) - (b / (3 * a))
            x3 = 2 * j * math.cos((k + 4 * math.pi) / 3) - (b / (3 * a))
            print("\nThree real roots:")
            print("x1 =", round(x1, 6))
            print("x2 =", round(x2, 6))
            print("x3 =", round(x3, 6))

    except ValueError:
        print("Invalid input. Please enter numeric values.")

    again = input("\nDo you want to solve another equation? (y/n): ").lower()
    if again != 'y':
        print("\nExiting... Goodbye!")
        break
