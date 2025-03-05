'''
Polymorphism is one of the key principles of Object-Oriented Programming (OOP) that allows methods or functions to take multiple forms. It enables code reusability and flexibility by allowing different classes to use the same interface.

Types of Polymorphism in Python
Method Overriding (Runtime Polymorphism)
Method Overloading (Not natively supported in Python)
Operator Overloading
Duck Typing (Dynamic Polymorphism)

Benefits of Polymorphism
✅ Code Reusability – The same interface works for different objects.
✅ Flexibility – New classes can be added without modifying existing code.
✅ Readability & Maintainability – Makes the code more structured and easier to understand.

Would you like an example where polymorphism is used in a real-world scenario?
'''

# Method Overriding (Runtime Polymorphism)
# When a child class provides a different implementation of a method already defined in its parent class. It is also known as runtime polymorphism because the method that needs to be executed is determined at runtime.

# Example: Method Overriding in Python
class Animal:
    def speak(self):
        return "Animal makes a sound"

class Dog(Animal):
    def speak(self):
        return "Woof! Woof!"  # Overriding parent method

class Cat(Animal):
    def speak(self):
        return "Meow! Meow!"

# Polymorphic behavior
animals = [Dog(), Cat(), Animal()]

for animal in animals:
    print(animal.speak())  


# Method Overloading (Not Natively Supported)
# Python does not support traditional method overloading (same method name with different parameters). However, we can achieve similar functionality using default arguments or *args / **kwargs.

# Example: Method Overloading in Python
class Calculator:
    def add(self, a, b, c=0):  # Default parameter for method overloading
        return a + b + c

calc = Calculator()
print(calc.add(2, 3))     # 5
print(calc.add(2, 3, 4))  # 9

# Operator Overloading
# Python allows us to redefine built-in operators for user-defined objects.

# Example: Operator Overloading in Python
class Book:
    def __init__(self, pages):
        self.pages = pages

    def __add__(self, other):
        return Book(self.pages + other.pages)  # Overloading '+' operator

    def __str__(self):
        return f"Book with {self.pages} pages"

book1 = Book(100)
book2 = Book(200)

book3 = book1 + book2  # Calls __add__ method
print(book3)  # Book with 300 pages

# Duck Typing (Dynamic Polymorphism)
# In Python, if an object behaves like a duck (has the same method name), we treat it as a duck.

# Example: Duck Typing in Python
class Bird:
    def fly(self):
        return "Bird is flying"

class Airplane:
    def fly(self):
        return "Airplane is flying"

def perform_flight(entity):
    return entity.fly()  # Doesn't check type, just calls fly()

print(perform_flight(Bird()))      # Bird is flying
print(perform_flight(Airplane()))  # Airplane is flying


