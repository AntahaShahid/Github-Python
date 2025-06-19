# Compound Interest: accruing,, search more..
#APR
#Formula: A=P(1+r/n)t

principle=0
rate=0
time=0

while True:
    principle=float(input("Enter the principal amount: "))
    if principle < 0:
        print("Principal cant be less than zero")
    else:
        break
while True:
    rate=float(input("Enter the rate amount: "))
    if rate< 0:
        print("rate cant be less than zero")
    else:
        break
while True:
    time=int(input("Enter the time in years: "))
    if time < 0:
         print("Time cant be less than zero")
    else:
         break
    
# else: # else k beghair it was not printing the desired output but Bro Code was doing smoothly
total=principle*pow((1 + rate/100),time)
print(f"Balance after {time} years will be {total:.2f}")

# True wali bat ki samjh ni ayi zeda but kr liya..
# true wali itni ayi k forever chalane k liye and isko explicitly break kiya gaya..
        
