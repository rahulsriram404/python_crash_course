# 7D) DICTIONARIES : UnOrdered(but indexed), Mutable, Duplicates-Not-Allowed(Overrides to latest)
# Key-Value Pairs, Maps
# Values can be integers, floats, complex, strings, lists, tuples, sets, dictionaries, functions(lambdas), classes and objects too.

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
# Cz elements can't be accessed by numeric-indices, but can be accessed by keys :
# - Using [] operator :

# - Using get() method :

# 7A2) How is it mutable?
# a) Cz Assigning a value to a key is possible :

# b) Cz Adding pairs is possible :

# c) Cz Removing pairs is possible : pop(), popitem(), clear() methods.
# - Use pop() method to remove by key.

# - Use popitem() method to remove the latest entry.

# - Use clear() method to empty the whole dictionary.

# d) Cz dictionary itself can be pointed to a new dictionary :
my_dict = {
    'name': 'Rahul SriRam',
    'gender': 'Male',
    'hobbies': hobbies
}

# NOTE:
# 1) 'del' keyword can be used to :
# - To remove a pair with a specific key :

# - To erase the dictionary from memory itself :

# 2) Accessing keys, values and pairs of  a dictionary :
# - For keys, we use the keys() method : List of keys

# - For values, we use the values() method : List of values

# - For pairs, we use items() method : List of Tuples of pairs

'''
3) The following will be discussed in the coming videos :
- Copying dictionaries, copy(), Deep VS Shallow Copying and References.
- update(), setdefault() and fromkeys() methods.
- Dictionary Comprehensions.
- Zipping, UnZipping, Packing, UnPacking, and the splat operator.
- enumerate() function.
'''
