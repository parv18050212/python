
n= int(input())
li = list(map(int, input().split()))

mx = max(li[0], li[1])
secondmax = min(li[0], li[1])
n = len(li)
for i in range(2, n):
    if li[i] > mx:
        secondmax = mx
        mx = li[i]
    elif li[i] > secondmax and mx != li[i]:
        secondmax = li[i]
    elif mx == secondmax and secondmax != li[i]:
        secondmax = li[i]
 
print(secondmax)