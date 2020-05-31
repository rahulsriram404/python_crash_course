# 5) OPERATORS :

# 5A) ARITHMETIC OPERATORS : +, -, *, /, %, //, **

var_1 = 5
var_2 = 2
print(var_1 + var_2)

# Thier result can be assigned to variables too :
my_sum = var_1 + var_2
print(my_sum)

# Order of execution of operations : 
my_sum = var_1 ** var_2 + 2 # Precedence

# 5B) ASSIGNMENT OPERATORS : +=, -=, *=, /=, %=, //=, **=

x = 5
print(x) # 5
x += 1 
print(x) # 6

# NOTE:

# a) String Concatenation and Interpolation :

first_name = 'Rahul'
last_name = 'SriRam'
age = 19

# TASK: I'm Rahul SriRam and I'm 19yrs old.
# NOTE: Escape-Sequences can be escaped using '\'

# TASK SOLUTION 1: Type-Casting Non-Strings to Strings is essential
print('I\'m ' + first_name + ' ' + last_name + ' and I\'m ' + str(age) + 'yrs old.')

# TASK SOLUTION 2:
my_str = 'I\'m '
my_str += first_name + ' ' + last_name + ' and I\'m ' + str(age) + 'yrs old.'
print(my_str)

# 5C) COMPARISION OPERATORS : ==, !=, >, <, >=, <=

print(5 == 5.0)

# Can be assigned to variables too :
bool_var = (5 <= 4)

print(bool_var)
print(type(bool_var)) # <class 'bool'>

# 5D) LOGICAL OPERATORS : and(&&), or(||), not(!)

bool_var = not 5 <= 4 # Precedence, again
print(bool_var) # True
print(type(bool_var))

# 5E) IDENTITY OPERATORS : is(===), is not(!==)

print(5 is 5.0) # Similar to == (but checks data-type too)
print(5 is not 4) # Similar to != (but checks data-type too)

# Can be assigned to variables too : like comparision operators
bool_var = (5 is 4)
print(bool_var)
print(type(bool_var))

'''
NOTE: 

1) Membership Operators will be discussed later in this video
2) The following will be discussed in the coming videos :
- Chaining Comparision-Operators in Python
'''