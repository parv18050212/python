First = (input('Enter the first number:'))
Second = (input("Enter the seconf number"))
First = (int(First))
Second = (int(Second))
print("For arithmetic operator press +,-,*,/----------")

operator = input("operator:")
if operator == "+": 
    print(First + Second)
elif operator == "-":
    print(First - Second)
elif operator == "*":
    print(First * Second)
elif operator == "/":
    print(First / Second)
else:
    print("Invalid Operator")
  