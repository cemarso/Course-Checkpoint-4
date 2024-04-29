
# M2C4 Python Assignment - Python exercises


# Exercise 1: Create a list, tuple, float, integer, decimal, and dictionary.

my_list = ['fruit', 'milk', 'rice']
print(my_list)

my_tuple = ('fruit', 'milk', 'rice')
print(my_tuple)

my_float = 2.55
print(my_float)

my_integer = 25
print(my_integer)

from decimal import Decimal
my_decimal = Decimal(2.55)
print(my_decimal)


# Exercise 2: Round your float up.

import math
my_float = 2.55
print(math.ceil(my_float))


# Exercise 3: Get the square root of your float.

import math
my_float = 2.55
print(math.sqrt(my_float))


# Exercise 4: Select the first element from your dictionary.

my_dictionary = {
    'BIO': 'Bilbao',
    'BCN': 'Barcelona',
    'MAD': 'Madrid'
}
my_first_element = my_dictionary['BIO']
print(my_first_element)


# Exercise 5: Select the second element from your tuple.

my_tuple = ('fruit', 'milk', 'rice')
print(my_tuple[1])


# Exercise 6: Add an element to the end of your list.

my_list = ['fruit', 'milk', 'rice']
my_list.append('butter')
print(my_list)


# Exercise 7: Replace the first element in your list.

my_list = ['fruit', 'milk', 'rice']
my_list.remove('fruit')
my_list.insert(0, 'vegetables')
print(my_list)


# Exercise 8: Sort your list alphabetically.

my_list = ['milk', 'rice', 'fruit']
my_sorted_list = sorted(my_list)
print(my_sorted_list)


# Exercise 9: Use reassignment to add an element to your tuple.

my_tuple = ('fruit', 'milk', 'rice')
my_tuple += ('butter',)
print(my_tuple)


