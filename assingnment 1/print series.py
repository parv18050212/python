N1 = int(input())
N2 = int(input())

count = 0
n = 1

while count < N1:
    t = 3 * n + 2

    if t % N2 != 0:
        print(t)
        count += 1

    n += 1