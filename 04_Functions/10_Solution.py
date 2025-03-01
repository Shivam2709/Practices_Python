# Problem: Create a recursive function to calculate the factorial of a number.

def factorial(n):
    if n == 1:
        return n
    return n * factorial(n - 1)

num = int(input("Enter a number: "))
print("Factorial of", num, "is", factorial(num))