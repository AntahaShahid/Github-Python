import math

#lets calculate the circumference of a circle

radius= float(input("Enter the radius of a circle: "))

circumference=2*math.pi*radius
# print(circumference) # we can roundoff it to whatever digits we want
# print(round(circumference,3))
# print(math.ceil(circumference))
print(math.floor(circumference))