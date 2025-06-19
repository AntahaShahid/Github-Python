# Nested Loop: A loop with in an another Loop.
            #Outer Loop
                        #Inner Loop
                        

# for x in range(1,8):
#     print(x)
    
    #If we want all of them to be on the same line:
    
# for x in range(1,8):
#     print(x, end=" ")
    
    # if we make this a nested loop:
    # we will print this series multiple times
    
for a in range(2):
    for x in range(1,8):
        print(x, end=" ")
    print()
    
    # once again the position of print statement tricked.