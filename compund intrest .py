P = float(input())
R = float(input())
t = 2
n = 1
r = R / 100
C = P * (1 + (r / n)) ** (n * t) - P
print(round(C, 2))
