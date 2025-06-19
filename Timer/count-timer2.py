import time

count_time=int(input("Enter time in seconds:"))

for x in range(0, count_time):
    # time.sleep(1) #Beautiful thing learned here is when remove that line time.sleep(1) then for
                    # prints our message the second time we gave input of.It also happens when place
                    # of print is not correct.
    time.sleep(3)
print("Happy BirthDay")
    
    
    