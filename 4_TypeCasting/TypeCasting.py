# 4) TYPE-CONVERSIONS AND CASTING :

# 4A) To Integers :

my_int = 5 # int itself doesn't need a type-casting
print(type(my_int))
print(my_int)

my_int = int(5.5) # takes in the decimal part of the float only
print(type(my_int))
print(my_int)

# my_int = int("theskinnycoder") # ERROR!
my_int = int("69") # Not an error, cz value of the string is an integer
print(type(my_int)) # <class 'int'>
print(my_int) # 69

my_int = int(False) # 0
my_int = int(True) # 1
print(type(my_int))
print(my_int) # 1

# 4B) To Floats :
my_float = float(5.5) # float itself doesn't need a type-casting
print(my_float)

my_float = float(5)
print(my_float) # 5.0

# my_float = float("the_skinny_coder") # ERROR!
my_float = float("2e-3") 
print(my_float) # 0.002

my_float = float(False)
print(my_float) # 0.0

# 4C) To Strings :
my_str = "Hello" # string itself doesn't need a type-casting
print(my_str)

my_str = str(3) 
print(type(my_str))
print(my_str) # "3"

my_str = str(5.6)
print(type(my_str))
print(my_str) # "5.6"

my_str = str(True)
print(type(my_str))
print(my_str) # "True"

# 4D) To Booleans :

# NOTE: Refer to Falsy Values in the previous module for a better understanding

my_bool = False # bool itself doesn't need a type-casting
print(type(my_bool))
print(my_bool)

my_bool = bool(1) # True 
my_bool = bool(0)  # False
print(type(my_bool))
print(my_bool) # False

my_bool = bool(0.1) # True, cz non-zero
my_bool = bool(0.0) # False
print(type(my_bool))
print(my_bool) # False

my_bool = bool("Hello") # True, cz non-empty 
my_bool = bool("") # False
print(type(my_bool))
print(my_bool)
