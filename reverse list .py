n = int(input("no of elements in list:"))
l =[]
i = 0
while(i<n):
    x =input("elements in list :")
    l.append(x)
    i = i+1
print(l)
lenth = len(l)
#l =[1,2,3,4,5]
start = 0
end = n-1
while start<end:
    l[start],l[end]=l[end],l[start]
    start+=1
    end-=1
print(l)