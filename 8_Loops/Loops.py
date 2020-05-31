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
while i < 6: # FIRST-WHILE-LOOP
    print(i, end=' ')
    i += 1

# 8C) On an iterable :
# 8C1) strings : We can use both while and for loops, since we have index based access.
# TASK: Iterate through any string using for-loop
for char in 'theskinnycoder':
    print(char, end='')
# OR :
my_string = 'theskinnycoder'
for char in my_string:
    print(char, end='')

# TASK: Iterate through the given string using while-loop 
my_string = 'BatMan'
counter = 0
while counter < len(my_string): # SECOND-WHILE-LOOPS
    print(my_string[counter], end='')
    counter += 1

# 8C2) lists and tuples : We can use both while and for loops, since we have index based access.

# TASK: Iterate through a tuple using for-loop
for elem in [1, 2, 3, 4]:
    print(elem, end=' ')
# OR :
my_list = [1, 2, 3, 4]
for elem in my_list:
    print(elem, end=' ')

# TASK: Iterate through the given list using while-loop 
my_tuple = (1, 2, 3, 4)
counter = 0
while counter <= len(my_tuple) - 1: # THIRD-WHILE-LOOP
    print(my_tuple[counter], end=' ')
    counter += 1

# 8C3) sets : We can use only for loops, as index-based access isn't possible.
for elem in {'x', 1, 3 + 4j, 4.3}:  # Unordered printing
    print(elem, end=' ')

# 8C4) range : Excessively used in for-loops.

# TASK: Repeat above while-loop tasks with for-loops using ranges :
# FIRST-WHILE-LOOP :
for x in range(1, 6):
    print(x, end=' ')

# SECOND-WHILE-LOOP
# instead of the following, use a for-in/while loop :
for index in range(0, len(my_string)):
    print(my_string[index], end='')

# THIRD-WHILE-LOOP
# instead of the following, use a for-in/while loop :
for index in range(0, len(my_tuple)):
    print(my_tuple[index], end='')

# TASK: Print the first 10 odd numbers :
for i in range(1, 21, 2):
    print(i, end=' ')

# NOTE: 

# a) TASK: Use 'continue' for the above output.
i = 1
while i < 20:
    if i % 2 == 0:
        i += 1
        continue
    print(i, end=' ')
    i += 1
        
# b) TASK: Demonstrate the use of 'break' in a while-loop.
i = 1
while i < 10:
    if i == 5:
        i += 1
        break
    print(i, end=' ')
    i += 1

# c) 'else-clause' in loops will be discussed in the coming videos.
