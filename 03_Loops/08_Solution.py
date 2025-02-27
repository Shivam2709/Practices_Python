# Problem: Keep asking the user for input until they enter a number between 1 and 10.

while True:
    num = input("Enter a number between 1 and 10: ")
    if num.isdigit() and 1 <= int(num) <= 10:
        break
    else:
        print("Invalid input. Try again.")