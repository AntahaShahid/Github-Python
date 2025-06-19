# String to Boolean:

# a="False"
# b=bool(a) # Converts every non-empty string to True.
# print(b)

# so by leaving the string empty, it will give us false
# a=""
# b=bool(a) # Converts every non-empty string to True.
# print(b)
####### NOte note note : We can use this function in projects that is someone has entered there name or not
### or the specfic questions which they are asked to..
# among strings and int

# age=22
# age=str(age)
# print(age+"1") #--> here in this case dont change the name of variable.


###--------Errors--------###
# From string to int:

# 1.Value Error:
# string="hello"
# int=int(string)
# print(int)

# int_value="hello"
# convert=int(int_value)
# print(convert)   #### note note note --> String to int me sirf tab masla krti jab string me koi
                ## number na ho "33" like agar aese ho to koi masla nai krti..

#2. Value/precision loss from float to int:

# float=23.333
# int=int(float)
# print(int)
#Printing the Data type:
# bool=True
# name="ANtaha"
# age=25.333
# print(type(age))

#Task 1:
# user_input=input("Enter a number: ")

# converted=int(user_input)

# print(f"Your given number is {converted+converted}")

# Task 2:

# float=22.398
# print(float)

# convert_to_int=int(float)
# print(convert_to_int)

# Task 3:

# users_input=int(input("Enter a Number: "))

# print(bool(users_input))

# Task 4:

empty=""
print(bool(empty))