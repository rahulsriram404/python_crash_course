# 7) DATA-STRUCTURES : ITERABLES

# 7A) LISTS : Ordered, Mutable, Duplicates-Allowed

# Initializing an empty list
my_list = []
print(my_list)
print(len(my_list))
print(type(my_list))

# Initializing a list with data
my_list = [5.5, 3 + 3j, 1, None, True, 'Johnny', 1]
print(my_list)
print(len(my_list))
print(type(my_list))

# 7A1) How is it ordered?
# Cz elements can be accessed by indices
print(my_list[2]) # (3+3j)

# 7A2) How is it mutable?
# a) Cz Assigning is possible :
my_list[2] = "Here, a complex should've been there"
print(my_list)

# b) Cz Adding Elements is possible : append(), insert()
# - Use append() method to insert at last.
my_list.append(8)
print(my_list)

# - Use insert() method to insert at a specific index.
my_list.insert(0, None)
print(my_list)

# c) Cz Removing Elements is possible : remove(), pop(), clear() methods.
# - Use remove() method to remove by value.
my_list.remove(1)
print(my_list)

# - Use pop() method to remove by index. Defaults to last index.
my_list.pop(0)
print(my_list)

# - Use clear() method to empty the whole list.
my_list.clear()
print(my_list)

# d) Cz list itself can be pointed to a new list :
my_list = ['Stack', 'Queue', 'Tree', 'Graph', 'List', 'Set', 'Map', 'Heap']
print(my_list)

# NOTE: 

# 1) Accessing an element at an index which isn't present raises an exception.
# print(my_list[12]) # ERROR!

# 2) 'del' keyword can be used to :
# - To remove an element at a specific index : By value isn't possible
del my_list[1]
print(my_list)

# - And to erase the whole list from memory itself :
del my_list
# print(my_list) # ERROR!

'''
3) The following will be discussed in the coming videos :
- Negative Indexing.
- Joining lists and extend()
- Copying lists, copy(), Deep VS Shallow Copying and References
- index(), reverse(), sort() methods
- List Slicing, and List Comprehensions
'''
