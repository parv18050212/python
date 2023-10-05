i = int(input("enter a number :"))
# for row in range(1,i+1):
#     for column in range(1,row+1):
#         print( column ,end="") 
#     print()
row=1
while (row<i+1):
    col=1
    while(col<row+1):
        print(col,end="")
        col=col+1
    row=row+1
    print()

