# Value Error, Index Error, FileNotFoundError, ZeroDivisionError


# Example 1
def process_positive_integer(number):
    if number <= 0:
        raise ValueError('Number must be postive integer.')
    else:
        return number


try:
    process_positive_integer(-8)
except ValueError as e:
    print(f'An error occured: {e}')


# Example 2
names = ['bibek', 'deepak', 'sunil', 'ashish']

try:
    name = names[10]
except IndexError as e:
    print(f'An error occured: {e}')


# Example 3
def divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Oops! Division by zero is not allowed.")
    else:
        print(f"The result is: {result}")
    finally:
        print("The divide function has been executed.")

divide(10, 2)
divide(10, 0)


# Example 4
filename = 'example.txt'

try: 
    with open(filename, 'r') as file:
        data = file.read()
        print(data)
except FileNotFoundError:
    print(f'File not found: {filename}')
except PermissionError as e:
    print(f"Error: permission denied - {filename}")
except IOError:  # same as OSError
    print(f'An I/O error occured while reading {filename}')
else:
    print(f'Successfully read data from {filename}')



'''
 Remember to use try, except, and finally blocks effectively, 
 catch specific exceptions to prevent accidentally suppressing unexpected errors, 
 and raise custom exceptions when necessary to provide clearer error messages.
'''