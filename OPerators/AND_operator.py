temp=float(input("Enter Current temperature: "))

Will=input("You wanna go outside:(Yes or No): ")
if temp==40 and Will=="Yes":
     print("Its Hot Outside")
     print("Wanna roast so go outside")
elif temp<=0 and temp>=-20 and Will=="Yes":
    print("Its too Cold outside")
elif temp>=10 and temp<=30 and  Will=="Yes":
    print("Here the temperature is friendly, so lets hangout")
    
    # We can also write condition in the folowing way:
    
elif 50 < temp > 100 and Will=="Yes":
    print("You want to rost")
     