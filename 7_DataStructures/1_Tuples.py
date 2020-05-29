# 7B) TUPLES : Ordered, Immutable, Duplicates-Allowed
my_tuple = (1, 5.5, 3 + 3j, True, 'Johnny', 1)
print(my_tuple)
print(len(my_tuple))
print(type(my_tuple))

# 7B1) How is it ordered?
# Cz elements can be accessed by indices

# 7B2) Why is it immutable?
# a) Cz Assigning and Adding Elements isn't possible! But :
# Convert to a List, assign/add elements, and convert back to Tuple.
my_tuple = list(my_tuple)
my_tuple.append('Python') # or use insert(), or change a value
my_tuple = tuple(my_tuple)

# b) Cz Removing Elements isn't possible! But :
# Convert to a List, remove elements, and convert back to Tuple.
my_tuple = list(my_tuple)
my_tuple.remove('Python') # or use del, pop(), clear()
my_tuple = tuple(my_tuple)

# NOTE:
# 1) Tuple itself can be pointed to a new tuple :
my_tuple = ('Stack', 'Queue', 'Tree', 'Graph', 'List', 'Set', 'Map', 'Heap')

# 2) Can be erased from the memory : using 'del'. Single element can't be erased like in lists.

'''
3) These following will be discussed in this Python Series :
- Intitialize a tuple with 1 element.
- Negative Indexing.
- Joining tuples.
- Copying tuples, Deep VS Shallow Copying and References.
- index(), sort() methods.
- Tuple Slicing, and Tuple Comprehensions.
- NamedTuples
'''