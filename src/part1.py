# # print hello world
# print('Hello, World!')

# # declare a variable
# name = 'Candace'

# # print a variable
# print(name)

# # String concatenation
# print('Hello ' + name)
# # `Hello ${name}`
# print(f'Hello {name}')


# # Data structures

# # Lists (not arrays)
# p = [10, 60, 20, 5, "banana"]
# print(p)
# # add an element to the end of p
# p.append(77)
# print(p)

# # Loop over the list P, and print every element
# # for every element in p, do some sort of code

# for element in p:
#     print(element)

# # lets print the index and element at the index of p
# # p = [10, 60, 20, 5, "banana"]
# # enumerate(p)=> [(0, 10), (1, 60), (2, 20), ...]
# for (index, element) in enumerate(p):
#     print(f'Element at {index} is {p[index]}')


# # List comprehensions
# # another way to create a list
# numbers = [1, 4, 9, 16, 25]
# # create a new list, of squares from the numbers list
# squares = []
# for num in numbers:
#     squares.append(num*num)
# print(squares)

# # lets use list comprehensions
# # for each element from numbers, multiply by itself, and add to cooler_squares
# # [ function(variable) for variable in some_list]
# cooler_squares = [num*num for num in numbers]
# print(cooler_squares)

# # create a list of just even numbers
# evens = [num for num in numbers if num % 2 == 0]
# print(evens)

# names = ['Sarah', 'jorge', 'sam', 'frank', 'bob', 'sandy', 'shawn']
# # create a new list containing only names that start with s
# # All names should be capitalized
# s_names = [name.capitalize() for name in names if name[0].lower() == 's']
# print(s_names)

# Dictionaries
# otherwise known as maps/hashmap/objects
# a key -> value data structure
new_dict = {}

# create a dictionary with some keys and values
food_dict = {
    'apple': 'is a fruit',
    'carrot': 'is a vegetable'
}
print(food_dict)

# add a new key value pair
food_dict['cucumber'] = 'is maybe a vegetable?'
print(food_dict)

# access a print a specific element in food_dict
chosen_food = 'apple'
print(food_dict[chosen_food])

# iterate through the keys and values of a dictionary
# for element in dict, do some code
for key, value in food_dict.items():
    print(f'{key} : {value}')

# how can we check if an element exists in a dictionary?
# is apple in food_dict?
print('apple' in food_dict)
print('banana' in food_dict)

# Tuple and sets
# Tuples are collection of a couple of elements

tup = (1, 2, 3, 4)
for item in tup:
    print(item)

# access a particular element
print(tup[1])

# you cannot modify tup in any way
# tup[1] = 'new_thing'

# set are basically dictionaries without values
fruit = {'cucumber', 'apple', 'banana'}

for item in fruit:
    print(item)

if 'cucumber' in fruit:
    print('I dont think cucumber is a fruit')
