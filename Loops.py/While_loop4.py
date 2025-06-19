# Another example just to show use of logical operators in while loop..

# number=int(input("Enter number:"))

# while number < 0 or number > 10:
#     print(f"{number} is an invalid for given condition")
#     number=int(input("Enter number:"))
# print(f"You typed number is: {number}")

    #ALERT ALERT ALERT :,,, REMEMBER THAT SECOND CONDITION SIRF TAB EXECUTE HO GI JAB WHILE SE 
    # GUZRI HO GI EK MARTABA..
    ## Another thing which in revision I observed is while just executes or condition exact in a way,
    ## It doesnot execute the and condition truly..
    
## Self-Created Challenge:  

Name=input("Enter Your Name: ")

while len(Name)>10 or " " in Name or any(char.isdigit() for char in Name):
    print("Your Name Length Exceeded")
    Name=input("Enter Your Name Again: ")
    
print(f"Wellcome to the Community {Name.capitalize()}!")
