#ncr = n! / (n-r)! r!

#npr = n!/ (n-r)!
n= int(input())
r=int(input())
def fac (t):
    ans = 1
    for i in range(1,t+1):
        ans = ans*i
    return ans

print(fac(n)/fac(n-r)*fac(r)) 
print(fac(n)/fac(n-r))
