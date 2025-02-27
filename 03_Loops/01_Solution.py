# Problem: Given a list of numbers, count how many are positive.
# Input :- [1, -2, 3, -4, 5, 6, -7, -8, 9, 10]

listA = [1, -2, 3, -4, 5, 6, -7, -8, 9, 10]
count = 0 

for i in listA:
    if i > 0:
        count += 1

print("Total positive numbers in the list:", count)