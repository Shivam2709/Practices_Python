# Problem: Check if all elements in a list are unique. If a duplicate is found, exit the loop and print the duplicate.

list = ["apple", "banana", "orange", "apple", "mango"]
is_unique = set()

for item in list:
    if item in is_unique:
        print("Duplicate found:", item)
        break
    is_unique.add(item)
