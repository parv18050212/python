#take a list from user and update the list product of array except self

li = list(map(int, input().split()))
l1 = []
for i in range (0,len(li)):
    multiply=1
    for j in range (0,len(li)):
        if(i==j):
            continue
        multiply = multiply*li[j]
    
    l1.append(multiply)
print(l1)
    

