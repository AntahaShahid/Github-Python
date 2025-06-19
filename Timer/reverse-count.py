# import time
# reverse=int(input("Time in seonds:"))

# for x in reversed(range(0,reverse+1)):
#     print(x)
#     time.sleep(1)
# print("ALLAH")

# Can also be done in another way

import time
reverse=int(input("Time in seonds:"))

for x in (range(reverse,1-1,-1)):
    print(x)
    time.sleep(1)
print("ALLAH")