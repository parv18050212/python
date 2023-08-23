First = (input("Enter the first number:"))
First = (int(First))
Second = (input("Enter the secod number:"))
Second = (int(Second))
print("press the +,-,*,/,**,//, %, for operators ")
operator = input("operator:")
if operator == "+": 
    print(First + Second)
elif operator == "-":
    print(First - Second)
elif operator == "*":
    print(First * Second)
elif operator == "/":
    print(First / Second)
elif operator == "%" :
    print(First % Second)
elif operator == "**":
    print(First ** Second)
elif operator == "//":
    print(First // Second)
else :
    print( " Operator Error ")