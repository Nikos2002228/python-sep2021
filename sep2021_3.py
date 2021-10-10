# Exercise 3 - Python - September 2021

# Input
number = int(input("Number: "))

# Add a counter
i = 0

# While the number is not 1...
while (number != 1):

    # Increase counter
    i += 1
    if (number % 2 == 0):
        number = number / 2
    else:
        number = number * 3 + 1

    print(int(number))

# Print the steps
print("Steps needed: ", i)
