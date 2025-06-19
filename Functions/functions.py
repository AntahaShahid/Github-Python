# Functions: A block of reusable code, place () after the function name to envoke it.
print()
#This print is just for adding Space--Great Idea

# def happybirthday(): 
#   print("Happy Birthday to You")
#   print("You are years old")
  
# happybirthday()
# happybirthday()

#Passing an argument
# def happybirthday(name, age): 
#    print(f"Happy Birthday to You {name}")
#    print(f"You are years old {age}")
  
# happybirthday("Antaha", "19")
# happybirthday("Sanan", 25)

# def display_invoice(username,adress,email):
#     print(f"Hello {username}, Your Home Adress is {adress}. And your email adress is {email}.")


# display_invoice("Antaha Shaihid","Diyal Road","antahashahid@gmail.com")
# print()

#return: statement used to end a function and send a result back to the caller.

def add(x,y):
   z = x+y
   return z

def add(x,y):
   z = x+y
   return z

def subtract(x,y):
   z = x-y
   return z

def multiply(x,y):
   z = x*y
   return z

def divide(x,y):
   z = x/y
   return z

print(add(2,3))
print(subtract(2,3))
print(multiply(2,3))
print(divide(2,3))


def createname(first,last):
    first=first.capitalize()
    last=last.capitalize()
    # return first,last --->comma se different print hota
    return first+" "+last

fullname=createname("antaha","shahid")
completename=createname("sanan","mehmood")
sh=createname("soban", "haider")

print(fullname)
print(completename)
print(sh)
    

