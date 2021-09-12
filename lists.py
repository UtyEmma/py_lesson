# A List is an array actually! It is a collection which is ordered and changeable and allow duplicate members

# numbers = [1, 2, 3, 4, 5]
# items = list((1, 2, 3, 4, 5)) # I do not like this method
# print(numbers, items)

fruits = ['apple', 'banana', 'pineapple', 'pears']

# print(fruits[1])
# print(len(fruits))
# fruits.append('mango')
# fruits.remove('apple')
# fruits.insert(2, "strawberry")
fruits.pop(2)
fruits.reverse()
fruits.sort()
fruits.sort(reverse=True)
fruits[0] = 'oranges'
print(fruits)

