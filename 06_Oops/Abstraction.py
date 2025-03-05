'''
Abstraction is one of the core principles of Object-Oriented Programming (OOP) that hides implementation details and only exposes the necessary features. It helps in simplifying complex systems by showing only relevant attributes and behaviors.

How is Abstraction Implemented in Python?
Python achieves abstraction using:

Abstract Base Classes (ABCs)
The abc module
To create an abstract class, you need to:

Import the ABC class from the abc module.
Use @abstractmethod to define abstract methods.

Benefits of Abstraction
✅ Hides Complexity → The user only sees necessary details.
✅ Improves Security → Internal implementation is hidden.
✅ Enforces Standardization → Child classes must implement certain methods.
✅ Enhances Code Reusability → Common features are defined in abstract classes.

Would you like a real-world example, such as an abstract class for payment processing? 
'''

# Example: Abstraction in Python
from abc import ABC, abstractmethod

# Abstract Class
class Animal(ABC):
    @abstractmethod
    def make_sound(self):  # Abstract method (must be implemented by child classes)
        pass

# Concrete Class (inherits from Animal)
class Dog(Animal):
    def make_sound(self):
        return "Woof! Woof!"

class Cat(Animal):
    def make_sound(self):
        return "Meow! Meow!"

# Creating objects
dog = Dog()
cat = Cat()

print(dog.make_sound())  # Woof! Woof!
print(cat.make_sound())  # Meow! Meow!
