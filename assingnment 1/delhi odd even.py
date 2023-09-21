n = int(input())
for _ in range(n):
    car_num = input()
    car_str = str(car_num)
    even_sum = 0
    odd_sum = 0

    for digit in car_str:
        digit_value = int(digit)
        if digit_value % 2 == 0:
            even_sum += digit_value
        else:
            odd_sum += digit_value

    if (even_sum % 4 == 0 or odd_sum % 3 == 0):
        print("Yes")
    else:
        print("No")
