'''
Inheritance is an Object-Oriented Programming (OOP) concept that allows a class (child class) to derive properties and behavior from another class (parent class). It promotes code reusability and establishes a relationship between classes.

Types of Inheritance in Python
1. Single Inheritance → One parent, one child
2. Multiple Inheritance → A child inherits from multiple parents
3. Multilevel Inheritance → Inheritance in multiple levels
4. Hierarchical Inheritance → Multiple child classes from the same parent
5. Hybrid Inheritance → A combination of different types of inheritance

Benefits of Inheritance
✅ Code Reusability – Reduces code duplication by reusing parent class code.
✅ Maintainability – Easier to manage and update code in one place.
✅ Scalability – Easily extend functionality by adding new classes.
✅ Polymorphism Support – Helps in overriding methods in child classes.

Would you like an example using inheritance in a real-world application? 
'''

# Single Inheritance
# When a child class inherits from a single parent class.

# Example: Single Inheritance in Python
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Some generic sound"

class Dog(Animal):  # Dog inherits from Animal
    def speak(self):
        return "Woof! Woof!"

# Creating objects
animal = Animal("Generic Animal")
dog = Dog("Buddy")

print(animal.speak())  # Some generic sound
print(dog.speak())     # Woof! Woof!

# Multiple Inheritance
# When a child class inherits from multiple parent classes.

# Example: Multiple Inheritance in Python
class Animal:
    def eat(self):
        return "Eating..."

class Bird:
    def fly(self):
        return "Flying..."

class Bat(Animal, Bird):  # Inherits from both Animal and Bird
    pass

bat = Bat()
print(bat.eat())  # Eating...
print(bat.fly())  # Flying...

# Multilevel Inheritance
# When a child class inherits from a parent class, and another class inherits from the child class.

# Example: Multilevel Inheritance in Python
class Animal:
    def breathe(self):
        return "Breathing..."

class Mammal(Animal):  # Mammal inherits from Animal
    def walk(self):
        return "Walking..."

class Human(Mammal):  # Human inherits from Mammal
    def talk(self):
        return "Talking..."

human = Human()
print(human.breathe())  # Breathing...
print(human.walk())     # Walking...
print(human.talk())     # Talking...


# Hierarchical Inheritance
# When multiple child classes inherit from the same parent class.

# Example: Hierarchical Inheritance in Python
class Animal:
    def move(self):
        return "Moving..."

class Dog(Animal):
    def bark(self):
        return "Barking..."

class Cat(Animal):
    def meow(self):
        return "Meowing..."

dog = Dog()
cat = Cat()

print(dog.move())  # Moving...
print(dog.bark())  # Barking...
print(cat.move())  # Moving...
print(cat.meow())  # Meowing...


# Hybrid Inheritance
# A combination of different types of inheritance.

# Example: Hybrid Inheritance in Python
class A:
    def method_A(self):
        return "Method A"

class B(A):
    def method_B(self):
        return "Method B"

class C(A):
    def method_C(self):
        return "Method C"

class D(B, C):  # Inherits from both B and C
    def method_D(self):
        return "Method D"

d = D()
print(d.method_A())  # Method A (from A)
print(d.method_B())  # Method B (from B)
print(d.method_C())  # Method C (from C)
print(d.method_D())  # Method D (from D)

# The super() Function
# The super() function allows you to call methods from the parent class inside a child class.


# Example: Using super() in Python
class Animal:
    def __init__(self, name):
        self.name = name

    def show_name(self):
        return f"Animal name: {self.name}"

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)  # Calls the parent constructor
        self.breed = breed

    def show_info(self):
        return f"{self.show_name()}, Breed: {self.breed}"

dog = Dog("Buddy", "Golden Retriever")
print(dog.show_info())  # Animal name: Buddy, Breed: Golden Retriever
