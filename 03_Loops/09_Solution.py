# Problem: Check if a number is prime.

num = int(input("Enter a number: "))

is_prime = True

if num < 2:
    is_prime = False
else:
    i = 2
    while i < num:
        if num % i == 0:
            is_prime = False
            break
        i += 1

if is_prime:
    print(num, "is a prime number.")
else:
    print(num, "is not a prime number.")
