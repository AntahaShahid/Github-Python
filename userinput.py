#input: A function that prompts the user to enter data and it returns the entered data as a string

# input("Whats Your Goal?") #this is only printing and not returning we will assign a variable to

# main_step=input("How will you lose weight?")

# print(f"BY taking a {main_step}")

# name=input("whats your name: ")
# print(f"I am {name}")

# age=input("How old are you: ")
# print(f"I am {name}")
                      # datatype we dont write the name of them and no need to tell the compiler
                      # in this age case we have write 19 years old where 19 is integer and yearold 
                      #is a string.
 # we can also write them together printing way like:
# name=input("whats your name: ")
# age=input("How old are you: ")
# print(f"I am {name}")
# age=int(age)
# age=age+1
# print(f"I am {age}")  #so here as we talk about datatypes, when its about printing, they are printing
                      # but as we do age+1 here the problem came of type error cz remember that whenever
                      # what the input function retuns its all in a string format.so in that case we
                      # we have to write int that is to give a datatype name whichever we are using.
                      # Also we can do this outside of the input example
age=int(input("How old are you: "))
age=age+2
print(f"I am {age} years old")                     

                     