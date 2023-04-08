#  A Regular Expression (RegEx) is a sequence of characters that defines a search pattern.

import re

pattern = '^m....e$'  # any six letter string starting with m and ending with e.
test_string = 'mobile'

result = re.match(pattern, test_string)

if result:
    print('Matched')
else:
    print('Not Matched')

