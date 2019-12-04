# Magic number game ## Project see definition of done

# promt the user for input
# generate a random number using a python library (should be between 1-10)
import random
randomNumber = random.randint(1, 10)
# check the the number against a magic number
# let the user know if he/she won or
    # if the guess was above or under

num = int
while num != randomNumber:
    num = int(input("Enter your number"))
    if num == randomNumber:
        print("You won!")
    elif num > randomNumber:
        print("Your number", num, "is higher")
    else:
        print("Your number", num, "is lower")



# Make it so you keep playing until we say: 'No more Magic'