'''
6) CONDITIONAL-STATEMENTS : if, elif, else
TASK: Write a program to find if a no. is -ve, 0, +ve (and demonstrate scope)
'''

num = int(input())
if num > 0: 
    print('Greater than zero') # This comes under the scope of 'if-block'
elif num < 0: # Multiple elif statements can be there
    print('Less than zero')
else:
    print('Zero')

'''
NOTE: The following will be discussed in the coming videos :
1) LEGB rule for scope, 'global' and 'nonlocal' statements
2) Terniary Conditionals
'''
