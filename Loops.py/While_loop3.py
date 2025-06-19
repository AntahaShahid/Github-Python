# Example by using a not operator to avoid the while conditon: its hard to convey my concept in 
# words but its the most useful concept i heard of:

food=input("Enter the food You Like: ")
while not food=="q":
    print(f"ohh You like {food} its great!!")
    # food=input("Enter the another food You Like: \nIf You want to Quit Please enter q: ")
    # Agar is trah se dusra food likhte hain to wo quit wale option pe a jata..
    # OHH ye just two times hi food puch raha us k baad quiting k us pe a jata..
    food=input("Enter the another food You Like: ")

    quit= input("Are You Sure to Quit: ").upper()
    
    if quit=="YES":
        print("Okay, Thanks for visiting")
    else:
        print("Go back to the menu")

# OHH ITS GREAT I HAVE CODE THE QUIT CONDITION ON MY OWN,
# THE VERY INTERSTING THING WHICH I HAVE LEARN THERE IS UNLIKE IS ELSE OR ELIF IF WE WANT TO PRINT
# ANOTHER CONDITION IT WONT BE PRINTED UNLESS WE GO BY THE FIRST (THAT WHILE CONDITION).
# WE HAVE TO GO THROGH BY THE WHILE CONDITION IF WE WANT TO PRINT OUR SECOND CONDTION(other than while) 