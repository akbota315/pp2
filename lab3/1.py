#1
class StringManipulator:
    def getString(self):
        self.s = input("Enter a string: ")

    def printString(self):
        print(self.s.upper())


string_obj = StringManipulator()
string_obj.getString()
string_obj.printString()

#2
class Shape:
    def area(self):
        return 0

class Square(Shape):
    def __init__(self, length):
        self.length = length
    
    def area(self):
        return self.length ** 2

# Example
square_obj = Square(4)
print(square_obj.area())

#3
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width

# Example
rectangle_obj = Rectangle(4, 5)
print(rectangle_obj.area())

#4
import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def show(self):
        print(f"Point({self.x}, {self.y})")
    
    def move(self, dx, dy):
        self.x += dx
        self.y += dy
    
    def dist(self, other_point):
        return math.sqrt((self.x - other_point.x)**2 + (self.y - other_point.y)**2)

# Example 
point1 = Point(3, 4)
point2 = Point(6, 8)
point1.show()
point1.move(1, 1)
point1.show()
print(point1.dist(point2))

#5
class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
    
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient funds!")

# Example
account = Account("John", 1000)
account.deposit(500)
account.withdraw(300)
account.withdraw(1500)

#6
def is_prime(n):
    return n > 1 and all(n % i != 0 for i in range(2, int(n ** 0.5) + 1))

numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
prime_numbers = list(filter(lambda x: is_prime(x), numbers))
print(prime_numbers)