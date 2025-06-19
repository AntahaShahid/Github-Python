#lets make python calculator without any cheating and tutorial:

a=float(input("Enter the value for a: "))
b=float(input("Enter the value for b: "))
print("Which operator you want:  + , - , * , / , % ")
operator=input("Which operator you want:  ")




#Addition: 
if operator=="+":
    print(f"The result for addition is: ", a+b)
#Subtraction:
elif operator=="-":
    print(f"The result for subtraction is: ", a-b)
#Multiplication:
elif operator=="*":
    print(f"The result for multiplication is: ", a*b)
#Division:
elif operator=="/":
    print(f"The result for division is: ", a/b)
#Remainder/Moduele:
elif operator=="%":
    print(f"The result for remainder is: ", (round(a%b,2)))
else:
    print(f"{operator} is not valid operator")