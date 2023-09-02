# a student will  ot be allowed to sit in exams if his attendace is less tham 75% take following input from user
# number of classes held,number of classes attended,and print percentage of class attended Ias a student is allowed to sit in exams or not

noh = input("Enter the number of class held:")
noa = input("Enter the number of class attended:")
noa = int(noa)
noh = int(noh)
per = (noa/noh)*100
if per >= 75 :
    print("you can sit in exmas")
else:
    print("you cannot sit in exams")
    