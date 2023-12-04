# st = input()
# flag = True
# for i in st:
#     if st.count(i) == 1 :
#         print(i)
#         flag = False
#         break
# if (flag == True):
#     print("None")
st = input()
d = {}
for i in st:
    if i in d:
        d[i] = d[i]+1
    else:
        d[i] = 1
flag = True
for i in st:
    if d[i]==1:
        print(i)
        flag = False
        break

if flag == True:
    print("None")
