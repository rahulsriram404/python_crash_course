# 7B) SETS : UnOrdered, Mutable, Duplicates-Not-Allowed(By Object, not by value)
my_set = {1, 5.5, 3 + 3j, 1, 'Johnny', 5.5}
print(my_set)
print(len(my_set))
print(type(my_set))

# 7B1) How is it UnOrdered?
# Cz elements can't be accessed by indices, since there isn't any indexing.

# 7B2) Why is it Mutable?
# a) Cz Adding Elements is possible :
# - Use add() method to insert 1 element.

# - Use update() method to insert a list/tuple/set of elements.

# b) Cz Removing Elements is possible :
# - Use remove() method to remove by value, but will raise an error if the element doesn't exist.

# - Use discard() method to remove by value, but won't raise an error if the element doesn't exist.

# - Use pop() method to remove and return the last element.

# - Use clear() method to empty the whole set.
my_set.clear()
print(my_set)

# NOTE:
# 1) Set itself can be pointed to a new set :
my_set = {'Stack', 'Queue', 'Tree', 'Graph', 'List', 'Set', 'Map', 'Heap'}

# 2) Can be erased from the memory. Single element can't be erased like in lists.

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