import math

# lets calculate the area of a circle: 
#Formula= A=pi*r**2

radius=float(input("Enter radius of a circle: "))
# Area=math.pi*radius**2
#we can also write it in a different method: 
Area=math.pi*pow(radius,2)

print(round(Area,2))