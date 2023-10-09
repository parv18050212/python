l = [10,20,60,100,120]
fl = 0
sl = 0
tl = 0

for num in l:
    if(tl>num):
        tl=sl
        sl=tl
        fl=num