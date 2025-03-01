# Problem: Write a generator function that yields even numbers up to a specified limit.

def even_numbers(limit):
    for i in range(0, limit + 1, 2):
        yield i

for num in even_numbers(10):
    print(num)