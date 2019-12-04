# Magic number game!
# I want you to use operators
# equate something

# As a user, I want to be able to guess a number and know if i got it correct or not, so that I can know if I won or not.

import random
# We should define/assign number to a variable called magic_number
magic_number = random.randint(1, 10)

# I need to ask user for input
#num = int(input("Please enter a number"))

# I need to check if this input matches a magic_number

num = int
# I need to let the user know if the response was write or not
while num != magic_number:
    num = int(input("Please input a number between 1 and 10: "))
    if num == magic_number:
        print('OMG you won congratulations')
    elif num > magic_number:
        print('Your number', num, 'is higher')
    else:
        print('Your number is lower')
#self five