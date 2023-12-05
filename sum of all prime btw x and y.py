def check_prime(t):
    for i in range(2,t):
        if t%i == 0:
            return False
    return True

x = int(input())
y = int(input())
s = 0
for i in range(x,y+1):
    if(check_prime(i)):
        print(i)
        s = s+i
print(s)


