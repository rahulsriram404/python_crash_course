# NOTE: MEMEBRSHIP OPERATORS : in, not in
# - In Strings :
my_string = 'She sells sea shells in the sea shore'

if 'sea' in my_string:
    print('Present')
else:
    print('Not present')

# - In Lists :
my_list = [1, 3 + 4j, 3.4, 'Rahul']

if 1 in my_list:
    print('Present')
else:
    print('Not present')

# - In Tuples :
my_tuple = (1, 3 + 4j, 3.4, 'Hero')

if 'Hero' not in my_tuple:
    print('Not present')
else:
    print('Present')

# - In Sets :
my_set = {43, 2.2, 3, 43}

if 43 in my_set:
    print('Present')
else:
    print('Not present')

# - In Dictionaries :
my_dict = {
    1: 'C++',
    2: 'Python',
    3: 'Java',
}

# By default, keys are used to check. We can use keys() method for that too.
if 'Java' in my_dict:
    print('Present')
else:
    print('Not present')

# We can check in values, using values() method :
if 'Java' not in my_dict.values():
    print('Present')
else:
    print('Not present')

# We can also check pairs, using entries() method : Use tuples
if (3, 'Java') in my_dict.items():
    print('Present')
else:
    print('Not present')
