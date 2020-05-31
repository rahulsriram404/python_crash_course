# 3) DATA-TYPES :

# 3A) STRINGS :

# Can use single/double/triple quotes.
my_str = 'Rahul SriRam'
# my_str = "Rahul SriRam"
# my_str = '''Rahul SriRam'''
# my_str = """Rahul SriRam"""
print(my_str)

# len() function can be used to find the length of the string.
print(len('Rahul')) # length of a literal
print(len(my_str)) # length of a string variable's value

# 3B) INTEGERS :
my_int = 7812964872365871658
print(my_int)

# 3C) FLOATS :
my_float = 5.5
print(my_float)

# We can use e/E for powers of 10
f1 = 1e5 # 1 * 10 ^ 5
print(f1) 
f2 = 2E-3 # 2 * 10 ^ -3
print(f2)

# 3D) COMPLEX :
c1 = 3 + 2j
c2 = -4 - 4j
print(c1)
print(c1.real) # gives 3.0(real part)
print(c1.imag) # gives 2.0(imaginary part)

# NOTE :

# a) To check the data-type of any variable/literal : (use type() function)
print(type(c2)) # <class 'complex'>, cz all data-types are classes

# b) None :
my_none = None
print(my_none)
print(type(my_none))

# 3E) BOOLEANS :
bool_variable = True
bool_other_variable = False
print(bool_variable, bool_other_variable)
print(type(bool_variable)) # <class 'bool'>

# '''
# Some Falsy values are :
# - None
# - False
# - 0, 0.0, 0j
# - '', "", '''''', """"""
# - [], (), {}
# '''

'''
NOTE:

The following will be discussed in the coming videos :
1) Functions like abs(), pow(), divmod(), factorial() etc.
2) Math Module.
3) Advanced String Formatting and Manuplulation Methods like f'strings, format() method, printf-style formatting, split(), join() methods etc.
'''
