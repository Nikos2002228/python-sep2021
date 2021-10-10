# Exercise 12 - Python - September 2021

# Input
while (True):
    try:
        file_path = str(input("Enter the path: "))
        file_in  = open(file_path, 'r')
    except (FileNotFoundError, NotADirectoryError):
        print("File not found, try again")
    else:
        break

# Lists of all the characters and digits
char_oth = ['!','@','#','$','%','&','(',')',
            '_','{','}','[',']','|',';',':',
            ',','?','<','>','~','`',' ']

char_dig = ['1', '2', '3', '4', '5',
            '6', '7', '8', '9', '0']

char_op  = ['+', '-', '*', '/', '=', '^', '.']

chars    = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
            'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
            's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# Print the file in rows of 16 characters
for line in file_in:
    word = ''
    num = ''
    i = 0
    j = 0
    passed = 0
    list = list(line)
    while (j < len(list)):
        
        number = False
        char = list[j]
        
        if (char in char_oth):
            if (not(num != '' and number == False)):
                word += '?'
            else:
                passed += 1                
        elif (char in char_op):
            if (not(num != '' and number == False)):
                word += ' '
            else:
               passed += 1              
        elif (char in chars):
            if (not(num != '' and number == False)):
                word += 'A'
            else:
                passed += 1
                passed -= 2
        elif (char in char_dig):
            number = True

        if (number): 
            num += char
        else:
            if (num != ''):      
                if (int(num) < 128):
                    word += 'p'
                elif (int(num) >= 128):
                    word += '1'
                num = ''
                i -= 1 * passed
                j -= 1 * passed
        j += 1 
        i += 1

        if (i == 16):
            print(word)
            word = ''
            i = 0
    print(word)  
    
# Close the files
file_in.close()