#print first n prime numbers
n = int(input("enter a number"))
cnt=0
a=2
while(cnt<n):
    flag=True
    for i in range (2,a):
        if (a%i == 0):
            flag=False
            break
    if (flag==True):
        print(a)
        cnt+=1
    a+=1