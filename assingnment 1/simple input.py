sum1 = 0

while True:
    num = int(input())
    sum1 = num + sum1
    if sum1 < 0:
        break
    print(num)