#take a list from user and integer t design an algorithm to print whose sum = t
n = int(input())
l = []
i = 0
while(i<n):
    x = int(input("enter elements in the list"))
    l.append(x)
    i = i+1
l.sort()
print(l)
t = int(input("enter a integer"))
k = 0
j = 1
while k<n:
    j = k+1
    while j<n:
        if(l[k]+l[j]==t):
            print(l[k],l[j])
        j = j+1
    k = k+1


