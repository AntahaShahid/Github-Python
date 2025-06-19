#Whiel Loop: Executes code until the condition remains true:

user_name=input("Enter Your Name: ")

while user_name == "":
    print("You did not enter Name")
    user_name=input("Enter Your Name: ")
print(f"wellcome {user_name}")
    
    #ERROR SOLUTION:
    #AGAR KABHI CODE BAWJOOD IS K K OK HO AUR NA DY RAHA HO DESIRED RESULT. LIKE KOI ERROR BHI SHOW
    #NA KARE AUR RUN BHI HO JAYE BUT DESIRED OUTPUT NA HO TO EK MARATBA DELETE KRNA CHAHYIHH 
    #TERMINAL KO.. I HAVE SPENT ALMOST 15 MINS ON THIS
    
#ON revising what i did is removed the second username statemnet ,and the code for name written is running
# smoothly, but the problem raises when i did empty that is the while condition so there the infinite loops run