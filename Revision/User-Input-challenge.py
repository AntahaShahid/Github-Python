# Error in User Input

# input=int(input("Enter a number: "))
# print(input)

#-------->>>>>> When User enters the abc or lets say words/string in the int input then program crashes, 
#--------So to avoid it lets use try-except,, So..

# try:
#     input=int(input("Enter a number: "))
#     print(input)
# except:
#     print("Please Enter a Valid number")
    
# try:
#     age=int(input("Enter your Age: "))
#     print(f"Next Year You Will be {age+1}")
# except ValueError:
#     print("Please Enter a Valid number") #-> This program also runs without writing valueError in 
#                                                 #except statment

# # Task 1:

# # Area of Rectangle:

# try:
#    length=float(input("Enter the length of a rectangle: "))
#    width=float(input("Enter the width of a rectangle: "))
#    area=length * width
#    print(f"The Area of rectangle is: {area}")
# except ValueError:
#   print("an incorrect, Please Enter correct value")
  
    # print(f"{area} an incorrect, Please Enter correct value")
    
# Task 2:

# Shopping Cart:


# item=input("What you want to buy ?")
# quantity=int(input(f"How many {item} you have bought ?"))
# price=float(input("Whats the Price ?"))

# Total_cost = price * quantity

# # 10% discount:
# try:
#   print(Total_cost * 0.90)
# except ValueError:
#     print("No discount")

###---This Program worked smoothly until there is no try except for discount but as we write
###---it there comes error, so to avoid this we will do this program by if else statment..

# item=input("What you want to buy ?")
# quantity=int(input(f"How many {item} you have bought ?"))
# price=float(input("Whats the Price ?"))

# Total_cost = price * quantity

# # 10% discount:
# if Total_cost>100:
    
#   print(Total_cost * 0.90)
# else:
#     print(f"Your final price is {Total_cost} No discount on less than 100rs shopping")

#Task 3:

# item=input("What you want to buy ? ")

# quantity=int(input(f"How many {item} you have bought ? "))
# price=float(input("Whats the Price ?"))

# Total_cost = price * quantity(item)

# print(Total_cost)


# Ask the user how many different items they want to buy
# num_items = int(input("How many different items do you want to buy? "))

# total_cost = 0  # Initialize total cost

# Loop through the number of items the user wants to buy

# Ask the user how many different items they want to buy
# num_items = int(input("How many different items do you want to buy? "))

# total_cost = 0  # Initialize total cos
# for i in range(num_items):
#     item = input(f"What do you want to buy (Item {i+1})? ")
#     quantity = int(input(f"How many {item}s did you buy? "))
#     price = float(input(f"What is the price of one {item}? "))

#     # Calculate the cost for this item and add to total cost
#     total_cost += price * quantity

# # Print the final total cost
# print(f"Total cost for all items: {total_cost}")

##---Doing by own logic:----------...>>>>::

item1=input("What item do you want to buy? ")
quantity1=int(input(f"How many {item1} you want? "))
price1=float(input(f"Whats the Price for {item1}"))


item2=input("What item do you want to buy? ")
quantity2=int(input(f"How many {item2} you want? "))
price2=float(input(f"Whats the Price for {item2}"))


# item3=input("What item do you want to buy? ")
# quantity=int(input(f"How many {item3} you want? "))
# price3=float(input(f"Whats the Price for {item3}"))

total_Price=(quantity1 * price1) + (quantity2 * price2) 
print(total_Price)