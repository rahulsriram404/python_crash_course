'''
NOTE :

1) Context Managers, and Enums will be discussed later in this Python Series.
2) list, tuple, set, dict, and range functions/constructors are used for type-conversions.
'''

# 3) ITERABLE-CONSTRUCTORS :

# TASK: Create a list from other iterables :
my_tuple = (1, 5.5, 3 + 3j, True, 'Johnny', 1)
my_set = {1, 5.5, 3 + 3j, 1, 'Johnny', 5.5}
my_dict = {
    'first_name': 'Rahul',
    'last_name': 'SriRam',
    'age': 19,
    'age': 20
}
my_list1 = list(my_tuple) 
my_list2 = list(my_set)
print(my_list1)
print(my_list2)

# Do not confuse with []
my_list1 = [my_tuple] # or use 'my_set' too
print(my_list1)

# Dictionary's keys() and values() methods already return lists.

# TASK: Create a set from other iterables : Deletes duplicates!
my_set1 = set(my_tuple)
my_set2 = set(my_list1)
my_set3 = set(my_dict.items()) # or use, keys()/values()
print(my_set1)
print(my_set2)
print(my_set3)
