 # take a list from user and rotate it in clockwise direction

# n = int(input("Enter the no of elements in the list"))
# l = []
# i = 0
# while(i<n):
#     x = int(input("enter elements in the list"))
#     l.append(x)
#     i = i+1
# print(l)
# k = int(input("enter the position"))
# k = k % len(l)
# l2 = l[-k:] + l[:-k]
# print(l)
# print(l2)

l = list(map(int,input().split()))
n=len(l)
temp = l[n-1]
i = n-2
while i>=0 :
    l[i+1]=l[i]
    i=i-1
l[0]=temp
print(l)
