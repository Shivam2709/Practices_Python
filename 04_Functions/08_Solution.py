# Problem: Create a function that accepts any number of keyword arguments and prints them in the format key: value.

def print_all(**kwargs):
    for key, value in kwargs.items():
        print(f'{key}: {value}')

print_all(name='John', age=25, city='New York')
print_all(name='Jane', age=30, city='London')