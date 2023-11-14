#take a list from user and find the maximum and minimum element of the list without using inbuilt function
import math
n = int(input())
l =[]
i = 0
while(i<n):
    x = int(input())
    l.append(x)
    i = i+1
print(l)
maxi = -math.inf
mini = math.inf
# mini = maxi = l[0] another method for solving this question
for element in l:
    if element < mini:
        mini = element
    elif element > maxi:
        maxi = element

print("Minimum element:", mini)
print("Maximum element:", maxi)