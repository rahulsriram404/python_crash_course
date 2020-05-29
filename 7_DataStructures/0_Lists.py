# 7) DATA-STRUCTURES : ITERABLES

# 7A) LISTS : Ordered, Mutable, Duplicates-Allowed
my_list = [1, 5.5, 3 + 3j, True, 'Johnny', 1]
print(my_list)
print(len(my_list))
print(type(my_list))

# 7A1) How is it ordered?
# Cz elements can be accessed by indices

# 7A2) How is it mutable?
# a) Cz Assigning is possible :

# b) Cz Adding Elements is possible : append(), insert()
# - Use append() method to insert at last.

# - Use insert() method to insert at a specific index.

# c) Cz Removing Elements is possible : remove(), pop(), clear() methods.
# - Use remove() method to remove by value.

# - Use pop() method to remove by index. Defaults to last index.

# - Use clear() method to empty the whole list.

# d) Cz list itself can be pointed to a new list :
my_list = ['Stack', 'Queue', 'Tree', 'Graph', 'List', 'Set', 'Map', 'Heap']

# NOTE: 
# 1) 'del' keyword can be used to :
# - To remove an element at a specific index : By value isn't possible

# - To erase the list from memory itself :

'''
2) The following will be discussed in the coming videos :
- Negative Indexing.
- Joining lists and extend()
- Copying lists, copy(), Deep VS Shallow Copying and References
- index(), reverse(), sort() methods
- List Slicing, and List Comprehensions
'''