#Keyword_Arguments: name-value pair passed to function as arguments

print()

def pet_description(animal_type,animal_name):
    print(f"I have a {animal_type.title()}")
    print(f"My {animal_type.title()} name is {animal_name.title()} ")
    
pet_description(animal_name="horse",animal_type="mammal") 

#ORDER DOESNOT MATTER
