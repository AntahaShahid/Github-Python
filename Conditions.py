#if statement: If the condition becomes true it will print otherwise else statement will execute.

#can also add multiple conditions by using elif property(feature/built-in funtion)
# age=int(input("Enter age: "))

# if age>=17:
#     print("Capable of making decisions")
# elif age<=0:
#     print("You havent born yet! Hahahhaha")
# elif age>=200:
#     print("WOw What an age limit you have reached!!!") #Here still the if condition becomes true
#                                                        #So it is printing out.
#                                                        #For this we will have to rethink on 
#                                                        #order and priority of else if..
# else:
#     print("You must take suggestions")
    
    # comment out the first code and new code with changed order:
    
age=int(input("Enter age: "))

if age>=200:
    print("WOw What an age limit you have reached!!!")
elif age>=17:
    print("Capable of making decisions")
elif age<=0:
    print("You havent born yet! Hahahhaha")
else:
    print("You must take suggestions")