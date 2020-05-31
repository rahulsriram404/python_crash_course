# 10) OOPS :

# 10A) TASK: Write a Rectangle class, and add some properties and methods to it.

class Rectangle:
    # Constructor :
    def __init__(self, length, width): # dunder/magic method
        self.length = length
        self.width = width
    
    def perimetre(self):
        return 2 * (self.length + self.width)

# 10B) TASK-2 : Instantiate objects to the class.
rect1 = Rectangle(3, 4)
rect2 = Rectangle(5, 6)
print(rect1.perimetre())

# 10C) TASK-3 : Repeat the same for a sub-class called Square.
class Square(Rectangle): # Inheritance
    def __init__(self, side):
        super().__init__(side, side)
    
    def area(self):
        return self.length ** 2

# Instantiating objects to the Square class
sqr = Square(3)
print(sqr.area())

'''
NOTE: The following will be discussed in the coming videos :
- Static properties and methods
- Decorators, arguments to decorators
- Getters, Setters and Deleters
- Magic Methods or Dunder Methods
'''
