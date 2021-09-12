#Tuples in Python - A Tuple is a collection which is ordered and Unchangeable

fruits = ('Apples', 'Oranges', 'Grapes')
# group = tuple(('Mangoes'))

# Single Value requires a trailing coma
fruit = ('Grape',)

# print(fruits, type(fruit))
print(fruits[1])

# del fruits
# print(fruits)


# Sets in Python - A Set is a collection which is unordered and unindexed and cannot have duplicate members

cars = {'Volvo', 'BMW', 'Audi', 'Toyota'}
# print('Mercedes' in cars) # To check for an item in a set

cars.add('Mercedes')
cars.remove('Audi')

print(cars)
cars.clear()

print(cars)

