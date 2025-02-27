# Problem: Suggest an activity based on the weather (e.g., Sunny - Go for a walk, Rainy - Read a book, Snowy - Build a snowman).

weatherType = input('Enter the weather type: ')

if weatherType == 'sunny':
    activity = 'Go for a walk.'
elif weatherType == 'rainy':
    activity = 'Read a book.'
elif weatherType == 'snowy':
   activity = 'Build a snowman.'
print(activity)