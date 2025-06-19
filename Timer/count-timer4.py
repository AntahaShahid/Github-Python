# in this example we have printed count-time with seconds
# import time
# reverse=int(input("Time in seonds:"))

# for x in (range(reverse,1-1,-1)):
#     # seconds =x%60
#     print(f"00:00:{x:02}")
    
#     time.sleep(1)
# print("ALLAH")

#seconds are also printing with x without seconds variable dont know whats the function of x%60 then

import time
reverse=int(input("Time in seonds:"))

for x in (range(reverse,1-1,-1)):
    seconds =x%60
    minutes=int(x/60)%60
    hours=int(x/3600)
    print(f"{hours}:{minutes}:{seconds:02}")
    
    time.sleep(1)
print("ALLAH")

#Here it worked beautifully,, like a digital clock..!!