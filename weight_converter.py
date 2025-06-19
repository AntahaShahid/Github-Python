# Lets create the weight converter

# Three differnt ways of writing it
# First:

# weight=float(input("Enter your weight: "))
# unit=input("kilograms or pounds k or L: ")
# if unit=="K":
#     weight=weight*2.205
#     unit="Lbs."
#     print(f"Your weight in pounds is  {round(weight,2)} {unit}")
# elif unit =="L":
#     weight=weight/2.205
#     unit="kgs."
#     print(f"Your weight in kilograms is {round(weight,2)} {unit}")
    
# else:
#     print("incorrect ")
    
    
    #Second: 
    
    # Here we write print statement at last
# weight=float(input("Enter your weight: "))
# unit=input("kilograms or pounds k or L: ")
# if unit=="k":
#     weight=weight*2.205
#     unit="Lbs."
# elif unit =="l":
#     weight=weight/2.205
#     unit="kgs."
    
# else:
#     print("You entered an incorrect input")
# print(f"Your weight is {round(weight,2)} {unit}")

# Third: 
# The changes we made is that changed the variable under if and elif to new_weight...
# here i am also braining that in python can we use one variable at different variable places
weight=float(input("Enter your weight: "))
unit=input("kilograms or pounds k or L: ")
if unit=="K":
    new_weight=weight*2.205
    unit="Lbs."
    print(f"Your weight in pounds is  {round(new_weight,2)} {unit}")
elif unit =="L":
    new_weight=weight/2.205
    unit="kgs."
    print(f"Your weight in kilograms is {round(new_weight,2)} {unit}")
    
else:
    print("You have entered an incorrect statement")