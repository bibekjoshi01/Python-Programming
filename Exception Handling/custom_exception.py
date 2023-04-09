# Custom exceptions can make your code more readable and easier to understand 
# by providing more descriptive error messages.

# Example 1
class NegativeNumberError(Exception):
    def __init__(self, value):
        self.value = value
    
    def __str__(self):
        return f'Negative numbers are not allowed: {self.value}'


def process_positive_number(number):
    if number < 0:
        raise NegativeNumberError(number)
    return number


try: 
    result = process_positive_number(-9)
    print(result)
except NegativeNumberError as e:
    print(f'An error occured: {e}')


# Exception Inheritence
class PasswordValidationError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class PasswordTooShortError(PasswordValidationError):
    def __init__(self, message='password is too short'):
        super().__init__(message)

class PasswordTooSimpleError(PasswordValidationError):
    def __init__(self, message='password too simple'):
        super().__init__(message)


def validate_password(password):
    if len(password) < 8:
        raise PasswordTooShortError()

    if password.isnumeric() or password.isalpha():
        raise PasswordTooSimpleError
    
    return True


try:
    validate_password('2167')
except PasswordTooSimpleError as e:
    print (e)
except PasswordTooShortError as e:
    print(e)
else:
    print('Good Password')
