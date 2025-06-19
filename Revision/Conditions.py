# Challenge 1:

# a=int(input("Enter a:"))
# b=int(input("Enter b: "))
# if a>b:
#     print("First number is greater")
# elif a<b:
#     print("Second number is greater")
# else:
#     print("Both numbers are Equal")
# Challenge 2:
# grades=int(input("Rank your grades between 0-100: "))

# if grades>89 and grades<101:
#     print("Grade A")
# elif grades>79 and grades<90:
#     print("Grade B")
# elif grades>69 and grades<80:
#     print("Grade C")
# elif grades >59 and grades <70:
#     print("Grade D")
# elif grades <60:
#     print("Grade F")
# else:
#     print("Ghuraba")
    
    
    # elif grades >59 and grades <61:

    # First I did here 90 and 100, 80 and 89, 70 and 79, So the exact words like 80,89,90,99 comes into else statement, then i gave the gap of two
    
    #Challenge 3:
   
# Year=int(input("Enter the Year: "))
# if Year%4==0:
#     print(f"{Year} is a Leap Year")
# else:
#     print("Not a Leap Year")
        
# Challenge 4:

# age=int(input("Enter Your age: "))  
# if age>0 and age<=12:  # IN this eg I observed that we can write <= this format to avoid abruptions13
#     print("Child")
# elif age>=13 and age<=19:
#     print("Teenager")
# elif age>=20 and age<=59:
#     print("Adult")
# elif age>=60:
#     print("Senior")    
# else:
#     print("Please Write Correct age")

    
#     Ask the user for a username and password.
# If the username is "admin" and password is "1234", print "Login successful".
# Otherwise, print "Access Denied"

# Challenge 5:

# user_name=input("Enter Your Name: ")
# password=int(input("Enter Password Please: "))

# if user_name == "admin" and password == 1234:
#     print("LOG in SuccessFull")
# else:
#     print("Access Denied")

# Challenge 6: Boolean

# mature=False

# if not mature:
#     print("Great")
# else: 
#     print("Try your best")

# Challenge 7: Ternary

success=int(input("Rank Your Success Level: "))
print("Good Job") if success>9 else print("At least Believe in Your-Self")