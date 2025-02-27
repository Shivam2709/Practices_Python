# Problem: Check if a password is "Weak", "Medium", or "Strong". Criteria: < 6 chars (Weak), 6-10 chars (Medium), >10 chars (Strong).

password = input('Enter the password: ')
passwordLen = len(password)

if passwordLen < 6:
    print('Weak password.')
elif passwordLen <= 10:
    print('Medium password.')
else:
    print('Strong password.')