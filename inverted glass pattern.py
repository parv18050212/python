def print_inverted_glass_pattern(n):
    for i in range(n, 0, -1):
        for j in range(n, i, -1):
            print(j, end=" ")
        for k in range(2 * (i - 1)):
            print(" ", end=" ")
        for l in range(i, n + 1):
            if l < n:
                print(l, end=" ")
            else:
                print(l, end="")
        print()

n = 5
print_inverted_glass_pattern(n)

