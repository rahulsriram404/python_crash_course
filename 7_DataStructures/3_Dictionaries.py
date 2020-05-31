# 7D) DICTIONARIES : UnOrdered(but indexed), Mutable, Duplicates-Not-Allowed(Overrides to latest)

# Python dictionaries are Key-Value Pairs, more like Maps in other languages

# Values can be integers, floats, complex, strings, lists, tuples, sets, dictionaries, functions(lambdas), classes and objects too.

# Utility lists to be used
hobbies = ['coding', 'binge-watch', 'talking to myself']
fav_food = ['ice-creams', 'omelettes', 'coke', 'pizza']

my_dict = {
    'first_name': 'Rahul',
    'last_name': 'SriRam',
    'age': 19,
    'age': 20,
    'fav_food': fav_food
}

print(my_dict)
print(len(my_dict))
print(type(my_dict))

# 7A1) How is it UnOrdered?
# Cz elements can't be accessed by numeric-indices, but can be accessed by keys by :

# - Using [] operator :
print(my_dict['first_name']) # 'Rahul'

# - Using get() method :
print(my_dict.get('first_name')) # 'Rahul'

# 7A2) How is it mutable?

# a) Cz Assigning a value to a key is possible :
my_dict['first_name'] = 'TSC' # if key is already present, it is asigning
print(my_dict)

# b) Cz Adding pairs is possible :
my_dict['is_male'] = True # if key isn't already present, it isn't assigning, but adding new pairs
print(my_dict)

# c) Cz Removing pairs is possible : pop(), popitem(), clear() methods

# - Use pop() method to remove by key :
my_dict.pop('is_male')
print(my_dict)

# - Use popitem() method to remove the latest entry :
returned_tuple = my_dict.popitem() # cz it returns a tuple
print(returned_tuple)

# - Use clear() method to empty the whole dictionary :
my_dict.clear()
print(my_dict) # {}

# d) Cz dictionary itself can be pointed to a new dictionary :
my_dict = {
    'name': 'Rahul SriRam',
    'gender': 'Male',
    'hobbies': hobbies
}
print(my_dict)

# NOTE:

# 1) 'del' keyword can be used to :

# - To remove a pair with a specific key :
del my_dict['gender']
print(my_dict)

# - To erase the dictionary from memory itself :
del my_dict
# print(my_dict) # ERROR!

# 2) Accessing keys, values and pairs of a dictionary :

# - For keys, we use the keys() method : List-like entity of keys
my_keys = my_dict.keys()
print(my_keys)

# - For values, we use the values() method : List-like entity of values
print(my_dict.values())

# - For pairs, we use items() method : List-like entity of Tuples of pairs
print(my_dict.items())

'''
3) The following will be discussed in the coming videos :
- Copying dictionaries, copy(), Deep VS Shallow Copying and References.
- update(), setdefault() and fromkeys() methods.
- Dictionary Comprehensions.
- Zipping, UnZipping, Packing, UnPacking, and the splat(**) operator.
- enumerate() function.
'''
