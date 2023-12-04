#given a string of lower case letterreduce it by  removing the character which appear more than k times in the string


st = input()
k = int(input())
d = {}
for i in st:
    if i in d:
        d[i] = d[i]+1
    else:
        d[i] = 1
res = ""
for i in st:
    if d[i]<k:
        res+=i
print(res)
       
        

