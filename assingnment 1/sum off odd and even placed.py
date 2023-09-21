N = int(input())

odd = 0
even = 0
position = 1  

while N > 0:
    digit = N % 10   
    if position % 2 == 0:
        even += digit
    else:
        odd += digit
    N //= 10  
    position += 1

print(odd)
print(even)