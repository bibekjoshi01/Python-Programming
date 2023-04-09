from . constants import pattern


def validate_email(email):
    if pattern.fullmatch(email):
        return True
    else:
        raise ValueError('Invalid Email !')
