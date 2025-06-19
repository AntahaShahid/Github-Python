temp=float(input("Enter the temperature: "))
unit=input("In Fahrenhiet or Celcius( F or C ): ").upper()

if unit=="C":
    new_temp=round((9*temp)/5+32,2)
    print(f"Temperature in Fahrenhiet is {new_temp}")
elif unit=="F":
    new_temp=round((temp-32)*5/9,2)
    print(f"The Temperature in Celcius is {new_temp}")
else:
    print("Please write correct temperature")