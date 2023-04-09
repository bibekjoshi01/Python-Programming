import re


def email_validator(*emails):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    pattern = re.compile(pattern)
    results = []
    for email in emails:
        if pattern.fullmatch(email):
            results.append(True)
        else:
            results.append(False)
    return results


emails = ('bibek@gmail.com', 'john.doe@hotmail.com', 'admin_01.@bibek.com.com', 'john.doe@com@domain.com', 'john.doe@com')
results = email_validator(*emails)

for i, email in enumerate(emails):
    '''Instead of using a separate variable to keep track of the index, 
    you can use enumerate() to generate the pairs of (index, value) for each item in the sequence.'''
    if results[i]:
        print(email, "is valid")
    else:
        print(email, "is invalid")
