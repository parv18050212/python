N1=int(input())
N2=int(input())
if N1>N2:
    n=N1
else:
    n=N1
for i in range(1,n+1):
    if N1%i==0 and N2%i==0:
        hcf=i
print(hcf)