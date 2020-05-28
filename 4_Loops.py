# 8) LOOPS:
# Using Loops, we can iterate :
# a) through a collection - for
# b) until a condition is satisfied - while
# c) on iterables

# 8A) On a collection of elements : (Generally, for-loop)
for x in 1, 2, 3, 4:
    print(x, end=' ')

# 8B) Until a condition is satisfied : (Generally, while-loop)
i = 1
while i < 6:
    print(i, end=' ')
    i += 1

# 8C) On an iterable :
# 8C1) strings : We can use both while and for loops, since we have index based access.
# TASK: Iterate through any string using for-loop

# TASK: Iterate through the given string using while-loop 
my_string = 'BatMan'

# 8C2) lists and tuples : We can use both while and for loops, since we have index based access.
# TASK: Iterate through a tuple using for-loop

# TASK: Iterate through a list using while-loop 
my_list = [1, 2, 3, 4]

# 8C3) sets : We can use only for loops, as index-based access isn't possible.
for elem in {'x', 'x', 1, 3 + 4j, 4.3}:  # Unordered printing
    print(elem, end=' ')

# 8C4) range : Excessievly used in for-loops.
# TASK: Repeat above above while-loop tasks with for-loops using ranges :

# TASK: Print the first 10 odd numbers :
for i in range(1, 21, 2):
    print(i, end=' ')

# NOTE: 
# a) TASK: Use 'continue' for the above output.
        
# b) TASK: Demonstrate the use of 'break' in a while-loop.

# c) 'else-clause' in loops will be discussed in the coming videos.
