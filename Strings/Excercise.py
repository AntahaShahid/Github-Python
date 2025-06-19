#user input validation
#not name more than 12 characters
#name must not contain spaces
#name must not contain diigits

user=input("Enter Name: ")

# if (len(user>12)):  # I write in that way which is wrong
if len(user)>12:
    print("Your name exceeds by condition")
# elif user.find(" "):
elif not user.find(" ")==-1:
    print("Your name should not contain spaces")
elif not user.isalpha():
    print("Your name should not contain digits")
else:
    print(f"Wellcome {user}")

























