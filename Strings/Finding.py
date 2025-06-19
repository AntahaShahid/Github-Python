#Simple:
# input=input("Enter a string: ")
# find=input.find("d")
# print(find)

# The above one is simple but what if same alphabet comes twice:

# we will use r(for reverse) this will return the index of last that same alphabet:

# reverse=input("Enter a string: ")
# find=reverse.rfind("a")
# print(find)  #Dont get confused it starts counting with start.

#If it dont find the desired result:

input=input("Enter a string: ")
find=input.find("d")
print(find)  # It will return -1