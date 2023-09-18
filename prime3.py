# print all prime number between the interval
n = int(input("enter a lower limit:"))
n1 = int(input("enter a upper limit:"))
for k in range(n,n1):
    flag=True
    for i in range(2,k):
        if k%i==0:
            flag=False
            break
    if flag == True:
        print(k)

