s = [2,5,7,11,33]
r=[1]*r
l =[1]*l
n = len(s)
for i in range(1,n):
    l[i]=s[i-1]*l[i-1]
print(l)
for j in range(n-2,-1,-1):
    r[j] = s[j+1]*l[j+1]
print(l)
for k in range(0,n):
    ans = l[i]*r[i]
    l.append(ans)
print(l)