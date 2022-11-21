import random
import string
#Welcome Banner
print()
print()
print('***************************************')
print('***************************************')
print('********Password Generator 2k22********')
print('***************************************')
print('***************************************')
print()
print()

#set variables
letters = string.ascii_letters

# whole numbers
numbers = string.digits

#special characters
special_characters = string.punctuation

#All options
all_options = letters + numbers + special_characters
#print(all_options) *test all options variable

password = list()
#password = []

#password generator loop
while len(password) < 10:
   
    #add random character to list
    password.append(random.choice(all_options))
    
    #convert characters from list to a string
    new_password = ''.join(password) 

#print(ans)
print(f'Your password is: {new_password}')


