#Shapes by Nested loops:
#Rectangle: 
rows=int(input("Enter rows #: "))
columns=int(input("Enter columns #: "))
symbol=input("Which Symbol to use: ")

for x in range(rows):
    for y in range(columns):
        print(symbol,end="")
    print()
    
    #mistake/learn i made:
    # for rows in range(4)
    # for columns in range(5)
