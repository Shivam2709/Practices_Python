# Problem: Assign a letter grade based on a student's score: A (90-100), B (80-89), C (70-79), D (60-69), F (below 60).

prec = int(input("Enter your precentage: "))

if prec >= 90:
    print("A")
elif prec >= 80:
    print("B")
elif prec >= 70:
    print("C")
elif prec >= 60:
    print("D")
else:
    print("F")