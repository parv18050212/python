i=int(input("enter a number:"))
num=1
for row in range(1,i+1):
    for column in range(1,row+1):
        print(num,end=" ")
        num=num+1
    print()