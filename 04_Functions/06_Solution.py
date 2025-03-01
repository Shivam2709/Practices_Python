# Problem: Create a lambda function to compute the cube of a number.
'''
A lambda function in Python is a small anonymous function that can have any number of arguments but only one expression. It is often used for short, simple functions that don’t require a full def function definition.

When to Use Lambda Functions?
✅ When you need a short function for a single-use case.
✅ When using higher-order functions like map(), filter(), and sorted().
✅ When writing concise and readable code.

⚠ Avoid lambda functions if the logic is complex—use def instead for better readability.

Let me know if you need more examples! 🚀
'''

cube = lambda x: x ** 3

print(cube(3))