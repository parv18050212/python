n=int(input())
flag=True
for i in range (2,n):
    if(n % i==0):
        print("Not Prime")
        flag=False
        break
if (flag==True):
    print("Prime")