# 7B) SETS : UnOrdered, Mutable, Duplicates-Not-Allowed(By Object, not by value)

my_set = {1, 5.5, True, 3 + 3j, 1, 'Johnny', 5.5}
print(my_set)
print(len(my_set))
print(type(my_set))

'''
7B1) How is it UnOrdered?
Cz elements can't be accessed by indices, since there isn't any indexing
'''

# 7B2) Why is it Mutable?

# a) Cz Adding Elements is possible :

# - Use add() method to insert 1 element.
my_set.add('rahul')
print(my_set)

# - Use update() method to insert a list/tuple/set of elements.
my_set.update(['x', 'y', 'z'])
# my_set.update(('x', 'y', 'z'))
# my_set.update({'x', 'y', 'z'})
print(my_set)

# b) Cz Removing Elements is possible :

# - Use remove() method to remove by value, but will raise an error if the element doesn't exist.
my_set.remove('x') # Removes 'x'
# my_set.remove('123') # ERROR!
print(my_set)

# - Use discard() method to remove by value, but won't raise an error if the element doesn't exist.
my_set.discard('123') # No error
my_set.discard('x') # Removes 'x'
print(my_set)

# - Use pop() method to remove and return the last element.
x = my_set.pop()
print(x) # Random
print(my_set)

# - Use clear() method to empty the whole set.
my_set.clear()
print(my_set) # Not {}. This is used in empty dictionaries. We get set()

# NOTE:

# 1) Set itself can be pointed to a new set :
my_set = {'Stack', 'Queue', 'Tree', 'Graph', 'List', 'Set', 'Map', 'Heap'}
print(my_set)

# 2) Can be erased from the memory. Single element can't be erased like in lists, cz index-based accessing isn't possible.
del my_set
print(my_set)

'''
3) The following will be discussed in the coming videos :
- union(), intersection(), difference(), and symmetric_difference() methods.
- All 4 updating methods in detail:
    - update()
    - intersection_update()
    - difference_update()
    - symmetric_difference_update()
- isdisjoint(), issubset(), and issuperset() methods.
- copy() method, Deep VS Shallow Copying, References.
- What is wrong with booleans in Sets?
- Set-Comprehensions.
- Frozen-Sets
'''
