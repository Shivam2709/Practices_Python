# Problem: Reverse a number using a loop.

num = input("Enter a number: ")
rev =""

for i in num:
    rev = i + rev
print("Reversed number:", rev)