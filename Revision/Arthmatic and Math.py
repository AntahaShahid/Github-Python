# # Challenge 1:
# import math

# diameter=float(input("Enter the diameter of a Circle: "))
# #Part 1: Finding Circumfernce:
# circumfernce= math.pi*diameter
# print(f"circumfernce of a circle is {circumfernce}")
# #Part 2: Finding Area using diameter:
# Area=math.pi*(diameter/2)**2
# print(f"Area= {Area}")

# Challenge 2:
# a=float(input("Enter the Value for a:"))
# b=float(input("Enter the Value for b:"))

# # Finding Hypotenuous:

# Hypotenuous= math.hypot(a,b)
# print(f"Hypotenuous: {Hypotenuous}")

# Challenge #3:
# tangent=float(input("Enter the value for tangent: ")) 

# radians=math.atan(tangent)
# degrees=math.degrees(radians) 
# print(radians)
# print(degrees)

#Challenge 4:

# number_1=float(input("Enter the first number: "))

# operator=input("Enter the operator: ")
# number_2=float(input("Enter the second number: "))

# result= =*operator

# print(result)

# Simple Calculator using Dictionary and Augmented Operators

# number_1 = float(input("Enter the first number: "))
# operator = input("Enter the operator (+, -, *, /): ")
# number_2 = float(input("Enter the second number: "))

# Dictionary storing operator functions
# operations = {
#     "+": lambda x, y: x + y,
#     "-": lambda x, y: x - y,
#     "*": lambda x, y: x * y,
#     "/": lambda x, y: x / y if y != 0 else "Error! Division by zero."
# }

# # Perform calculation
# result = operations.get(operator, lambda x, y: "Invalid operator!")(number_1, number_2)

# print(f"Result: {result}")

# Simple Augmentation: 

# Important thing here which i forgot is we will write the augmented operator with the variable itself(first operator)..


num1=int(input("Enter number 1: "))
b=int(input("Enter number 2: "))
num1+=b
print(num1)