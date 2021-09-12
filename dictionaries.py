# Dictionaries is a collection which is unordered, changeable and indexed and has no duplicate members

person = {
    'firstname' : 'John',
    'lastname' : 'Maxwell',
    'age' : 50,
    'gender' : 'male'
}

# You can use constructor
# person = dict(firstname="Johnson", lastname="May")

# print(person, type(person))

# print(person['firstname'])
# print(person.get('lastname'))
person['phone'] = '08025291607' 

# print(person)
# print(person.keys())
# print(person.items())

# utibe = person.copy() #Copy An Item
# utibe['city'] = 'Uyo'

# print(utibe)

# del(person['age'])
# person.pop('phone')
# person.clear()

# print(len(person))


# We can have a List of DIctionaries
people = [
    {'name': "Utibe", 'age' : '75' },
    {'name': "Samson", 'age' : '5' }
]

print(people[1]['age'])