print()

# def pet_description(animal_type="mammal",animal_name): it gives error,positonal arguments #
# should be written first while using default
# def pet_description(animal_name,animal_type="mammal"):
#     print(f"I have a {animal_type.title()}")
#     print(f"My {animal_type.title()} name is {animal_name.title()} ")
    
# pet_description("horse") #this also prints right output

# pet_description(animal_name="horse") #we can write it in keyword argument


# print()

# def pet_description(animal_specie,animal_name,animal_type="mammal"):
#     #we have to follow order in this case cz it would print funny mix
#     print(f"I have a {animal_type.title()}")
#     print(f"My {animal_type.title()} name is {animal_name.title()} and specie is {animal_specie} ")
    
# pet_description("horse","Google") 

# print()

# def pet_description(animal_specie,animal_name,animal_type="mammal"):
#     #we dont have to follow order in this case cz now its in it keyword
#     print(f"I have a {animal_type.title()}")
#     print(f"My {animal_type.title()} name is {animal_name.title()} and specie is {animal_specie} ")
    
# # pet_description(animal_name="horse",animal_specie="Google") 
# #this keywords can also be written in any order
# pet_description(animal_specie="Google",animal_name="horse") 

print()
def makeshirt(size):
    print(f"Hello I wear a T-shirt of size {size}")
makeshirt("22cm")   
makeshirt(size="25cm") 
