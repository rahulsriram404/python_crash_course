# 11) EXCEPTION-HANDLING :

# We use 'try', 'except', 'finally', 'raise' keywords

# 11A) Normal runtime-error prone code : (TASK: Show ZeroDivisionError)
num = int(input('Enter numerator : ')) # Give any 'int'
den = int(input('Enter denominator : ')) # Give 0
print(num / den) # Raises ZeroDivisonError if den == 0
print('hello') # Won't be executed if den == 0! hence, we handle exceptions

# 11B) Exception Handled Code : (TASK: handle multiple-exceptions with ZeroDivisionError and then ValueError)
try:
    num = int(input('Numerator : '))
    den = int(input('Denominator : '))
    result = num / den
except ZeroDivisionError:
    print('Can\'t divide with 0')
except ValueError:
    print('Give in integer only')
except: # To handle any other sorts of Exceptions
    print('This is from global exception handling')
print('hello') # Will be executed for sure!

# 11C) Raise an expression : (TASK: Demonstrate raising a ZeroDivisionError)
try:
    num = int(input('Numerator : '))
    den = int(input('Denominator : '))
    if den == 0:
        raise ZeroDivisionError
    result = num / den
except ValueError:
    pass # To avoid any raised Exception

'''
NOTE: The following will be discussed in the coming videos :
- User-Defined Exceptions
- Differences bw else-block and finally-block
'''
