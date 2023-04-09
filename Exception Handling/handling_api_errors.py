'''
When working with APIs, its essential to handle errors gracefully 
and provide meaningful feedback to users.
'''

import requests

url = 'https://api.example.com/data'

try:
    response = requests.get(url)
    response.raise_for_status()
except requests.exceptions.HTTPError as e:
    print(f'An HTTP error occured: {e}')
except requests.exceptions.ConnectionError as e:
    print(f'A connectino error occured: {e}')
except requests.exceptions.Timeout as e:
    print(f'A timeout error occured: {e}')
except requests.exceptions.RequestException as e:
    print(f'An unknown error occured: {e}')
else:
    print(response.json())
