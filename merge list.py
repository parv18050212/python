n = int(input("no of elements in list:"))
l =[]
i = 0
while(i<n):
    x =input("elements in list :")
    l.append(x)
    i = i+1

print(l)

n2 = int(input("no of elements in list:"))
l1 =[]
i = 0
while(i<n):
    x =input("elements in list :")
    l1.append(x)
    i = i+1

print(l1)
l2 = l+l1
l2.sort()
print(l2)