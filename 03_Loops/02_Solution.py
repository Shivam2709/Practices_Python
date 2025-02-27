# Problem: Calculate the sum of even numbers up to a given number n.

n = input("Enter a number: ")
sum = 0

for i in range(1, int(n)+ 1):
    if i % 2 == 0:
        sum += i

print("Sum of even numbers up to", n, "is", sum)

