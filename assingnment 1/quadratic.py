import math

a,b,c =input().split()
a,b,c=int(a),int(b),int(c)


discriminant = b**2 - 4*a*c

if discriminant > 0:
    root1 = int((-b + math.sqrt(discriminant)) / (2*a))
    root2 = int((-b - math.sqrt(discriminant)) / (2*a))
    print("Real and Distinct")
    print(root2, root1)

elif discriminant == 0:
    root = int(-b / (2*a))
    print("Real and Equal")
    print(root, root)

else:
    print("Imaginary")