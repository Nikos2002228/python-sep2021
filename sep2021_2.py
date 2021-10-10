# Exercise 2 - Python - September 2021

# Imports
import time, datetime

# Get current time in seconds (rounded)
curr_time_secs = round(time.time())

print("Current time in seconds: " + str(curr_time_secs))

# Check if the number can be divided by other numbers except by 1 and by it self...
i = 2
prime = True
while (i < curr_time_secs and prime):
    if (curr_time_secs % i == 0):
        print("This number can be divided by: ")
        print(i)
        prime = False
    i+=1

if (prime):
    safe = True
    p = curr_time_secs
    q = (p - 1) / 2 
    print("Next prime number: " + str(q))

    i = 1
    while (i < q and safe):
        i+=1
        if (q % i == 0):
            print("This number can be divided by: ")
            print(i)
            safe = False

    if (not(safe)):
        print("This is a prime number but not a safe one")
    else:
        print("This is a safe prime number")

else:
    print("This is not a prime number.")
