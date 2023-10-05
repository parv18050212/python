i=int(input("enter the number:"))
for row in range(1,i+1):
    for space in range(1,i-row+1):
        print(" ", end=" ")
    for star in range(i-row+1,i+1):
        print("*", end=" ")
    print()