# Problem: Given a string, find the first non-repeated character.

str = input("Enter a string: ")
non_repeated = None

for i in str:
    if str.count(i) == 1:   # count function count the number of times a character appears in a string
        non_repeated = i
        break

print("First non-repeated character:", non_repeated)