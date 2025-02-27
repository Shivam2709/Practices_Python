# Problem: Reverse a string using a loop.

str = input("Enter a string: ")
rev =""

for i in str:
    rev = i + rev
print("Reversed string:", rev)