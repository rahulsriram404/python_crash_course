# 7D) RANGES : Special data-structures to create a range of numbers with a given step

# Mostly used in for-loops and to create APs, i.e., Arithmetic Progressions.

# range(start, stop, end)
# where, Start is inclusive, End is exculsive, Step defaults to 1.

my_range = range(1, 11, 2) 
print(len(my_range))
print(type(my_range))
print(my_range) # <class 'range'>

print(my_range[0])
print(my_range[1])
print(my_range[2])
print(my_range[3])
print(my_range[4])
# print(my_range[5]) # IndexError
