# a=float(input("Enter first number: "))
# b=float(input("Enter 2nd number: "))

# operator=input("Please Select Operator: + - * / % : ")

# if operator=="+":
#     result=a+b
#     print(round(result,2))
# elif operator=="-":
#     result=a-b
#     print(round(result,2))
# elif operator=="*":
#     result=a*b
#     print(round(result,3))
# elif operator=="/":
#     result=a/b
#     print(round(result,3))
# elif operator=="%":
#     result=a%b
#     print(round(result,3))
    
# else:
#     print(f"{operator} is not a valid operator")
    
    # Challenge 2:
item=input("Which Item You want to Buy: ")
quantity=int(input(f"How many {item} you bought: "))
price=float(input(f"Whats the price for {item}: "))
total_price=price*quantity
    
if total_price>=100:
        discount=total_price*0.85
        print(discount)
else:
    discount=total_price*0.95
    print(discount)