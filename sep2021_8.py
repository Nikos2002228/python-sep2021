# Exercise 8 - Python - September 2021 

# Input
key = int(input("Enter the key: "))

# All English characters from A-Z
characters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I',
              'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
              'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

# Characters to remove from file
characters2 = '1234567890!@#$%^&*()-=_+{}[]|;:.,?/<>~`'

# Open the file
while (True):
    try:
        file_path = str(input("Enter file path: "))
        file_in  = open(file_path, 'r')
    except (FileNotFoundError, NotADirectoryError):
        print("File not found, try again")
    else:
        break

file_out = open('data_out_8.txt', 'w')

# For each line remove every character from characters2
for line in file_in:
    for char in characters2:
        if (char in line):
            line = line.replace(char, '') 
            print(line)
            
    file_out.write(line)

### Remove data from 'data_out.txt' and copy them to 'data.txt'
file_in.close()
file_in = open(file_path, 'w')

file_out.close()
file_out = open('data_out_8.txt', 'r')

for line in file_out:
    file_in.write(line)

file_out.close()
file_out = open('data_out_8.txt', 'w')
### ### ### 

# Re-open the modified text file
file_in.close()
file_in = open(file_path, 'r')

# For each line... 
for line in file_in:
    # And for each word
    for word in line.split():
        # Create an empty string
        new_word = ''
        
        # For each character in the list word
        for char in list(word):
            i = 0
            
            # Find the location in the characters list
            for char2 in characters:          
                if (char is char2):
                    location = i
                    break
                else:
                    i += 1

            if (key + i > 25):
                i = key + i - 26                   
            else:
                i+=key

            char = characters[i]
            # Add the new char to the string that will replace the word
            new_word += char
            
        print(new_word[::-1])
        
        # Write the changes
        # Reverse the string
        file_out.write(new_word[::-1])
        file_out.write(' ')

# Close the file_out
file_in.close()
file_out.close()