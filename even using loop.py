#to find even number btw two limits abd sum of them
n=1
n1=int(input("enter a number"))
sum1=0
for k in range(n,n1):
    flag=True
    for i in range(1,k):
        if k%2==0:
            flag=False
            break
    if flag==False:
        print(k)
        sum1=sum1+k
print(sum1)


