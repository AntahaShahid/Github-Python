# user_name=input("Enter Your Name: ")
# password=int(input("Enter Password Please: "))

# if user_name == "admin" and password == 1234:
#     print("Access Granted")
# else:
#     print("Access Denied")

# Challenge 2:

# 👉 Ask the user for their age and membership status (yes/no).
# 👉 If the user is at least 60 years old or has a membership, print "You get a discount!"
# 👉 Otherwise, print "No discount available.

# age=int(input("Enter Your Age: "))
# member_ship=input("You Have Membership? Yes/NO: ").upper()

# if age>=60 or member_ship=="YES":
#     print("You get a discount")
# else:
#     print("No Discount available")
    
#     👉 Ask the user if it’s raining (yes or no).
# 👉 If it’s not raining, print "Go outside and enjoy!"
# 👉 Otherwise, print "Take an umbrella!

# raining=input("Is it raining outside? Yes or No: ").upper()
# if not (raining=="YES"):
#     print("Go Outside and enjoy")
# else:
#     print("Take an Umbrella")

temp=int(input("Enter the Temperature: "))
if 0<temp<25:  # we can write and operator like this..
    print("Best for Outdoor Event")
else:
    print("Event Will be Indoor")