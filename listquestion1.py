# take a list from the user and generate pairs
l = list(map(int,input().split()))
l1 = len(l)
i = 0
j = 1
while i<l1:
    j = i+1
    while j<l1:
        print(l[i],l[j])
        
        j = j+1
    i = i+1

