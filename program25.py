# Program 25 — Triangle area (Heron formula)

a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))
s = (a + b + c) / 2
area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
print("Area =", area)
