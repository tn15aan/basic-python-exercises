# Define the following variables

#name, last_name, age, eye_color, hair_color
name = 'Jon'
last_name = 'Doe'
eye_color = 'Brown'
hair_color = 'Black'
age = '23'

# Prompt user for input and Re-assign these
# name = input('Enter the first name')
# last_name = input('Enter the last name')
# eye_color = input('Enter eye color')
# hair_color = input('Enter a hair color')
# age = input('Enter the age')

# Print them back to the user as conversation
# Example: 'Hello Jack! Welcome, your age is 26, your eyes are green and your hair color is black.
print('Hello', name ,'!', 'Welcome, your age is', age, ', your eyes are', eye_color,
      'and your hair color is', hair_color)


#Section 2 - Calculate in what year was the person born? and responde back.
# print something like: 'You said you we're 28 hence you were born in 1991!'
calculatedYear = 2019 - int(age)
print('You said you were', age, 'hence you were born in', calculatedYear, '!')

#Extra - Cast your input
#