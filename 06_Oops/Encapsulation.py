'''
Encapsulation in Python
Encapsulation is one of the core principles of Object-Oriented Programming (OOP) that restricts direct access to the data and methods inside a class, thereby preventing unintended modification. It is used to bind data (variables) and methods (functions) together and control access using access modifiers.

Benefits of Encapsulation
✅ Data Hiding: Prevents direct access to sensitive data.
✅ Security: Restricts unauthorized modification of important attributes.
✅ Flexibility: Allows controlled access using getter and setter methods.
✅ Code Maintainability: Keeps the internal workings hidden, making the code clean
'''

class Employee:
    def __init__(self, name, salary):
        self.name = name  # Public attribute
        self._department = "IT"  # Protected attribute
        self.__salary = salary  # Private attribute

    def get_salary(self):
        """Public method to access private attribute"""
        return self.__salary

    def set_salary(self, new_salary):
        """Public method to modify private attribute"""
        if new_salary > 0:
            self.__salary = new_salary
        else:
            print("Invalid salary amount")

# Creating an instance
emp = Employee("John", 50000)

# Accessing public attribute
print(emp.name)  # John

# Accessing protected attribute (Not recommended but possible)
print(emp._department)  # IT

# Accessing private attribute (Will raise AttributeError)
# print(emp.__salary)  # ❌ AttributeError: 'Employee' object has no attribute '__salary'

# Accessing private attribute using a public method
print(emp.get_salary())  # 50000

# Modifying private attribute using setter method
emp.set_salary(60000)
print(emp.get_salary())  # 60000
