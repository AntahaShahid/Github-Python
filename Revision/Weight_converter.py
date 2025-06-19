weight=float(input("Enter Your Weight: "))
unit=input("Is it in Kgs or Lbs ( K or L ): ").upper()
if unit=="K":
    new_weight=weight*2.205
    unit="lbs."
    print(f"Your Weight in Lbs is {round(new_weight,2)} {unit} ")
elif unit=="L":
    new_weight=weight/2.205
    unit="Kgs."
    print(f"Your Weight in Kgs is {round(new_weight,2)} {unit}")