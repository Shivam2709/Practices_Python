# Problem: Write a function to calculate and return the square of a number.

def square(num):
    return num**2

num = int(input("Enter a number: "))
print("Square of", num, "is", square(num))