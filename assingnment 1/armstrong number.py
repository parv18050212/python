n=int(input())
sum=0
o=len(str(n))
n1=n
while(n>0):
    d=n%10
    sum+=d**o
    n=n//10
if(sum==n1):
    print("true")
else:
    print("false")