'''
NOTE :
1) Context Managers, and Enums will be discussed later in this Python Series.
2) list, tuple, set, dict, and range functions/constructors are used for type-conversions.
'''
# 3) ITERABLE CONSTRUCTORS :

# TASK: Create a list from other iterables :
my_tuple = (1, 5.5, 3 + 3j, True, 'Johnny', 1)
my_set = {1, 5.5, 3 + 3j, 1, 'Johnny', 5.5}
my_dict = {
    'first_name': 'Rahul',
    'last_name': 'SriRam',
    'age': 19,
    'age': 20
}
my_list1 = list(my_tuple) # Similarly, list(my_set)
# Do not confuse with []

# Dictionary's keys() and values() methods already return lists.

# TASK: Create a set from other iterables : Deletes duplicates!

# TASK: Create a dictionary from 2 lists.
keys_list = ['name', 'age', 'is_male']
values_list = ['Roger Federer', 38, True]
