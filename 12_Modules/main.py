# 12) MODULES :
# 12A) TASK: Write some utitility functions in 'library.py' and use them here.
import library


print(library.square_up(7))

print(list(library.my_dict.keys())[0]) # 'name'

# 12B) Using aliases (TASK: Rename the imported module)
import library as lib


# print(library.square_up(7)) # ERROR!
print(lib.square_up(7))
print(lib.pi) # 3.14

# 12C) Importing Standard Library Modules (TASK: use the 'math' module)
import math


print(math.sqrt(16)) # 4

# 12D) 'from' keyword (TASK: Show how accessing variables differs)
from library import square_up


print(square_up(5)) # 25
# print(library.square_up(5)) # ERROR!

# We can alias the imported function too
from library import square_up as func

# print(square_up(5)) # ERROR!
print(func(5))

'''
NOTE: The following will be discussed in the coming videos :
- Differences bw modules and packages
- Writing packages
'''
