# Classify a person's age group: Child (< 13), Teenager (13-19), Adult (20-59), Senior (60+).

x = int(input("Enter your age: "))
if x < 13:
    print("Child")
elif x <= 19:
    print("Teenager")
elif x <= 59:
    print("Adult")
else: 
    print("Senoir")