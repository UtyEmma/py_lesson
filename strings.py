firstname = "Utibe-Abasi"
lastname = "Akpan"

# Concatenate
# print("Hello, my name is "+firstname+" "+lastname)

#String Formatting (Allows you to insert variables in strings)

# Using Positional Arguments
# print("My first name is {firstname} while my lastname is {lastname}".format(firstname=firstname, lastname=lastname))

# We can also use FStrings
# print(f'Hello, my name is {firstname} and I am {lastname}')

# STRING METHODS
s = "hello world"

# print(s.capitalize()) # Capitalize
# print(s.upper()) #UpperCase
# print(len(s)) # Get the length of the string
# print(s.replace('world', 'Everyone')) # Replaces
# print(s.count("w")) #count the number of times a string is provided
# print(s.split()) #explode the string into a list
print(s.find('r'))
print(s.isalnum())
