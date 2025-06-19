#Lets create the temperature converter:

# Fahrenhiet to celcius:
    # Formula:  C=(F-32)*5/9
    
temp=float(input("Enter temperature: "))    
unit=input("Is the unit is in Fahrenhiet or Celcius(F or C): ")
if unit=="F":
    temp=round((temp-32)*5/9 ,2)
    print(f"Your temperature in Celcius is : {temp}")
    
# Celcius to Fahrenhiet:
    # Formula: F=(C*9/5)+32   

elif unit=="C":

    # temp=(round(temp*9/5+ 32 ,2))
    temp=round((9* temp)/5 + 32 , 1)
    print(f"Your temperature in Fahrenhiet is : {temp}")
    
    
    
