#p=Principal
#r=Rate
#t=Time

p=0
r=0
t=0

while True:
    p=float(input("Enter the Principal Amount: "))
    if p<=0:
        print("Pricipal cant be less than zero")
    else:
        break

while True:
    r=float(input("Enter the rate Amount: "))
    if r<=0:
        print("Rate cant be less than zero")
    else:
        break
while True:
    
    t=int(input("Enter the time: "))
    if t<=0:
        print("Time cant be less than zero")
    else:
        break    
    
comp_interest=p*pow((1+r/100),t)

print(f"Your amount after {t} years wil be {comp_interest:.2f}")