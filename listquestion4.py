#take a list from user and break it into two list first one store all the even indexing and second one odd indexing
n = int(input())
l = []
i = 0
while (i<n) :
    x = int(input())
    l.append(x)
    i = i+1
print(l)
odd = []
even = []
for k in range (len(l)):
    if k % 2 == 0:
        even.append(l[k])
    else:
        odd.append(l[k])
print(odd)
print(even)
