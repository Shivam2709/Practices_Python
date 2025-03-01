# Problem: Write a function that greets a user. If no name is provided, it should greet with a default name.

def greet(name= "User"):
    return f"Hello, {name}!"

print(greet())
print(greet("John"))