n=input()
n=int(n)

dec,i = 0,0

while n>0: 
    r=n%10
    exp=r*(2**i)
    dec=dec+exp
    n=n//10
    i+=1
print(dec)