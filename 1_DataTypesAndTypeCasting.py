# 2) VARIABLES :
'''
NOTE:
a) No data-type is needed to be mentioned when declaring.
b) Naming rules :
    1) Can contain alpha-numeric characters(A-z, 0-9) and underscore(_), but can't start with numbers.
    2) Case-Sensitive.
c) Variables can't be just declared and left, they have to be initialized at the time of declaration only :
'''

# 2A) Declaration and Initialisation :
x = 5 # Use the assignment operator to assign literals/values to variables.

# print() can print the variable's value or the value itself to the console
print(x)
print(5)

# 2B) Assign another value to already declared variable :
x = 6
print(x)

# 3) DATA-TYPES :
# 3A) STRINGS :
# Can use single/double/triple quotes.

# len() function can be used to find the length of the string.
print(len('Rahul'))

# 3B) INTEGERS :

# 3C) FLOATS :

# We can use e/E for powers of 10
f1 = 1e5 # 1 * 10 ^ 5
print(f1) 

# 3D) COMPLEX :
c1 = 3 + 2j
c2 = -4 - 4j
print(c1)
print(c1.real)
print(c1.imag)

# NOTE :
# a) To check the data-type of any variable/literal : (use type() function)

# b) None :
my_none = None
print(my_none)
print(type(my_none))

# 3E) BOOLEANS :
bool_variable = True
print(bool_variable)
print(type(bool_variable))

'''
Some Falsy values are :
- None
- False
- 0, 0.0, 0j
- '', ""
- [], (), {}
'''

# 4) TYPE-CONVERSIONS AND CASTING :
# 4A) To Integers :
my_int = 5
print(my_int)
my_int = int(5.5)
print(my_int)
my_int = int("5")
print(my_int)
my_int = int(True)
print(my_int)

# 4B) To Floats :
my_float = 5.5
print(my_float)
my_float = float(5.5)
print(my_float)
my_float = float("5.6")
print(my_float)
my_float = float(True)
print(my_float)

# 4C) To Strings :
my_str = "Hello"
print(my_str)
my_str = str(3)
print(my_str)
my_str = str(5.6)
print(my_str)
my_str = str(True)
print(my_str)

# 4D) To Booleans :
my_bool = True
print(my_bool)
my_bool = bool(5)
print(my_bool)
my_bool = bool(33.3)
print(my_bool)
my_bool = bool("Hello, World")
print(my_bool)

'''
NOTE :
The following will be discussed in the coming videos :
1) Functions like abs(), pow(), divmod(), factorial() etc.
2) Math Module.
3) Advanced String Formatting and Manuplulation Methods like f'strings, format() method, printf-style formatting, split(), join() methods etc.
'''