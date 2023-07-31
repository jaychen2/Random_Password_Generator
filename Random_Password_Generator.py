#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

number_of_time = int(input("How many passwords?\n")) 
nr_letters = int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

complete_pass = []

for x in range(number_of_time):
    while nr_letters > 0 or nr_symbols > 0 or nr_numbers>0:
        randomizer = (random.randint(0,2))

        if randomizer == 0 and nr_letters > 0:
            random_letter = random.randint(0,25)
            randomizer_case = (random.randint(0,1))
            if randomizer_case == 0:
                complete_pass.append(letters[random_letter])
                nr_letters -= 1
            elif randomizer_case == 1:
                complete_pass.append(letters[random_letter].upper())
                nr_letters -= 1  
                
        elif randomizer == 1 and nr_symbols > 0: 
            random_symbols = random.randint(0,8)
            complete_pass.append(symbols[random_symbols])
            nr_symbols -= 1
            
            
        elif randomizer == 2 and nr_numbers > 0: 
            random_number = random.randint(0,9)
            complete_pass.append(numbers[random_number])
            nr_numbers -= 1

    random.shuffle(complete_pass)

    random_string = ""

    for string in complete_pass:
        random_string += string

    print(random_string)


    

    


    