# Problem: Compute the factorial of a number using a while loop.

num = input("Enter a number: ")

fact = 1
i = 1
while i <= int(num):
    fact *= i
    i += 1

print("Factorial of", num, "is", fact)