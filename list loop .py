n = int(input("no of elements in list:"))
l =[]
i = 0
while(i<n):
    x =input("elements in list :")
    l.append(x)
    i = i+1
l.sort()
print(l[-1])
print(l[-2])
print(l[-3])