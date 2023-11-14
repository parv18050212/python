l=[50,40,30,20,10]
i=1
while(i<len(l)):
    j=0
    while(j<(len(l))):
        if(l[j]>l[j+1]):
            l[j],l[j+j]=l[j+j],l[j]
        j = j+1
print(l)