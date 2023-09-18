#print prime number btw the range and print sum of these number
n=int(input("enter the lower limit"))
n1=int(input("enter the upper limit"))
sum1=0
for k in range(n,n1):
    flag=True
    for i in range(2,k):
        if k%i==0:
            flag=False
            break
    if flag==True:
        print(k)
        sum1=sum1+k
print(sum1)     

