# Problem: Customize a coffee order: "Small", "Medium", or "Large" with an option for "Extra shot" of espresso.

coffeeSize = input('Enter the coffee size: ')
extraShot = input('Do you want an extra shot? (yes/no): ')
 
if coffeeSize == 'small':
    if extraShot == 'yes':
        print('Small coffee with an extra shot of espresso.')
    else:
        print('Small coffee.')
elif coffeeSize == 'medium':
    if extraShot == 'yes':
        print('Medium coffee with an extra shot of espresso.')
    else:
        print('Medium coffee.')
elif coffeeSize == 'large':
    if extraShot == 'yes':
        print('Large coffee with an extra shot of espresso.')
    else:
        print('Large coffee.')
else:
    print('Invalid coffee size.')
