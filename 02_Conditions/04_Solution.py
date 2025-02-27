# Problem: Determine if a fruit is ripe, overripe, or unripe based on its color. (e.g., Banana: Green - Unripe, Yellow - Ripe, Brown - Overripe)

fruitColor = input('Enter the fruitCrolor: ')

if fruitColor == 'green':
    print('The fruit is unripe.')
elif fruitColor == 'yellow':
    print('The fruit is ripe.')
elif fruitColor == 'brown':
    print('The fruit is overripe.')
else:
    print('The fruit is not ripe yet.')