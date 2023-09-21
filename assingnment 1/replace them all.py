n=int(input())
n1=0
if n==0:
    n=5
while n>0:
    a=n%10
    if a==0:
        a=5
    n=n//10
    n1=n1*10+a

n=0
while n1>0:
    r=n1%10 
    n=n*10+r
    n1=n1//10
print(n)