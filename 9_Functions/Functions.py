# 9) FUNCTIONS :

# 9A) TASK: Write a function taking in no paramters, without a return statement

# 'pass' statement can be used to temporarily avoid errors in conditionals, loops, functions and classes

def func_1(): # Function Definition and Declaration
    print('Hello, World!')

func_1() # Function Call

# 9B) TASK: Write a function taking in paramters, without a return statement
def func_2(num1, num2):
    print('The sum is : ' + str(num1 + num2))

func_2(5, 6)

# 9C) TASK: Write a function taking in no paramters, with a return statement
def pi():
    return 3.14
r = 2
print('Area is : ' + str(pi() * (r ** 2)))
var_pi = pi()
print(var_pi)

# 9D) TASK: Write a function taking in paramters, with a return statement
def my_sum(x, y):
    return x + y

print(my_sum(3, 4))

'''
NOTE: The following will be discussed in the coming videos :
- First-Class Functions, Higher-Order Functions, and Lambdas
- Multiple arguments to functions
- Command-Line Arguments
- Zipping, UnZipping, Packing, UnPacking and the 'splat' operator.
'''
