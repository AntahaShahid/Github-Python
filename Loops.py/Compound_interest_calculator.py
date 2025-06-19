# Compound Interest: accruing,, search more..
#APR
#Formula: A=P(1+r/n)t

principle=0
rate=0
time=0

while principle <=0:
    principle=float(input("Enter the principal amount: "))
    if principle<=0:
        print("Principal cant be less than or equal to zero")
        
while rate <=0:
    rate=float(input("Enter the rate amount: "))
    if rate<=0:
        print("rate cant be less than or equal to zero")
        
while time <=0:
    time=int(input("Enter the time in years: "))
    if time<=0:
      print("Time cant be less than or equal to zero")
else: # else k beghair it was not printing the desired output but Bro Code was doing smoothly
        total=principle*pow((1 + rate/100),time)
        print(f"Balance after {time} years will be {total}")
        
#Another way of doing this code will be in comp_int2 file