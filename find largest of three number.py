list = list(map(int,input().split()))
maxi = list[0]
for element in list:
    if element > maxi:
        maxi = element
print(maxi)